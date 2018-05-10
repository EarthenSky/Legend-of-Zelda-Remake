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
                row_list = line.replace('\n', '').split(" ")  # Obtain each item and make it a list.
                self.map_matrix.append(row_list)
                #print row_list

        #print str(self.map_matrix)

        # Is this object drawing from a batch of images or one large one?
        self.image_passed = False

        # Check if image was passed.
        if img == 0:
            self.image_passed = False
        else:
            self.image_passed = True

    def draw(self, surface):
        if not self.image_passed:
            # Loop thorough the matrix and find / draw all the tiles.
            for row_index in range(len(self.map_matrix)):
                for column_index in range(len(self.map_matrix[row_index])):
                    pos_x = column_index * 64 + self.position[0]
                    pos_y = row_index * 64 + self.position[1]

                    # Only draw the tile if it is in the screen.
                    if pos_x >= 0 and pos_x <= SCREEN_SIZE[0] and pos_y >= 0 and pos_y <= SCREEN_SIZE[1]:
                        asset_manager.draw_tile(surface, (pos_x, pos_y), self.map_matrix[row_index][column_index][0], self.map_matrix[row_index][column_index][1]);

        else:
            pass
            # TODO: just blit this image.

    # Uses delta time (dt).
    def update(self, dt):
        pass #TODO: animate some tiles.
