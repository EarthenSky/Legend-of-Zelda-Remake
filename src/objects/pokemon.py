import __builtin__
import random

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

        # iterates the POKEMON dict and finds the current name.
        for name, value in POKEMON.items():
            print value
            if value == pokemon_val:
                self.name = name  # Saves the name of the pokemon.

        #self._img = -1  #asset_manager.getpokemon(pokemon_val)

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
        self._moves_list = []  # list of all the moves.

    # This function inits the stats of a pokemon randomly.
    def init_stats(self):
        self._max_health = 5 + random.randint(int(self._level/4), int(self._level * 3/4))
        self._current_health = self._max_health

        self._attack = random.randint(int(self._level/4), int(self._level * 3/4))
        self._defence = random.randint(int(self._level/4), int(self._level * 3/4))
        self._speed = random.randint(int(self._level/4), int(self._level * 3/4))

    # Returns hp and max_hp in a dict.
    def get_health(self):
        return { ["hp"] : self._current_health, ["max_hp"] : self._max_health }

    # Returns the other stats in a dict.
    def get_stats(self):
        return { ["attack"] : self._attack, ["defence"] : self._defence, ["speed"] : self._speed }

    def get_level(self):
        return str(self._level)

    # Returns all the moves in a dict.
    def get_moves(self):
        return self._moves_list

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
        # Make random stats go up.

        self._moves_list = []  # Reset the moves list.

        if self.pokemon_val == POKEMON["BULBASAUR"]:
            self._moves_list.append( move("tackle") )
            self._moves_list.append( move("growl") )

            if self._level >= 8:
                self._moves_list.append( move("vine whip") )

        elif self.pokemon_val == POKEMON["IVYSAUR"]:
            self._moves_list.append( move("tackle") )
            self._moves_list.append( move("growl") )
            self._moves_list.append( move("vine whip") )
            self._moves_list.append( move("razor leaf") )

        elif self.pokemon_val == POKEMON["CHARMANDER"]:
            self._moves_list.append( move("scratch") )
            self._moves_list.append( move("tail whip") )

            if self._level >= 8:
                self._moves_list.append( move("ember") )

        elif self.pokemon_val == POKEMON["CHARMELEON"]:
            self._moves_list.append( move("scratch") )
            self._moves_list.append( move("tail whip") )
            self._moves_list.append( move("ember") )
            self._moves_list.append( move("fire blast") )

        elif self.pokemon_val == POKEMON["SQUIRTLE"]:
            self._moves_list.append( move("scratch") )
            self._moves_list.append( move("tail whip") )

            if self._level >= 8:
                self._moves_list.append( move("water gun") )

        elif self.pokemon_val == POKEMON["WARTORTLE"]:
            self._moves_list.append( move("scratch") )
            self._moves_list.append( move("harden") )
            self._moves_list.append( move("water gun") )
            self._moves_list.append( move("bubble beam") )

        elif self.pokemon_val == POKEMON["PIDGEY"]:
            self._moves_list.append( move("gust") )
            self._moves_list.append( move("peck") )

            if self._level >= 8:
                self._moves_list.append( move("slash") )

        elif self.pokemon_val == POKEMON["PIDGEOTTO"]:
            self._moves_list.append( move("gust") )
            self._moves_list.append( move("peck") )
            self._moves_list.append( move("slash") )
            self._moves_list.append( move("drill peck") )

        elif self.pokemon_val == POKEMON["GEODUDE"]:
            self._moves_list.append( move("tackle") )
            self._moves_list.append( move("harden") )

            if self._level >= 8:
                self._moves_list.append( move("rock throw") )

        elif self.pokemon_val == POKEMON["GRAVELER"]:
            self._moves_list.append( move("tackle") )
            self._moves_list.append( move("harden") )
            self._moves_list.append( move("rock throw") )
            self._moves_list.append( move("rage") )

        elif self.pokemon_val == POKEMON["SANDSHREW"]:
            self._moves_list.append( move("slash") )
            self._moves_list.append( move("sand attack") )
            self._moves_list.append( move("stomp") )

        elif self.pokemon_val == POKEMON["CATERPIE"]:
            self._moves_list.append( move("tackle") )

            if self._level >= 4:
                self._moves_list.append( move("string shot") )

                if self._level >= 7:
                    self._moves_list.append( move("pin missile") )

        elif self.pokemon_val == POKEMON["METAPOD"]:
            self._moves_list.append( move("tackle") )
            self._moves_list.append( move("string shot") )
            self._moves_list.append( move("pin missile") )
            self._moves_list.append( move("harden") )

        elif self.pokemon_val == POKEMON["EKANS"]:
            self._moves_list.append( move("sludge bomb") )
            self._moves_list.append( move("sand attack") )

            if self._level >= 5:
                self._moves_list.append( move("growl") )

                if self._level >= 12:
                    self._moves_list.append( move("rage") )

        elif self.pokemon_val == POKEMON["RATATA"]:
            self._moves_list.append( move("tackle") )
            self._moves_list.append( move("growl") )

        elif self.pokemon_val == POKEMON["RATICATE"]:
            self._moves_list.append( move("tackle") )
            self._moves_list.append( move("growl") )
            self._moves_list.append( move("slash") )
            self._moves_list.append( move("rage") )

    def evolve(self):
        pass  #TODO: make stats go up by a lot.

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
    def __init__(self, name):
        self.name = name
        self._init_move(name)

    def _init_move(self, name):
        if name == "tackle":
            self.damage = 40
            self.stat_boost = STAT_BOOST["NONE"]
            self.type = TYPE["NORMAL"]
            self.pp = 35
            self.accuracy = 100

        if name == "scratch":
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

        elif name == "growl":
            self.damage = 0
            self.stat_boost = STAT_BOOST["OP_ATK_DOWN"]
            self.type = TYPE["NORMAL"]
            self.pp = 30
            self.accuracy = 100

        elif name == "stomp":
            self.damage = 65
            self.stat_boost = STAT_BOOST["NONE"]
            self.type = TYPE["GROUND"]
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

        elif name == "sand attack":
            self.damage = 0
            self.stat_boost = STAT_BOOST["OP_ACC_DOWN"]
            self.type = TYPE["GROUND"]
            self.pp = 15
            self.accuracy = 100

        elif name == "fire blast":
            self.damage = 90
            self.stat_boost = STAT_BOOST["NONE"]
            self.type = TYPE["FIRE"]
            self.pp = 10
            self.accuracy = 85

        elif name == "drill peck":
            self.damage = 80
            self.stat_boost = STAT_BOOST["NONE"]
            self.type = TYPE["FLYING"]
            self.pp = 15
            self.accuracy = 95

        elif name == "bubble beam":
            self.damage = 70
            self.stat_boost = STAT_BOOST["OP_DEF_DOWN"]
            self.type = TYPE["WATER"]
            self.pp = 10
            self.accuracy = 90

        elif name == "razor leaf":
            self.damage = 120
            self.stat_boost = STAT_BOOST["NONE"]
            self.type = TYPE["GRASS"]
            self.pp = 5
            self.accuracy = 95

        elif name == "rock throw":
            self.damage = 60
            self.stat_boost = STAT_BOOST["NONE"]
            self.type = TYPE["ROCK"]
            self.pp = 15
            self.accuracy = 100

        elif name == "sludge bomb":
            self.damage = 90
            self.stat_boost = STAT_BOOST["NONE"]
            self.type = TYPE["POISON"]
            self.pp = 20
            self.accuracy = 100

        elif name == "rage":
            self.damage = 210
            self.stat_boost = STAT_BOOST["NONE"]
            self.type = TYPE["NORMAL"]
            self.pp = 35
            self.accuracy = 25

        elif name == "pin missile":
            self.damage = 110
            self.stat_boost = STAT_BOOST["NONE"]
            self.type = TYPE["BUG"]
            self.pp = 25
            self.accuracy = 70

        elif name == "slash":
            self.damage = 70
            self.stat_boost = STAT_BOOST["NONE"]
            self.type = TYPE["NORMAL"]
            self.pp = 15
            self.accuracy = 95
