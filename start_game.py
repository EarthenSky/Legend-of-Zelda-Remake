'''In this file the user will be able to set if the game is full screen or not,
assign which keys do what (maybe even use a controller?), and is given a small tip
about moving the story along (try to leave the town if you havn't played any pokemon games before.)
before being sent into the main intro loop.'''

import sys

sys.path.insert(0, 'src/')  # This line tells the importer where to look for modules.
import game_loop_hidden  # Import the hidden main gameloop class.

#TODO: insert settings and name stuff here.

# Start the game.
game_loop_hidden.start_gameloop()
