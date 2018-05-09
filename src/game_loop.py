'''This file contains the main gameloop, which controls sequential
scenes (environment scenes), usually just called different scenes.'''

import sys
import pygame

# Different Scene Constants.
PLAYER_HOUSE_UPSTAIRS = 0
PLAYER_HOUSE_DOWNSTAIRS = 1
OUTSIDE = 2
# TODO: add more scenes.

# Constants.
SCREEN_SIZE = [240 * 4, 160 * 4]

# Starts and sets up pygame.
pygame.init()
DISPLAY_SURFACE = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Pokemon Wave Blue")

# Must be imported after pygame has been initialized.
sys.path.insert(0, 'src/objects/')  # This line tells the importer where to look for the module.
import tilemap

# Globals.
g_game_stopped = False
g_current_scene = OUTSIDE

# Create the different scenes.
g_outside_tilemap = tilemap.Tilemap("outside.map", 0)

# This function handles any input.  Called before update.
def handle_input():
    global g_game_stopped

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            g_game_stopped = True

# This is for drawing stuff.  Called before update.
def draw():
    if g_current_scene == PLAYER_HOUSE_UPSTAIRS:
        pass
    elif g_current_scene == PLAYER_HOUSE_DOWNSTAIRS:
        pass
    elif g_current_scene == OUTSIDE:
        g_outside_tilemap.draw(DISPLAY_SURFACE)
    else:
        print "GAME IS NOT IN ANY SCENE."

    # Draw the sixth item of the TREE group.
    #asset_manager.draw_tile(DISPLAY_SURFACE, (128, 64), asset_manager.TREE, 3);

# This is the "do game math" function.  Put any math or functional code here.
def update(dt):
    if g_current_scene == PLAYER_HOUSE_UPSTAIRS:
        pass
    elif g_current_scene == PLAYER_HOUSE_DOWNSTAIRS:
        pass
    elif g_current_scene == OUTSIDE:
        #g_outside_tilemap.update()
        pass
    else:
        print "GAME IS NOT IN ANY SCENE."

    #print "last frame elapsed {}s".format(dt)

# This function returns if the game is completed or not.  Return true if game is done.
def is_exit():
    return g_game_stopped
