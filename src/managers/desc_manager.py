# This is the queue for any messages that need to be sent to the player.
text_queue = []

# This function adds a message to the queue.
# A message contains a top string and a bottom string. (top, bottom) are placed in a tuple like so.
def add_message_to_queue(top_text, bottom_text):
    text_queue.append( (top_text, bottom_text) )
