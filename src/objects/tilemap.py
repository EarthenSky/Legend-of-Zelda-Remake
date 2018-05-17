'''This class handles the drawing and checking for interaction or collision.
The player class interacts with this class.'''

import sys

# Constants.
SCREEN_SIZE = [240 * 4, 160 * 4]

ANIMATION_SPEED = 0.138*1.7  # 1.7 times more than 0.138s or 138ms per frame.

# The asset manager helps render images.
sys.path.insert(0, 'src/managers/')  # This line tells the importer where to look for the module.
import asset_manager

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

    def __init__(self, map_file_name, img=0):
        self.position = [0, 0]  # The world position of the map.

        self.map_matrix = []  # Init the matrix.
        self._create_map(map_file_name, self.map_matrix)  # Fill the matrix.

        # Is this object drawing from a batch of images or one large one?
        self.image_passed = False

        # Check if image was passed.
        if img == 0:
            self.image_passed = False
        else:
            self.image_passed = True

        # The list that holds all the draw functions for the items drawn after the player.
        self.over_tile_queue = []

        # The animation frame that the tilemap is on. (affects all the sprites at the same time.)
        # Note: this variable goes to 8 frames cause some animations are 8 frames long.
        self._animation_frame = 0
        self._animation_timer_val = 0

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
                    if pos_x >= -64 and pos_x <= SCREEN_SIZE[0] + 64 and pos_y >= -64 and pos_y <= SCREEN_SIZE[1] + 64:
                        # Choose hjow to draw this tile.
                        if self.map_matrix[row_index][column_index][0] == 0:  # Case: ao, animation over.
                            # Draw the two tiles, the animation is the top tile.
                            asset_manager.draw_tile(surface, (pos_x, pos_y), self.map_matrix[row_index][column_index][1], self.map_matrix[row_index][column_index][2]);  # Draw the tile
                            asset_manager.draw_tile(surface, (pos_x, pos_y), self.map_matrix[row_index][column_index][3], self._animation_frame % 4);

                        elif self.map_matrix[row_index][column_index][0] == 1:  # Case: au, animation under.
                            # Draw the two tiles, the animation is the bottom tile.
                            asset_manager.draw_tile(surface, (pos_x, pos_y), self.map_matrix[row_index][column_index][1], self._animation_frame);  # Draw the tile
                            asset_manager.draw_tile(surface, (pos_x, pos_y), self.map_matrix[row_index][column_index][2], self.map_matrix[row_index][column_index][3]);

                        elif self.map_matrix[row_index][column_index][0] == 2:  # Case: normal tile.
                            # Draw a single tile.
                            asset_manager.draw_tile(surface, (pos_x, pos_y), self.map_matrix[row_index][column_index][1], self.map_matrix[row_index][column_index][2]);  # Draw the tile

                        elif self.map_matrix[row_index][column_index][0] == 3:  # Case: two tiles, one over the player.
                            # Draw the bottom tile first.
                            asset_manager.draw_tile(surface, (pos_x, pos_y), self.map_matrix[row_index][column_index][1], self.map_matrix[row_index][column_index][2]);

                            # Draw the second tile above the player.
                            self.over_tile_queue.append( ((pos_x, pos_y), self.map_matrix[row_index][column_index][3], self.map_matrix[row_index][column_index][4]) )
                        else:                                                 # Case: two tiles, both under the player.
                            # Draw both tiles under the player, one on top of eachother.
                            asset_manager.draw_tile(surface, (pos_x, pos_y), self.map_matrix[row_index][column_index][1], self.map_matrix[row_index][column_index][2]);
                            asset_manager.draw_tile(surface, (pos_x, pos_y), self.map_matrix[row_index][column_index][3], self.map_matrix[row_index][column_index][4]);

        else:
            pass
            # TODO: just blit this image.

    # Draw all the tiles that are drawn over the player.
    def over_draw(self, surface):
        for tile in self.over_tile_queue:
            asset_manager.draw_tile(surface, tile[0], tile[1], tile[2]);

    def _update_animation(self, dt):
        self._animation_timer_val += dt

        # If the timer has gone on for 0.2 seconds, change to the next animation frame.
        if self._animation_timer_val >= ANIMATION_SPEED:
            self._animation_timer_val = 0

            # Update frame number
            self._animation_frame += 1
            if self._animation_frame >= 8:
                self._animation_frame = 0

    # Uses delta time (dt).
    def update(self, dt):
        self._update_animation(dt)

    def get_tile(self, x, y):
        if self.map_matrix[x][y][0] == 0:  # Case: ao, animation over.
            return( (self.map_matrix[x][y][1], self.map_matrix[x][y][2]) );  #return the tile.

        elif self.map_matrix[x][y][0] == 1:  # Case: au, animation under.
            return( (self.map_matrix[x][y][2], self.map_matrix[x][y][3]) );  #return the tile.

        elif self.map_matrix[x][y][0] == 2:  # Case: normal tile.
            return( (self.map_matrix[x][y][1], self.map_matrix[x][y][2]) );  #return the tile.

        elif self.map_matrix[x][y][0] == 3:  # Case: two tiles, one over the player.
            return( (self.map_matrix[x][y][1], self.map_matrix[x][y][2]) );  #return the bottomtile.

        else:                                 # Case: two tiles, both under the player.
            return( (self.map_matrix[x][y][3], self.map_matrix[x][y][4]) );  #return the bottomtile.
