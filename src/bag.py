import pygame
import sys

# The asset manager helps render images.
sys.path.insert(0, 'src/managers/')  # This line tells the importer where to look for the module.
import text_manager

class Bag:

    def __init__(self):
        self.potions = 0
        self.pokeballs = 0

    def add_to_potion(self, amount):
        self.potions += amount

    def add_to_pokeball(self, amount):
        self.pokeballs += amount

    def get_potions(self):
        return self.potions

    def get_pokeballs(self):
        return self.pokeballs
