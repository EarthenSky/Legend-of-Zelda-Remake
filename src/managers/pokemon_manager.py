'''This class manages all the collected pokemon and which ones are in the pc or in
the player's party.  This class also has a function that is used to create a pokemon.'''
import sys
import time
import random

import __builtin__  # For truly global variables.  (This is actually pretty bad.)

import pygame

sys.path.insert(0, 'src/objects/')  # This line tells the importer where to look for the module.
import pokemon

sys.path.insert(0, 'src/managers/')  # This line tells the importer where to look for the module.
import desc_manager

pokemon_list = []  # These are your 6 pokemon.

# Adds a pokemon to the list.
def add_pokemon(pokemon_val, level):
    pokemon_list.append( pokemon.pokemon(pokemon_val, level) )

def delete_pokemon():
    pass

# CHECK FOR THE NEXT ALIVE POEKMON IN THE LIST.  IF NONE EXIST, THE PLAYER LOSES, and GAME EXITS.
def get_next_pokemon(screen):
    for index in range(0, len(pokemon_list)):
        if pokemon_list[index].current_health > 0:
            desc_manager.add_message_to_queue("You send out your next pokemon", "...")
            return pokemon_list[index]

    # Quit the game.  You lost.
    desc_manager.add_message_to_queue("You Lose", "...")
    desc_manager.add_message_to_queue("Your last pokemon fainted...", "D:")
    desc_manager.check_queue(screen)

    # Close pygame before application closes.
    pygame.quit()
    print "DEBUG: Application Complete."
    sys.exit(0)

# This functions grates a random pokemon.
def create_random_enemy():
    random_pokemon_number = __builtin__.POKEMON["BULBASAUR"]  #TODO: get random pokemon
    random_level = 5

    pkm = pokemon.pokemon(random_pokemon_number, random_level)  # Create a new instance of the pokemon class.
    pkm.check_new_move()  # Remember to set the pokemon's initial moves.

    return pkm

# This functions grates a random pokemonin grass.
def create_random_enemy_by_level(level_avg):
    random_pokemon_number = __builtin__.POKEMON["BULBASAUR"]  #TODO: get random pokemon
    random_level = abs( random.randint(level_avg-6, level_avg) )

    pkm = pokemon.pokemon(random_pokemon_number, random_level)  # Create a new instance of the pokemon class.
    pkm.check_new_move()  # Remember to set the pokemon's initial moves.

    return pkm
