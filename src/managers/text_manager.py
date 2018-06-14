'''This script manages printing text to the screen'''

import pygame

LARGEST_CHAR_VALUE = 67  # The value to count up to when loading images.  Aka the size of the img list.

# This is a list of all the image files for each character.
img_list = []
img_list_small = []

### Order of image files in the list:
### space, uppercase_letters, lowercase_letters, period, comma, colon, exclamation mark, numbers, extras.

# This function loads all the images and puts them into img_list.
def init():
    for file_name in range(0, LARGEST_CHAR_VALUE + 1):
        img_list.append( pygame.image.load("resc/images/characters/" + str(file_name) + ".png") )

    for file_name in range(0, LARGEST_CHAR_VALUE + 1):
        img_list_small.append( pygame.image.load("resc/images/characters_small/" + str(file_name) + ".png") )

# This function converts the string into a format that can be printed out.
def _convert_string(in_str):
    # The string to output.
    out_str = ""

    # Loop through all the characters in the string and convert them.
    for index in range(len(in_str)):
        char_ord = ord( in_str[index] )  # The integer representation of the current char.

        if char_ord <= 90 and char_ord >= 65:  # Case: char is uppercase.
            out_str += chr(char_ord-64)
        elif char_ord <= 124 and char_ord >= 95:  # Case: char is lowercase.
            out_str += chr(char_ord-70)
        elif char_ord == 32:  # Case: char is a space.
            out_str += chr(0)
        elif char_ord == ord("."):  # Case: char is a period.
            out_str += chr(53)
        elif char_ord == ord(","):  # Case: char is a comma.
            out_str += chr(54)
        elif char_ord == ord(":"):  # Case: char is a colon.
            out_str += chr(55)
        elif char_ord == ord("!"):  # Case: char is a exclamation mark.
            out_str += chr(56)
        elif char_ord >= 48 and char_ord <= 57:
            out_str += chr(char_ord + 9)
        elif char_ord == ord("-"):  # Case: char is a exclamation mark.
            out_str += chr(67)

    # Output the converted string.
    return out_str

# This function draws text to a certain x,y position.
def draw_text(screen, text, pos):
    text = _convert_string(text)  # Convert the text to a string that can be read by this function.

    # Loop through all the characters in the string and draws them onto the screen.
    for index in range(len(text)):

        # Loads the needed char from the list.
        char_img = img_list[ ord( text[index] ) ]

        # Gets non scaled dimensions of the letter.
        width, height = char_img.get_rect().size

        # Scales the image before drawing it.
        char_img = pygame.transform.scale(char_img, (width * 4, height * 4))

        # This is can just be a monospaced font. (each char is the same size.) (+1 for space between chars.)
        width = 6+1

        # Blits the char to the screen.
        screen.blit( char_img, (pos[0] + index * (width * 4), pos[1]) )

# This function draws text to a certain x,y position.
def draw_text_small(screen, text, pos):
    text = _convert_string(text)  # Convert the text to a string that can be read by this function.

    # Loop through all the characters in the string and draws them onto the screen.
    for index in range(len(text)):
        # Loads the needed char from the list.
        char_img = img_list_small[ ord( text[index] ) ]

        # Gets non scaled dimensions of the letter.
        width, height = char_img.get_rect().size

        # Scales the image before drawing it.
        char_img = pygame.transform.scale(char_img, (width * 4, height * 4))

        # This is can just be a monospaced font. (each char is the same size.) (+1 for space between chars.)
        width = 5+1  # (5 size instead of 6, "small")

        # Blits the char to the screen.
        screen.blit( char_img, (pos[0] + index * (width * 4), pos[1]) )
