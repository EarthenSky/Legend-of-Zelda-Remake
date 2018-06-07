'''This is the pokemon class that holds info about a specific pokemon, be it wild
or a pokemon in your own party. The pokemon class is often implemented in the
pokemon_manager class.'''

import __builtin__

# Only do this once.  # right?
if __name__ == "__main__":
    # An 'enum' that holds the names of all the pokemon.
    __builtin__.POKEMON = {}
    __builtin__.POKEMON["BULBASAUR"]    =   (0, 0)
    __builtin__.POKEMON["IVYSAUR"]      =   (0, 1)
    __builtin__.POKEMON["CHARMANDER"]   =   (1, 0)
    __builtin__.POKEMON["CHARMELEON"]   =   (1, 1)
    __builtin__.POKEMON["SQUIRTLE"]     =   (2, 0)
    __builtin__.POKEMON["WARTORTLE"]    =   (2, 1)
    __builtin__.POKEMON["PIDGEY"]       =   (0, 3)
    __builtin__.POKEMON["PIDGEOTTO"]    =   (0, 4)
    __builtin__.POKEMON["GEODUDE"]      =   (4, 14)
    __builtin__.POKEMON["GRAVELER"]     =   (5, 0)
    __builtin__.POKEMON["SANDSHREW"]    =   (3, 5)
    __builtin__.POKEMON["CATERPIE"]     =   (3, 0)
    __builtin__.POKEMON["METAPOD"]      =   (3, 1)
    __builtin__.POKEMON["EKANS"]        =   (2, 4)
    __builtin__.POKEMON["RATATA"]       =   (1, 3)
    __builtin__.POKEMON["RATICATE"]     =   (1, 4)

class pokemon:
    def __init__ (self, pokemon_val, level):
        self.pokemon_val = pokemon_val
        self._img = -1  #asset_manager.getpokemon(pokemon_val)

        # Initialized stats.
        self._level = level

        self._attack_mod = 0
        self._defence_mod = 0

        # Uninitialized stats.  In this case, -1 signifies null.
        self._max_health = -1
        self._current_health = -1

        self._attack = -1
        self._defence = -1
        self._speed = -1

        self.init_stats()  # Init the stats

        self.moves = [4]  # 4 length
        print "LOOK AT MEEEEEEEEEEEEE!!!!!!!! (ARRAY TEST, LEN SHOULD BE 4)", self.moves, "len:", len(self.moves)

    # This function inits the stats of a pokemon randomly.
    def init_stats(self):
        self._max_health = 5 + random.randint(int(level/4), int(level * 3/4))
        self._current_health = self._max_health

        self._attack = random.randint(int(level/4), int(level * 3/4))
        self._defence = random.randint(int(level/4), int(level * 3/4))
        self._speed = random.randint(int(level/4), int(level * 3/4))

    # Returns hp and max_hp in a dict.
    def get_health(self):
        return { ["hp"] : self._current_health, ["max_hp"] : self._max_health }

    # Returns the other stats in a dict.
    def get_stats(self):
        return { ["attack"] : self._attack, ["defence"] : self._defence, ["speed"] : self._speed }

    # Returns all the moves in a dict.
    def get_moves(self):
        pass

    # Add val to the attack mod.
    def inc_attack_mod(self, val):
        self._attack_mod += val

    # Add val to the defence mod.
    def inc_defence_mod(self, val):
        self._defence_mod += val

    # Reset the attack and defence stat modifiers.
    def reset_stat_mods(self):
        self._attack_mod = 0
        self._defence_mod = 0

    def level_up(self):
        pass

    def evolve(self):
        pass
