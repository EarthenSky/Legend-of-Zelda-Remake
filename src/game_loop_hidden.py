'''This file contains the background stuff that runs the main gameloop.'''

import pygame
import game_loop  # Import the main gameloop to call its functions.
import __builtin__  # NOOOOOooOOoOoO.

# This is the gameloop section of code.
def _gameloop():
    # Constants.
    FPS = 120

    # Globals.
    delta_time = 0
    game_stopped = False

    # Create the object that handles framerate regulation and delta_time.
    framerate_clock = pygame.time.Clock()
    g_delta_time = framerate_clock.tick(FPS) / 1000.0

    everysecond_val = 0

    # This is the start of the gameloop.
    while not game_stopped:
        game_loop.handle_input()  # First Gameloop Stage.

        game_loop.update(delta_time)  # Second Gameloop Stage.

        game_loop.draw()  # Last Gameloop Stage.

        game_stopped = game_loop.is_exit()  # Checks if the game needs to be stopped.

        pygame.display.update() # Updates the display with changes.

        # Pause pygame and calculate delta time.
        delta_time = framerate_clock.tick(FPS) / 1000.0

        everysecond_val += delta_time

        # Prints the delta_time value.  Only for debug.
        if everysecond_val > 1:
            everysecond_val = 0
            print "DEBUG: delta_time = " + str(delta_time) + ", fps -> " + str( framerate_clock.get_fps() )

    # Close pygame before application closes.
    pygame.quit()

    print "DEBUG: Application Complete."

# This function is used to start the main seciton of the game.
def start_gameloop(player_name, rival_name):
    __builtin__.player_name = player_name
    __builtin__.rival_name = rival_name
    _gameloop()
