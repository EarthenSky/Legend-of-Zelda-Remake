'''This class handles the drawing and checking for interaction or collision.
The player class interacts with this class.'''

import sys
import __builtin__  # TODO: PLEASE NO!!!

# Constants.
SCREEN_SIZE = [240 * 4, 160 * 4]

ANIMATION_SPEED = 0.138*1.6  # 1.6 times more than 0.138s or 138ms per frame.

# The asset manager helps render images.
sys.path.insert(0, 'src/managers/')  # This line tells the importer where to look for the module.
import asset_manager
import desc_manager

class Tilemap:
    # This function converts the tile map into a matrix of tuples.
    def _create_map(self, map_file_name, map_matrix):
        # Create the string matrix from the map's text.
        with open("resc/maps/{}".format(map_file_name), 'r') as map_file:
            # Loop through each line.
            for line in map_file:
                read_row_list = ' '.join(line.split()).split(" ")  # Obtain each item and make it a list..replace('\n', '')

                out_row_list = []  # The list to add to the matrix.

                ### For the map tuples:
                ### 0 == ao, or animation tile over the second tile.  (flowers)
                ### 1 == au, or animation tile under the second tile.  (water)
                ### 2 == none, a regular tile.
                ### 3 == tb, dual tiles, draw the second tile over the player.  (Tree tops)
                ### 4 == b, dual tiles, draw the second tile under the player.  (fence w/ grass)

                # Loop thorugh each tile in the list.
                for tile_string in read_row_list:
                    # Convert the strings into numbers so it runs faster.
                    if tile_string.find('ao') != -1:  # Case: found an 'a'.  the o stands for 'over' as in the top image is an animation.
                        # Get the 3 variables from the string.
                        group, depth, group2 = tile_string.replace(' ', '').replace('ao', ',').split(',')
                        out_row_list.append( (0, int(group), int(depth), int(group2)) )  # Add the tuple to the list.

                    elif tile_string.find('au') != -1:  # Case: found an 'a'.  the u stands for 'under' as in the bottom image is an animation.
                        # Get the 4 variables from the string.
                        group, group2, depth2 = tile_string.replace(' ', '').replace('au', ',').split(',')
                        out_row_list.append( (1, int(group), int(group2), int(depth2)) )  # Add the tuple to the list.

                    elif tile_string.find('t') == -1:  # -1 means cannot find.
                        # Get the two variables from the string.
                        group, depth = tile_string.replace(' ', '').split(',')
                        out_row_list.append( (2, int(group), int(depth)) )  # Add the tuple to the list.

                    else:
                        if tile_string.find('b') == -1:  # -1 means cannot find.
                            # Get the 4 variables from the string.
                            group, depth, group2, depth2 = tile_string.replace(' ', '').replace('t', ',').split(',')
                            out_row_list.append( (3, int(group), int(depth), int(group2), int(depth2)) )  # Add the tuple to the list.

                        else:
                            # Get the 4 variables from the string.
                            group, depth, group2, depth2 = tile_string.replace(' ', '').replace('tb', ',').split(',')
                            out_row_list.append( (4, int(group), int(depth), int(group2), int(depth2)) )

                map_matrix.append(out_row_list)  # Add the modified list to the matrix.

    def __init__(self, map_file_name, draw_relative_position, img=0):
        self.position = [0, 0]  # The world position of the map.

        self.draw_relative_position = draw_relative_position  # The draw relative position.

        self.map_matrix = []  # Init the matrix.
        self._create_map(map_file_name, self.map_matrix)  # Fill the matrix.

        # Is this object drawing from a batch of images or one large one?
        self.image_passed = False

        # Check if image was passed.
        if img != 0:
            self.image_passed = True
            self._img = img

        # The list that holds all the draw functions for the items drawn after the player.
        self.over_tile_queue = []

        # The animation frame that the tilemap is on. (affects all the sprites at the same time.)
        # Note: this variable goes to 8 frames cause some animations are 8 frames long.
        self._animation_frame = 0
        self._animation_timer_val = 0

        self._triggered_animations = []  # the format for animations is (x, y, animation_type, animation_frame, last_frame)

    # For type, 2 is grass...
    def trigger_animation(self, x, y, animation_type):
        self._triggered_animations.append( [x, y, animation_type, 0, 4] )

    # Gets the player's 'offset' tuple which contains a position and what to do with it.
    # The tuple can be translation or assignation.
    def get_offset(self, offset):
        # 0 == translate, 1 = set_pos
        if offset[0] == 0:
            self.position[0] += offset[1]
            self.position[1] += offset[2]
        else:
            self.position[0] = offset[1]
            self.position[1] = offset[2]

    def draw(self, surface):
        if not self.image_passed:
            # Reset the over tile queue.
            self.over_tile_queue = []

            # Loop thorough the matrix and find / draw all the tiles.
            for row_index in range(len(self.map_matrix)):
                for column_index in range(len(self.map_matrix[row_index])):
                    pos_x = column_index * 64 + self.position[0]
                    pos_y = row_index * 64 + self.position[1]

                    # Only draw the tile if it is inside the screen.
                    if pos_x + self.draw_relative_position[0] >= -64 and pos_x + self.draw_relative_position[0] <= SCREEN_SIZE[0] + 64 and pos_y + self.draw_relative_position[1] >= -64 and pos_y + self.draw_relative_position[1] <= SCREEN_SIZE[1] + 64:
                        # Choose hjow to draw this tile.
                        if self.map_matrix[row_index][column_index][0] == 0:  # Case: ao, animation over.
                            # Draw the two tiles, the animation is the top tile.
                            asset_manager.draw_tile(surface, (pos_x + self.draw_relative_position[0], pos_y + self.draw_relative_position[1]), self.map_matrix[row_index][column_index][1], self.map_matrix[row_index][column_index][2]);  # Draw the tile
                            asset_manager.draw_tile(surface, (pos_x + self.draw_relative_position[0], pos_y + self.draw_relative_position[1]), self.map_matrix[row_index][column_index][3], self._animation_frame % 4);

                        elif self.map_matrix[row_index][column_index][0] == 1:  # Case: au, animation under.
                            # Draw the two tiles, the animation is the bottom tile.
                            asset_manager.draw_tile(surface, (pos_x + self.draw_relative_position[0], pos_y + self.draw_relative_position[1]), self.map_matrix[row_index][column_index][1], self._animation_frame);  # Draw the tile
                            asset_manager.draw_tile(surface, (pos_x + self.draw_relative_position[0], pos_y + self.draw_relative_position[1]), self.map_matrix[row_index][column_index][2], self.map_matrix[row_index][column_index][3]);

                        elif self.map_matrix[row_index][column_index][0] == 2:  # Case: normal tile.
                            # Draw a single tile.
                            asset_manager.draw_tile(surface, (pos_x + self.draw_relative_position[0], pos_y + self.draw_relative_position[1]), self.map_matrix[row_index][column_index][1], self.map_matrix[row_index][column_index][2]);  # Draw the tile

                        elif self.map_matrix[row_index][column_index][0] == 3:  # Case: two tiles, one over the player.
                            # Draw the bottom tile first.
                            asset_manager.draw_tile(surface, (pos_x + self.draw_relative_position[0], pos_y + self.draw_relative_position[1]), self.map_matrix[row_index][column_index][1], self.map_matrix[row_index][column_index][2]);

                            # Draw the second tile above the player.
                            self.over_tile_queue.append( ((pos_x + self.draw_relative_position[0], pos_y + self.draw_relative_position[1]), self.map_matrix[row_index][column_index][3], self.map_matrix[row_index][column_index][4]) )
                        else:                                                 # Case: two tiles, both under the player.
                            # Draw both tiles under the player, one on top of eachother.
                            asset_manager.draw_tile(surface, (pos_x + self.draw_relative_position[0], pos_y + self.draw_relative_position[1]), self.map_matrix[row_index][column_index][1], self.map_matrix[row_index][column_index][2]);
                            asset_manager.draw_tile(surface, (pos_x + self.draw_relative_position[0], pos_y + self.draw_relative_position[1]), self.map_matrix[row_index][column_index][3], self.map_matrix[row_index][column_index][4]);  # This is almost DEPRECATED

        else:  # Checks the over tile queue.
            # Reset the over tile queue.
            self.over_tile_queue = []

            # Loop thorough the matrix and find / draw all the tiles.
            for row_index in range(len(self.map_matrix)):
                for column_index in range(len(self.map_matrix[row_index])):
                    pos_x = column_index * 64 + self.position[0]
                    pos_y = row_index * 64 + self.position[1]

                    # Only draw the tile if it is inside the screen.
                    if pos_x + self.draw_relative_position[0] >= -64 and pos_x + self.draw_relative_position[0] <= SCREEN_SIZE[0] + 64 and pos_y + self.draw_relative_position[1] >= -64 and pos_y + self.draw_relative_position[1] <= SCREEN_SIZE[1] + 64:
                        if self.map_matrix[row_index][column_index][0] == 3:  # Case: two tiles, one over the player.
                            # Draw the second tile above the player.
                            self.over_tile_queue.append( ((pos_x + self.draw_relative_position[0], pos_y + self.draw_relative_position[1]), self.map_matrix[row_index][column_index][3], self.map_matrix[row_index][column_index][4]) )

            asset_manager._draw(surface, self._img, (self.position[0] + self.draw_relative_position[0], self.position[1] + self.draw_relative_position[1]), (-1, -1, -1, -1))

    # Draw all the tiles that are drawn over the player.
    def over_draw(self, surface):
        for tile in self.over_tile_queue:
            if __builtin__.g_current_scene == LAB:
                asset_manager.draw_tile(surface, (tile[0][0], tile[0][1] + 16), tile[1], tile[2]);
            elif __builtin__.g_current_scene == PLAYER_HOUSE_DOWNSTAIRS:
                asset_manager.draw_tile(surface, (tile[0][0], tile[0][1] + 16), tile[1], tile[2]);
            elif __builtin__.g_current_scene == PLAYER_HOUSE_UPSTAIRS:
                asset_manager.draw_tile(surface, (tile[0][0], tile[0][1] + 16), tile[1], tile[2]);
            else:
                asset_manager.draw_tile(surface, (tile[0][0], tile[0][1]), tile[1], tile[2]);

        garbage_list = []

        # Check if animation is done.
        for animation in self._triggered_animations:
            if animation[3] >= animation[4]:
                garbage_list.append(animation)

        # Remove items that are done.
        for animation in garbage_list:
            self._triggered_animations.remove(animation)  # Remove the item at index.  ( Garbage )

        # Draw items.
        for index in range(len(self._triggered_animations)):
            pos_x = self._triggered_animations[index][0] * 64 + self.position[0]
            pos_y = (self._triggered_animations[index][1]+1) * 64 + self.position[1]

            # Draw the animation.
            asset_manager.draw_tile(surface, (pos_x, pos_y), self._triggered_animations[index][2], self._triggered_animations[index][3]);

    def _update_animation(self, dt):
        self._animation_timer_val += dt

        # If the timer has gone on for 0.2 seconds, change to the next animation frame.
        if self._animation_timer_val >= ANIMATION_SPEED:
            self._animation_timer_val = 0

            # Update frame number
            self._animation_frame += 1
            if self._animation_frame >= 8:
                self._animation_frame = 0

            # Update _triggered_animations.
            for index in range(len(self._triggered_animations)):
                self._triggered_animations[index][3] += 1  # Increment the animation frame

    # Uses delta time (dt).
    def update(self, dt):
        self._update_animation(dt)

    # TODO: make sure x, y are in bounds.
    def get_tile(self, x, y):
        y += 1  # Just... I dunno.  It works.

        if self.map_matrix[y][x][0] == 0:  # Case: ao, animation over.
            return( (self.map_matrix[y][x][1], self.map_matrix[y][x][2]) );  #return the tile.

        elif self.map_matrix[y][x][0] == 1:  # Case: au, animation under.
            return( (self.map_matrix[y][x][2], self.map_matrix[y][x][3]) );  #return the tile.

        elif self.map_matrix[y][x][0] == 2:  # Case: normal tile.
            return( (self.map_matrix[y][x][1], self.map_matrix[y][x][2]) );  #return the tile.

        elif self.map_matrix[y][x][0] == 3:  # Case: two tiles, one over the player.
            return( (self.map_matrix[y][x][1], self.map_matrix[y][x][2]) );  #return the bottomtile.
        else:                                 # Case: two tiles, both under the player.
            return( (self.map_matrix[y][x][3], self.map_matrix[y][x][4]) );  #return the toptile.

    def check_interaction_at_tile(self, x, y):
        #tile = self.get_tile(x, y)

        print (x, y)
        if __builtin__.g_current_scene == OUTSIDE:
            if x == 10 and y == 13:  # The sign's text.
                desc_manager.add_message_to_queue("Pokemon can be found in tall", "grass.")
                desc_manager.add_message_to_queue("TRAINER TIPS", "")
            elif x == 14 and y == 10:  # The town sign's text.
                desc_manager.add_message_to_queue("PALLET TOWN", "We have a lake.")
            elif x == 21 and y == 15:  # The lab sign's text.
                desc_manager.add_message_to_queue("OAK POKeMON RESEARCH LAB", "")
            elif x == 21 and y == 12:  # Going into the lab.
                __builtin__.g_current_scene = LAB
                __builtin__.g_player.set_pos( (64 * 7, 64 * 13) )
            elif x == 11 and y == 6:  # Other house
                desc_manager.add_message_to_queue("The door is locked.  You guess", "it will never be opened.")
            elif x == 9 and y == 6:  # Other house
                desc_manager.add_message_to_queue("RIVAL's house", "")
            elif x == 18 and y == 6:  # Other house
                desc_manager.add_message_to_queue("PLAYER's house", "")
            elif x == 20 and y == 6:  # Going into the player's house.
                __builtin__.g_current_scene = PLAYER_HOUSE_DOWNSTAIRS
                __builtin__.g_player.set_pos( (64 * 4, 64 * 9) )

        elif __builtin__.g_current_scene == LAB:
            if x == 8 and y == 1:  # Prof's Certification
                desc_manager.add_message_to_queue("It looks like someone wrote.", "on it with crayons.")
                desc_manager.add_message_to_queue("This is one of Professor", "Oak's certificates.")
            elif x == 7 and y == 1:  # Prof's Certification
                desc_manager.add_message_to_queue("This certificate looks", "like it's real.")
            elif x == 10 and y == 1:  # BOOKCASE
                desc_manager.add_message_to_queue("It's crammed full of POKeMON", "books.")
            elif x == 11 and y == 1:  # BOOKCASE
                desc_manager.add_message_to_queue("It's crammed full of POKeMON", "books.")
            elif x == 12 and y == 1:  # BOOKCASE
                desc_manager.add_message_to_queue("It's crammed full of POKeMON", "books.")
            elif x == 13 and y == 1:  # BOOKCASE
                desc_manager.add_message_to_queue("It's crammed full of POKeMON", "books.")
            elif x == 5 and y == 8:  # BOOKCASE
                desc_manager.add_message_to_queue("It's crammed full of POKeMON", "books.")
            elif x == 4 and y == 8:  # BOOKCASE
                desc_manager.add_message_to_queue("It's crammed full of POKeMON", "books.")
            elif x == 3 and y == 8:  # BOOKCASE
                desc_manager.add_message_to_queue("It's crammed full of POKeMON", "books.")
            elif x == 2 and y == 8:  # BOOKCASE
                desc_manager.add_message_to_queue("It's crammed full of POKeMON", "books.")
            elif x == 1 and y == 8:  # BOOKCASE
                desc_manager.add_message_to_queue("It's crammed full of POKeMON", "books.")
            elif x == 9 and y == 8:  # BOOKCASE
                desc_manager.add_message_to_queue("It's crammed full of POKeMON", "books.")
            elif x == 10 and y == 8:  # BOOKCASE
                desc_manager.add_message_to_queue("It's crammed full of POKeMON", "books.")
            elif x == 11 and y == 8:  # BOOKCASE
                desc_manager.add_message_to_queue("It's crammed full of POKeMON", "books.")
            elif x == 12 and y == 8:  # BOOKCASE
                desc_manager.add_message_to_queue("It's crammed full of POKeMON", "books.")
            elif x == 13 and y == 8:  # BOOKCASE
                desc_manager.add_message_to_queue("It's crammed full of POKeMON", "books.")
            elif x == 9 and y == 0:  # Window
                desc_manager.add_message_to_queue("You get a new pokemon!", "")
                desc_manager.add_message_to_queue("You spot a pokemon out the ", "window.  Score!")
            elif x == 4 and y == 1:  # COMPUTER
                desc_manager.add_message_to_queue("The computer doesn't turn on.", "You wonder why...")
            elif x == 3 and y == 1:  # COMPUTER
                desc_manager.add_message_to_queue("The screen doesn't turn on.", "You wonder why...")
            elif x == 1 and y == 12:  # DOPE_PLANT_THAT_RAPS
				desc_manager.add_message_to_queue("...", "")
				desc_manager.add_message_to_queue("YO HOMES TO BEL-AIR!", "")
				desc_manager.add_message_to_queue("was rare, but I", "thought nah forget it")
			 	desc_manager.add_message_to_queue("If anything I could", "say that this cab")
				desc_manager.add_message_to_queue("it had dice in the", "mirror!")
			 	desc_manager.add_message_to_queue("near the license plate", "said FRESH and")
				desc_manager.add_message_to_queue("I whisteled for a cab", "and when it came")
				desc_manager.add_message_to_queue("auntie and uncle in", "Bel-air")
				desc_manager.add_message_to_queue("she said you're", "movin' in with your")
				desc_manager.add_message_to_queue("little fight and my", "mom got scared")
				desc_manager.add_message_to_queue("my neighbourhood,", "I got in one")
				desc_manager.add_message_to_queue("to no good, started", "making trouble in")
				desc_manager.add_message_to_queue("when a couple of guys", "they were up")
				desc_manager.add_message_to_queue("some b-ball outside", "of the school")
				desc_manager.add_message_to_queue("relaxin' all cool", "and all shooting")
				desc_manager.add_message_to_queue("Most of my days.", "Chillin' out maxin'")
				desc_manager.add_message_to_queue("on the playground was", "where I spent")
				desc_manager.add_message_to_queue("In west Philidelphia", "born and raised")
				desc_manager.add_message_to_queue("the prince of a small", "town called Bel-air.")
				desc_manager.add_message_to_queue("right there. I'll tell", "you how i became")
				desc_manager.add_message_to_queue("and I'd like to take", "a minute just sit")
				desc_manager.add_message_to_queue("my life got flipped-", "turned upside down")
				desc_manager.add_message_to_queue("Now this is a story", "all about how")
            elif x == 7 and y == 13:  # Going out of the lab
                __builtin__.g_current_scene = OUTSIDE
                __builtin__.g_player.set_pos( (64 * 21, 64 * 13 - 16) )

        elif __builtin__.g_current_scene == PLAYER_HOUSE_DOWNSTAIRS:
            if x == 6 and y == 1:  # TV
                desc_manager.add_message_to_queue("...I better go, too.", "")
                desc_manager.add_message_to_queue("railroad tracks.", "")
                desc_manager.add_message_to_queue("There is a movie on TV.", "Two boys are walking on-")
            elif x == 4 and y == 1:  # CABINET
                desc_manager.add_message_to_queue("Dishes and plates are neatly", "lined up.")
            elif x == 3 and y == 1:  # CABINET
                desc_manager.add_message_to_queue("Dishes and plates are neatly", "lined up.")
            elif x == 2 and y == 1:  # FOODAREA
                desc_manager.add_message_to_queue("It smells delicious!", "Someone has been cooking here.")
            elif x == 1 and y == 1:  # SINK
                desc_manager.add_message_to_queue("Don't feel like doing", "the dishes right now.")
            elif x == 11 and y == 2:  # Stairs
                __builtin__.g_current_scene = PLAYER_HOUSE_UPSTAIRS
                __builtin__.g_player.set_pos( (64 * 9, 64 * 2) )
            elif x == 4 and y == 9:  # Going out of the house
                __builtin__.g_current_scene = OUTSIDE
                __builtin__.g_player.set_pos( (64 * 20, 64 * 7 - 16) )

        elif __builtin__.g_current_scene == PLAYER_HOUSE_UPSTAIRS:
            if x == 3 and y == 1:  # dresser
                desc_manager.add_message_to_queue("It's a nicely made dresser.", "It will hold a lot of stuff.")
            elif x == 4 and y == 1:  # bookshelf
                desc_manager.add_message_to_queue("It's crammed full of POKeMON", "books.")
            elif x == 5 and y == 1:  # bookshelf
                desc_manager.add_message_to_queue("It's crammed full of POKeMON", "books.")
            elif x == 2 and y == 1:  # desk
                desc_manager.add_message_to_queue("It's a wooden desk...", "")
            elif x == 1 and y == 1:  # computer
                desc_manager.add_message_to_queue("This computer is running", "windows vista.  Yikes!")
            elif x == 9 and y == 2:  # Stairs
                __builtin__.g_current_scene = PLAYER_HOUSE_DOWNSTAIRS
                __builtin__.g_player.set_pos( (64 * 11, 64 * 2) )
            elif x == 11 and y == 1:  # sign thing
                desc_manager.add_message_to_queue("people.", "             T - T")
                desc_manager.add_message_to_queue("This game was made with", "lots of stress by three-")
            elif x == 6 and y == 5:  # computer
                desc_manager.add_message_to_queue("You play with the nes.", "Okay!  It's time to go!")
