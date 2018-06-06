'''This is the pokemon class that holds info about a specific pokemon, be it wild
or a pokemon in your own party. The pokemon class is often implemented in the
pokemon_manager class.'''

import __builtin__

# Only do this once.
if __name__ == "__main__":
    # An 'enum' that holds the names of all the pokemon.
    __builtin__.POKEMON = {}
    __builtin__.POKEMON["BULBASAUR"]    =   0
    __builtin__.POKEMON["IVYSAUR"]      =   1
    __builtin__.POKEMON["CHARMANDER"]   =   2
    __builtin__.POKEMON["CHARMELEON"]   =   3
    __builtin__.POKEMON["SQUIRTLE"]     =   4
    __builtin__.POKEMON["WARTORTLE"]    =   5
    __builtin__.POKEMON["PIDGEY"]       =   6
    __builtin__.POKEMON["PIDGEOTTO"]    =   7
    __builtin__.POKEMON["GEODUDE"]      =   8
    __builtin__.POKEMON["GRAVELER"]     =   9
    __builtin__.POKEMON["SANDSHREW"]    =   10
    __builtin__.POKEMON["CATERPIE"]     =   11
    __builtin__.POKEMON["METAPOD"]      =   12
    __builtin__.POKEMON["EKANS"]        =   13

class pokemon:
    def __init__ (self, pokemon_val, level):
        self.pokemon_val = pokemon_val
        self._img = -1 # asset_manager.getpokemon(pokemon_val)

        # Initialized stats.
        self._level = level

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

    def level_up(self):
        pass

    def evolve(self):
        pass
