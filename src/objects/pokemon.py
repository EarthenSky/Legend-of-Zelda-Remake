import __builtin__

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

'''This is the pokemon class that holds info about a specific pokemon, be it wild
or a pokemon in your own party. The pokemon class is often implemented in the
pokemon_manager class.'''
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

__builtin__.TYPE = {}
__builtin__.TYPE["GRASS"]  =    0
__builtin__.TYPE["FIRE"]   =    1
__builtin__.TYPE["WATER"]  =    2
__builtin__.TYPE["FLYING"] =    3
__builtin__.TYPE["ROCK"]   =    4
__builtin__.TYPE["GROUND"] =    5
__builtin__.TYPE["BUG"]    =    6
__builtin__.TYPE["POISON"] =    7
__builtin__.TYPE["NORMAL"] =    8

__builtin__.STAT_BOOST = {}
__builtin__.STAT_BOOST["NONE"]              =   -1
__builtin__.STAT_BOOST["PLAYER_DEF_UP"]     =    0
__builtin__.STAT_BOOST["OP_DEF_DOWN"]       =    1
__builtin__.STAT_BOOST["PLAYER_ATK_UP"]     =    2
__builtin__.STAT_BOOST["OP_ATK_DOWN"]       =    3
__builtin__.STAT_BOOST["PLAYER_ACC_UP"]     =    4
__builtin__.STAT_BOOST["OP_ACC_DOWN"]       =    5
__builtin__.STAT_BOOST["PLAYER_EVASION_UP"] =    4
__builtin__.STAT_BOOST["OP_EVASION_DOWN"]   =    5

''' This class holds the information for each move in the game.  (this is more like a data structure [struct] than a class.) '''
class move:
    # if stat_boost == -1, no stat boost.
    # 0 = my_def_up
    # 1 = their_def_down
    # 2 = my_attack_up
    # 3 = their_attack_down
    # type: ex. grass, fire, etc.

    def __init__(self, name, damage, stat_boost, type, pp):
        self.name = name
        self._init_move(name)

    def _init_move(self, name):
        if name == "tackle":
            self.damage = 40
            self.stat_boost = STAT_BOOST["NONE"]
            self.type = TYPE["NORMAL"]
            self.pp = 35
            self.accuracy = 100

        elif name == "tail whip":
            self.damage = 0
            self.stat_boost = STAT_BOOST["OP_DEF_DOWN"]
            self.type = TYPE["NORMAL"]
            self.pp = 30
            self.accuracy = 100

        elif name == "stomp":
            self.damage = 65
            self.stat_boost = STAT_BOOST["NONE"]
            self.type = TYPE["NORMAL"]
            self.pp = 20
            self.accuracy = 100

        elif name == "harden":
            self.damage = 0
            self.stat_boost = STAT_BOOST["PLAYER_DEF_UP"]
            self.type = TYPE["NORMAL"]
            self.pp = 30
            self.accuracy = -1  # NEVER MISS

        elif name == "gust":
            self.damage = 40
            self.stat_boost = STAT_BOOST["NONE"]
            self.type = TYPE["FLYING"]
            self.pp = 35
            self.accuracy = 100

        elif name == "peck":
            self.damage = 60
            self.stat_boost = STAT_BOOST["NONE"]
            self.type = TYPE["FLYING"]
            self.pp = 35
            self.accuracy = 100

        elif name == "string shot":
            self.damage = 0
            self.stat_boost = STAT_BOOST["OP_EVASION_DOWN"]
            self.type = TYPE["FLYING"]
            self.pp = 25
            self.accuracy = 90

        elif name == "water gun":
            self.damage = 40
            self.stat_boost = STAT_BOOST["NONE"]
            self.type = TYPE["WATER"]
            self.pp = 25
            self.accuracy = 100

        elif name == "ember":
            self.damage = 40
            self.stat_boost = STAT_BOOST["NONE"]
            self.type = TYPE["FIRE"]
            self.pp = 25
            self.accuracy = 100

        elif name == "vine whip":
            self.damage = 45
            self.stat_boost = STAT_BOOST["NONE"]
            self.type = TYPE["GRASS"]
            self.pp = 25
            self.accuracy = 100
