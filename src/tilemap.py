'''This class handles the drawing and checking for interaction or collision.
The player class interacts with this class.'''

class Tilemap:

    def __init__(self, map_file_name, img=0):
        # TODO: Auto find the folder with maps in it.
        self.map_matrix = []  #TODO: create a matrix from the map's text

        # Is this object drawing from a batch of images or one large one?
        self.is_batch_image = False

        if img == 0:
            self.is_batch_image = True  # TODO: do nothing because no image was passed..
        else:
            self.is_batch_image = False

    def draw(self, surface):
        if is_batch_image
            # TODO: for loop and draw the current animation pane.
        else:
            # TODO: just blit this image.

    # Uses delta time (dt).
    def update(self, dt):
        pass #TODO: animate some tiles.
