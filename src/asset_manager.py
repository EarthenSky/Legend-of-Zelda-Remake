'''This script helps manage the assets like tiles and stuff.'''

import pygame

# Pseudo Enum constants.  Each constant refers to a different image group to draw from.
LIGHT_GRASS = 0
TREE = 1
CROWDED_TREE = 2
FENCE = 3
LEDGE = 4
DARK_GRASS = 5
SPECIAL = 6  # (0:bright tall grass, 1:metal sign, 2:bright wood sign)
#TODO: add -> HOUSE = 7
#TODO: add -> LAB = 7

# Asset manager initialization
outside_tiles = pygame.image.load("resc/images/outside_tiles.png").convert()

#TODO: add the tiles to these.
# animated_tiles = pygame.image.load("resc/images/animated_tiles.png").convert()
# forest_tiles = pygame.image.load("resc/images/forest_tiles.png").convert()

# Blits the image to the surface.
def _draw(surface, img, position, cut_rect):
    img = img.subsurface(cut_rect)  # Crop the img.
    img = pygame.transform.scale(img, (64, 64))  # 4x scale the img.
    surface.blit(img, position)  # Draw the img.

# 'group' is one of the constants and means the row.  'index' is how far down the row you go.
def draw_tile(surface, position, group, index):
    # TODO: camera stuff here?

    # Passes the cut position for the image to the draw function.
    if group == LIGHT_GRASS:
        _draw( surface, outside_tiles, position, (index * 16, group * 16, 16, 16) )
    elif group == TREE:
        _draw( surface, outside_tiles, position, (index * 16, group * 16, 16, 16) )

# TODO: draw the different pokemon angles.
def draw_pokemon():
    pass
