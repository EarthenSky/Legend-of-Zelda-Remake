'''This class manages all the collected pokemon and which ones are in the pc or in
the player's party.  This class also has a function that is used to create a pokemon.'''

import __builtin__  # For truly global variables.  (This is actually pretty bad.)
import sys
import random

sys.path.insert(0, 'src/objects/')  # This line tells the importer where to look for the module.
import pokemon

pokemon_list = []  # These are your 6 pokemon.

# Adds a pokemon to the list.
def add_pokemon(pokemon_val, level):
    pokemon_list.append( pokemon.pokemon(pokemon_val, level) )

def delete_pokemon():
    pass

# TODO: CHECK FOR THE NEXT ALIVE POEKMON IN THE LIST.  IF NONE EXIST, THE PLAYER LOSES.
def get_next_pokemon():
    return pokemon_list[0]

# This functions grates a random pokemon on found in the grass.
def create_random_enemy():
    random_pokemon_number = __builtin__.POKEMON["BULBASAUR"]
    random_level = random.randint(4, 10)

    pkm = pokemon.pokemon(random_pokemon_number, random_level)  # Create a new instance of the pokemon class.
    pkm.check_new_move()  # Remember to set the pokemon's initial moves.

    return pkm

pokemon_list.append( create_random_enemy() )
