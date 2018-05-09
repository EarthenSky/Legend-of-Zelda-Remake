'''This file contains the main gameloop, which controls sequential
scenes (environment scenes), usually just called different scenes.'''

import pygame

# Constants.
SCREEN_SIZE = [240 * 4, 160 * 4]

# Starts and sets up pygame.
pygame.init()
DISPLAY_SURFACE = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Pokemon Wave Blue")

# The asset manager helps render images.  Must be imported after pygame has been initialized.
import asset_manager

# Globals.
g_game_stopped = False

# This function handles any input.  Called before update.
def handle_input():
    global g_game_stopped

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            g_game_stopped = True

# This is for drawing stuff.  Called before update.
def draw():
    # Draw the sixth item of the TREE group.
    asset_manager.draw_tile(DISPLAY_SURFACE, (128, 64), asset_manager.TREE, 3);

    asset_manager.draw_tile(DISPLAY_SURFACE, (64, 64), asset_manager.TREE, 2);

    asset_manager.draw_tile(DISPLAY_SURFACE, (128, 0), asset_manager.TREE, 1);
    asset_manager.draw_tile(DISPLAY_SURFACE, (64, 0), asset_manager.TREE, 0);

    asset_manager.draw_tile(DISPLAY_SURFACE, (128, 128), asset_manager.TREE, 5);
    asset_manager.draw_tile(DISPLAY_SURFACE, (64, 128), asset_manager.TREE, 4);

    asset_manager.draw_tile(DISPLAY_SURFACE, (128 + 64, 128), asset_manager.LIGHT_GRASS, 5);

# This is the "do game math" function.  Put any math or functional code here.
def update(dt):
    print "last frame elapsed {}s".format(dt)

# This function returns if the game is completed or not.  Return true if game is done.
def is_exit():
    return g_game_stopped
