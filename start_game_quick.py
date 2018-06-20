'''In this file the user will be able to set if the game is full screen or not,
assign which keys do what (maybe even use a controller?), and might be given a small tip
about moving the story along (try to leave the town if you havn't played any pokemon games before.)
before being sent into the main intro loop.'''

import sys

# This line tells the importer where to look for the following modules.
sys.path.insert(0, 'src/')

# Import the hidden main gameloop class.
# This calls the main functions in the gameloop, like update() or check_input().
import game_loop_hidden

#TODO: insert settings and name stuff here.

# Start the game.
game_loop_hidden.start_gameloop("PLAYER", "RIVAL")
