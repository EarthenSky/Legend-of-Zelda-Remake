'''TODO: rename to queue manager.'''

import sys

# The asset manager helps render images.
sys.path.insert(0, 'src/managers/')  # This line tells the importer where to look for the module.
import asset_manager

import pygame

import __builtin__  # PLEASE NOOO!!!!!

# This is the queue for any messages that need to be sent to the player.
text_queue = []

# This function adds a message to the queue.
# A message contains a top string and a bottom string. (top, bottom) are placed in a tuple like so.
def add_message_to_queue(top_text, bottom_text):
    global text_queue

    text_queue.append( (top_text, bottom_text) )

def check_queue(screen):
    global text_queue

    # Go through all items in the queue if there are any.
    for item in text_queue:
        loop_item(screen)
        text_queue = text_queue[:-1]  # Remove the last item by slicing.

# This function check if the z key (A button) is pressed.
def check_skip_box():
    for event in pygame.event.get():  # TODO: THIS BUG WITH THE PLAYER?
        # Do the player events separately incase the z button is pressed.


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                return True
        elif event.type == pygame.QUIT:
            # Close pygame before application closes.
            pygame.quit()
            print "DEBUG: Application Complete."
            sys.exit(0)
            
        elif g_player.handle_input(event):
            pass

    return False

# This loop runs at 60 fps because there is not much happening.
def loop_item(screen):
    # Draw the text box first.
    asset_manager.draw_message(screen, text_queue[len(text_queue)-1][0], text_queue[len(text_queue)-1][1])
    pygame.display.update()  # Updates the display with any changes.

    # Create the object that handles framerate regulation and delta_time.
    framerate_clock = pygame.time.Clock()
    delta_time = framerate_clock.tick(60) / 1000.0
    everysecond_val = 0

    # Continuously check for the z key (A button) being pressed.
    start_exit = False
    exit_wait_val = 0

    keep_looping = True
    while keep_looping:
        if check_skip_box() == True:
            start_exit = True

        # This is the timer that pauses before starting the next popup.
        if start_exit == True:
            if exit_wait_val > 0.05:
                keep_looping = False
            else:
                exit_wait_val += delta_time

        # Pause pygame and calculate delta time.
        delta_time = framerate_clock.tick(60) / 1000.0

        everysecond_val += delta_time

        # Tells person they are in a message
        if everysecond_val > 1:
            everysecond_val = 0
            print "In a MESSAGE!"
