import pygame
import sys

# The asset manager helps render images.
sys.path.insert(0, 'src/managers/')  # This line tells the importer where to look for the module.
import text_manager
import bag

class Menu:
    def __init__(self, screen):
        self.m_bag = bag.Bag()

        # Loads the images
        self.menu_image = pygame.image.load("resc\images\menu_screens\g_menu.png")
        self.cursor = pygame.image.load("resc\images\menu_screens\m_cursor.png")
        self.pokemon_menu_image = pygame.image.load("resc\images\menu_screens\m_pokemon.png")
        self.pokemon_bag_image = pygame.image.load("resc\images\menu_screens\m_bag.png")

        # Assigns the screen
        self.screen = screen

        # Gets dimensions of screen menu and cursor
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()
        self.image_width, self.image_height = self.menu_image.get_rect().size
        self.cursor_width, self.cursor_height = self.cursor.get_rect().size

        # Places cursor on screen
        self.cursor_x, self.cursor_y = (self.screen_width - self.image_width) + 32, 40
        self.bag_cursor_x, self.bag_cursor_y = (98*4 - (9*4), 48)

        # Amount of options in the menu (for knowing where the cursor is)
        self.text_items = 3

        # The main menu loop
        self.run_menu = True

        # The pokemon menu and bag menu loops
        self.run_pokemon_menu = False
        self.run_bag_menu = False

        # The amount of items in your bag
        self.items_in_bag = []

        # Adds pokeballs and potions to your bag
        self.items_in_bag.append("POTION          x")
        self.items_in_bag.append("POKe BALL       x")
        #print self.items_in_bag[0]

        # Amount of potions and pokeballs in your bag
        self.potions = 0
        self.pokeballs = 0

    # Writes the menu options on the screen
    def display_menu_options(self):
        self.screen.blit(self.cursor, (self.cursor_x, self.cursor_y))
        text_manager.draw_text(self.screen, "POKeMON", ((self.screen_width - self.image_width) + 60, 44))
        text_manager.draw_text(self.screen, "BAG", ((self.screen_width - self.image_width) + 60, 44 + 60))
        text_manager.draw_text(self.screen, "EXIT", ((self.screen_width - self.image_width) + 60, 44 + 120))

    # Displays pokemon menu
    def pokemon_menu(self):
        self.screen.blit(self.pokemon_menu_image, (0, 0))

    # Displays pokemon bag
    def pokemon_bag(self):
        self.screen.blit(self.pokemon_bag_image, (0, 0))
        self.screen.blit(self.cursor, (self.bag_cursor_x, self.bag_cursor_y))

        #self.potions = self.m_bag.get_potions()
        #self.pokeballs = self.m_bag.get_pokeballs()

        #print (self.potions, self.pokeballs)

        # Makes sure cancel is below every item in bag
        for i in range(len(self.items_in_bag)):
            text_manager.draw_text(self.screen, self.items_in_bag[i], (98*4, 52 + (i*64)))
            text_manager.draw_text(self.screen, "CANCEL", (98*4, 52 + (len(self.items_in_bag)*64)))

    # Closes out all menus
    def exit_menu(self):
        if self.run_pokemon_menu == True:
            self.run_pokemon_menu = False
        if self.run_bag_menu == True:
            self.run_bag_menu = False

        self.run_menu = False

    # Enables the menu
    def enable_menu(self):
        # Globals.
        delta_time = 0

        # Create the object that handles framerate regulation and delta_time.
        framerate_clock = pygame.time.Clock()
        g_delta_time = framerate_clock.tick(60) / 1000.0

        menu_pokemon = False
        menu_bag = False

        self.run_menu = True

        # Starts menu loop
        while self.run_menu:
            # Blits menu to screen and displays text
            self.screen.blit(self.menu_image, (self.screen_width - (self.image_width + 1), 1))
            self.display_menu_options()

            # If pokemon menu is selected, display it
            if self.run_pokemon_menu == True:
                self.pokemon_menu()

            # If bag is selected, run it
            if self.run_bag_menu == True:
                self.pokemon_bag()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # Exits the menu if x is pressed
                    if event.key == pygame.K_x:
                        self.exit_menu()

                    # Key down and up moves the cursor by 60 pixels
                    elif event.key == pygame.K_DOWN:
                        # Makes sure cursor doesn't go lower than it should
                        # depends on whether it's in the menu or not
                        if self.run_bag_menu == True:
                            if self.bag_cursor_y >= 52+ ((len(self.items_in_bag) - 1)*64):
                                pass
                            else:
                                self.bag_cursor_y += 60

                        else:
                            if self.cursor_y >= 60 *(self.text_items - 1):
                                pass
                            else:
                                self.cursor_y += 60

                    # So that cursor doesn't go too high
                    elif event.key == pygame.K_UP:
                        if self.run_bag_menu == True:
                            if self.bag_cursor_y <= 52:
                                pass
                            else:
                                self.bag_cursor_y -= 60

                        else:
                            if self.cursor_y <= 44:
                                pass
                            else:
                                self.cursor_y -= 60

                    elif event.key == pygame.K_z:
                        #print self.run_bag_menu
                        #print self.run_menu
                        if self.run_bag_menu == True:
                            # Checks if your cursor is next to potions pokeballs
                            # or exit with the use of magic numbers
                            if self.bag_cursor_y == 48:
                                print "you have " + self.m_bag.get_potions() + " potions"
                            if self.bag_cursor_y == 48 + 60:
                                print "you have " + self.m_bag.get_pokeballs() + " pokeballs"
                            if self.bag_cursor_y == 48+120:
                                self.exit_menu()

                        # When the menu is running, checks which option cursor is
                        # next to
                        if self.run_menu == True:
                            # Next to the pokemon menu
                            if self.cursor_y == 40:
                                self.run_pokemon_menu = True

                            # Next to the bag menu
                            if self.cursor_y == 40+60:
                                self.run_bag_menu = True

                            # Next to exit
                            if self.cursor_y == 40+120:
                                self.run_menu = False

                elif self._check_skip_box(event) == True:
                    pass

            pygame.display.update() # Updates the display with changes.

            # Pause pygame and calculate delta time.
            delta_time = framerate_clock.tick(60) / 1000.0

    # This function checks if the thing is quit.
    def _check_skip_box(self, event):
        if event.type == pygame.QUIT:
            # Close pygame before application closes.
            pygame.quit()
            print "DEBUG: Application Complete."
            sys.exit(0)
            return True

        elif g_player.handle_input(event):
            return True

        return False
