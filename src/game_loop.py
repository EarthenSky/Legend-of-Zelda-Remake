'''This file contains the main gameloop, which controls sequential
scenes (environment scenes), usually just called different scenes.'''

import sys
import pygame

import __builtin__  # TODO: PLEASE NO!!!

# Different Scene Constants.
__builtin__.PLAYER_HOUSE_UPSTAIRS = 0
__builtin__.PLAYER_HOUSE_DOWNSTAIRS = 1
__builtin__.OUTSIDE = 2
__builtin__.LAB = 3
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

# Must be imported after pygame has been initialized.
sys.path.insert(0, 'src/managers/')  # This line tells the importer where to look for the module.
import desc_manager

import player  # The player needs to move.

# Globals.
g_game_stopped = False
__builtin__.g_current_scene = OUTSIDE

# Create the different scenes.
__builtin__.g_outside_tilemap = tilemap.Tilemap("outside.map", 0)
__builtin__.g_lab_tilemap = tilemap.Tilemap( "lab.map", pygame.image.load("resc/images/lab.png").convert() )
__builtin__.g_player_house_down_tilemap = tilemap.Tilemap( "player_house_down.map", pygame.image.load("resc/images/player_house_down.png").convert() )

# Create the player object.
__builtin__.g_player = player.Player( [240*4/2-8*4, 160*4/2-4*4] )

# This function handles any input.  Called before update.
def handle_input():
    global g_game_stopped

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            g_game_stopped = True
        elif g_player.handle_input(event):
            pass

# This is for drawing stuff.  Called before update.
def draw():
    if g_current_scene == PLAYER_HOUSE_UPSTAIRS:
        pass
    elif g_current_scene == PLAYER_HOUSE_DOWNSTAIRS:
        DISPLAY_SURFACE.fill( (0, 0, 0) )
        g_player_house_down_tilemap.draw(DISPLAY_SURFACE)
    elif g_current_scene == OUTSIDE:
        DISPLAY_SURFACE.fill( (0, 0, 0) )
        g_outside_tilemap.draw(DISPLAY_SURFACE)
    elif g_current_scene == LAB:
        DISPLAY_SURFACE.fill( (0, 0, 0) )
        g_lab_tilemap.draw(DISPLAY_SURFACE)
    else:
        print "GAME IS NOT IN ANY SCENE."

    # Draw the player.
    g_player.draw(DISPLAY_SURFACE)

    # Stuff drawn over the player.
    if g_current_scene == PLAYER_HOUSE_UPSTAIRS:
        pass
    elif g_current_scene == PLAYER_HOUSE_DOWNSTAIRS:
        g_player_house_down_tilemap.over_draw(DISPLAY_SURFACE)
    elif g_current_scene == OUTSIDE:
        g_outside_tilemap.over_draw(DISPLAY_SURFACE)
    elif g_current_scene == LAB:
        g_lab_tilemap.over_draw(DISPLAY_SURFACE)

    # Check for any popup boxes.
    desc_manager.check_queue(DISPLAY_SURFACE)

# This is the "do game math" function.  Put any math or functional code here.
def update(dt):
    # Move the player and give the movement value to the other scenes.
    player_offset = g_player.update(dt)

    if g_current_scene == PLAYER_HOUSE_UPSTAIRS:
        pass
    elif g_current_scene == PLAYER_HOUSE_DOWNSTAIRS:
        g_player_house_down_tilemap.update(dt)
        g_player_house_down_tilemap.get_offset(player_offset)
    elif g_current_scene == OUTSIDE:
        # Update the tilemap, then translate it.
        g_outside_tilemap.update(dt)
        g_outside_tilemap.get_offset(player_offset)
    elif g_current_scene == LAB:
        # Update the tilemap, then translate it.
        g_lab_tilemap.update(dt)
        g_lab_tilemap.get_offset(player_offset)
    else:
        print "GAME IS NOT IN ANY SCENE."

# This function returns if the game is completed or not.  Return true if game is done.
def is_exit():
    return g_game_stopped
