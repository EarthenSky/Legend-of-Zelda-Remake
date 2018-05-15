'''This script helps manage the assets like tiles and stuff.'''

import pygame

# Pseudo Enum constants.  Each constant refers to a different image group to draw from.
LIGHT_GRASS = 0
TREE = 1
CROWDED_TREE = 2
FENCE = 3
LEDGE = 4
DARK_GRASS = 5
SPECIAL = 6  # (0:bright tall grass, 1:metal sign, 2:bright wood sign, 3-4:mailbox)
DIRT = 7
HOUSE = 8
LAB = 9

# Asset manager initialization
outside_tiles = pygame.image.load("resc/images/outside_tiles.png").convert_alpha()

#TODO: add the tiles to these.
# animated_tiles = pygame.image.load("resc/images/animated_tiles.png").convert()
# forest_tiles = pygame.image.load("resc/images/forest_tiles.png").convert()

# Initialize the player sprite sheet.
male_char_spritesheet = pygame.image.load("resc/images/male_char_spritesheet.png").convert_alpha()

# Blits the image to the surface.
def _draw(surface, img, position, cut_rect):
    # Rounds the position to every 4 pixels.
    position = (round(position[0] / 4) * 4, round(position[1] / 4) * 4)

    img = img.subsurface(cut_rect)  # Crop the img.
    img = pygame.transform.scale(img, (img.get_width() * 4, img.get_height() * 4))  # 4x scale the img.
    surface.blit(img, position)  # Draw the img.

# 'group' is one of the constants and means the row.  'depth' is how far down the row you go.
def draw_tile(surface, position, group, depth):
    # TODO: camera stuff here?

    # Make group and index integers.
    group = int(group)
    depth = int(depth)

    # Passes the cut position for the image to the draw function.
    if group >= 0 and group <= LAB:
        _draw( surface, outside_tiles, position, (depth * 16, group * 16, 16, 16) )
    else:
        print "ERR 8: INCORRECT GROUP NAME PASSED in asset_manager.py"

def draw_player(surface, position, group, depth, is_male):
    if is_male:
        _draw( surface, male_char_spritesheet, position, (depth * 16, group * 20, 16, 20) )
    else:
        pass

# TODO: draw the different pokemon angles.
def draw_pokemon():
    pass
