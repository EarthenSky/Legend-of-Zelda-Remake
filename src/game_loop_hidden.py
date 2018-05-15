'''This file contains the background stuff that runs the main gameloop.'''

import pygame
import game_loop  # Import the main gameloop to call its functions.

# This is the gameloop section of code.
def gameloop():
    # Constants.
    FPS = 120

    # Globals.
    delta_time = 0
    game_stopped = False

    # Create the object that handles framerate regulation and delta_time.
    framerate_clock = pygame.time.Clock()
    g_delta_time = framerate_clock.tick(FPS) / 1000.0

    # This is the start of the gameloop.
    while not game_stopped:
        game_loop.handle_input()  # First Gameloop Stage.

        game_loop.update(delta_time)  # Second Gameloop Stage.

        game_loop.draw()  # Last Gameloop Stage.

        game_stopped = game_loop.is_exit()  # Checks if the game needs to be stopped.

        pygame.display.update() # Updates the display with changes.

        # Pause pygame and calculate delta time.
        delta_time = framerate_clock.tick(FPS) / 1000.0

        # Prints the delta_time value.  Only for debug.
        if framerate_clock.get_fps() < 100:
            print "DEBUG: delta_time = " + str(delta_time) + ", fps -> " + str( framerate_clock.get_fps() )

    # Close pygame before application closes.
    pygame.quit()

    print "DEBUG: Application Complete."

# This function is used to start the main seciton of the game.
def start_gameloop():
    gameloop()
