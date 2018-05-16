'''This class handles the drawing and checking for interaction or collision.
The player class interacts with this class.'''

import sys

# Constants.
SCREEN_SIZE = [240 * 4, 160 * 4]

# The asset manager helps render images.
sys.path.insert(0, 'src/managers/')  # This line tells the importer where to look for the module.
import asset_manager

class Tilemap:
    def __init__(self, map_file_name, img=0):
        self.map_matrix = []  # Init the matrix

        self.position = [0, 0]  # The world position of the map.

        # Create the string matrix from the map's text.
        with open("resc/maps/{}".format(map_file_name), 'r') as map_file:
            # Loop through each line.
            for line in map_file:
                row_list = ' '.join(line.split()).split(" ")  # Obtain each item and make it a list..replace('\n', '')
                self.map_matrix.append(row_list)

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

                    # Only draw the tile if it is in the screen.
                    if pos_x >= -64 and pos_x <= SCREEN_SIZE[0] + 64 and pos_y >= -64 and pos_y <= SCREEN_SIZE[1] + 64:
                        # Look for two tiles. t means a second tile on top of eachother.
                        if self.map_matrix[row_index][column_index].find('t') == -1:  # -1 means cannot find.
                            # Get the two variables from the string.
                            group, depth = self.map_matrix[row_index][column_index].replace(' ', '').split(',')
                            asset_manager.draw_tile(surface, (pos_x, pos_y), group, depth);  # Draw the tile

                        elif self.map_matrix[row_index][column_index].find('ao') != -1:  # Case: found an 'a'.  the o stands for 'over' as in the top image is an animation.
                            # Get the 4 variables from the string.
                            group, depth, group2 = self.map_matrix[row_index][column_index].replace(' ', '').replace('ao', ',').split(',')
                            asset_manager.draw_tile(surface, (pos_x, pos_y), group, depth);  # Draw the tile

                            # Draw the second tile above the player.
                            self.over_tile_queue.append( ((pos_x, pos_y), group2, _animation_frame) )

                        elif self.map_matrix[row_index][column_index].find('au') != -1:  # Case: found an 'a'.  the u stands for 'under' as in the bottom image is an animation.
                            # Get the 4 variables from the string.
                            depth, group2, depth2 = self.map_matrix[row_index][column_index].replace(' ', '').replace('au', ',').split(',')
                            asset_manager.draw_tile(surface, (pos_x, pos_y), group, _animation_frame);  # Draw the tile

                            # Draw the second tile above the player.
                            self.over_tile_queue.append( ((pos_x, pos_y), group2, depth2) )

                        else:
                            if self.map_matrix[row_index][column_index].find('b') == -1:  # -1 means cannot find.
                                # Get the 4 variables from the string.
                                group, depth, group2, depth2 = self.map_matrix[row_index][column_index].replace(' ', '').replace('t', ',').split(',')
                                asset_manager.draw_tile(surface, (pos_x, pos_y), group, depth);

                                # Draw the second tile above the player.
                                self.over_tile_queue.append( ((pos_x, pos_y), group2, depth2) )
                            else:
                                # Get the 4 variables from the string.
                                group, depth, group2, depth2 = self.map_matrix[row_index][column_index].replace(' ', '').replace('tb', ',').split(',')

                                # Draw both tiles under the player.
                                asset_manager.draw_tile(surface, (pos_x, pos_y), group, depth);
                                asset_manager.draw_tile(surface, (pos_x, pos_y), group2, depth2);

        else:
            pass
            # TODO: just blit this image.

    # Draw all the tiles that are drawn over the player.
    def over_draw(self, surface):
        for tile in self.over_tile_queue:
            asset_manager.draw_tile(surface, tile[0], tile[1], tile[2]);

    # Uses delta time (dt).
    def update(self, dt):
        pass #TODO: animate some tiles.
