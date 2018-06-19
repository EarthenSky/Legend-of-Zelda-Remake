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

'''This is the pokemon class that holds info about a specific pokemon, be it wild
or a pokemon in your own party. The pokemon class will be implemented in the
pokemon_manager class.'''
class pokemon:
    def __init__ (self, pokemon_val, level):
        self.pokemon_val = pokemon_val

        # iterates the POKEMON dict and finds the current name.
        for name, value in POKEMON.items():
            if value == pokemon_val:
                self.name = name  # Saves the name of the pokemon.

        #self._img = -1  #asset_manager.getpokemon(pokemon_val)

        # Initialized stats.
        self._level = level

        self.attack_mod = 0
        self.defence_mod = 0
        self.exp = 0

        # Uninitialized stats.  In this case, -1 signifies null.
        self.max_health = -1
        self.current_health = -1
        self.attack = -1
        self.defence = -1
        self.speed = -1
        self.type = -1

        self.init_stats()  # Init the base stats.

        self._moves_list = []  # This is a list of all the moves.

    # This function inits the stats of a pokemon randomly.
    def init_stats(self):
        self.max_health = 7 + (random.randint(int(self._level/4), int(self._level * 3/4))) * 10
        self.current_health = self.max_health

        self.attack = random.randint(int(self._level/4), int(self._level * 3/4))
        self.defence = random.randint(int(self._level/4), int(self._level * 3/4))
        self.speed = random.randint(int(self._level/4), int(self._level * 3/4))

        if self.pokemon_val == POKEMON["BULBASAUR"]:
            self.type = TYPE["GRASS"]
        elif self.pokemon_val == POKEMON["IVYSAUR"]:
            self.type = TYPE["GRASS"]
        elif self.pokemon_val == POKEMON["CHARMANDER"]:
            self.type = TYPE["FIRE"]
        elif self.pokemon_val == POKEMON["CHARMELEON"]:
            self.type = TYPE["FIRE"]
        elif self.pokemon_val == POKEMON["SQUIRTLE"]:
            self.type = TYPE["WATER"]
        elif self.pokemon_val == POKEMON["WARTORTLE"]:
            self.type = TYPE["WATER"]
        elif self.pokemon_val == POKEMON["PIDGEY"]:
            self.type = TYPE["FLYING"]
        elif self.pokemon_val == POKEMON["PIDGEOTTO"]:
            self.type = TYPE["FLYING"]
        elif self.pokemon_val == POKEMON["GEODUDE"]:
            self.type = TYPE["ROCK"]
        elif self.pokemon_val == POKEMON["GRAVELER"]:
            self.type = TYPE["ROCK"]
        elif self.pokemon_val == POKEMON["SANDSHREW"]:
            self.type = TYPE["GROUND"]
        elif self.pokemon_val == POKEMON["CATERPIE"]:
            self.type = TYPE["BUG"]
        elif self.pokemon_val == POKEMON["METAPOD"]:
            self.type = TYPE["BUG"]
        elif self.pokemon_val == POKEMON["EKANS"]:
            self.type = TYPE["POISON"]
        elif self.pokemon_val == POKEMON["RATATA"]:
            self.type = TYPE["NORMAL"]
        elif self.pokemon_val == POKEMON["RATICATE"]:
            self.type = TYPE["NORMAL"]

    def get_level(self):
        return str(self._level)

    # Returns all the moves in a dict.
    def get_moves(self):
        return self._moves_list

    def check_new_move(self):
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

    def level_up(self):
        # Make random stats go up.
        gained_stat_points = random.randint(1, 4)  # both numbers are inclusive
        for index in range(gained_stat_points):
            stat = random.randint(0, 3)  # both numbers are inclusive
            stat_increment = random.randint(1, 2)

            if stat == 0:
                self.max_health += stat_increment * 10
                self.current_health += stat_increment * 10

            elif stat == 1:
                self._attack += stat_increment

            elif stat == 2:
                self._attack += stat_increment

            elif stat == 3:
                self._speed += stat_increment

        self._moves_list = []  # Reset the moves list.

        self.check_new_move()  # Check if leveling up learns any new moves.

    def evolve(self):
        pass  #TODO: make stats go up by a lot.

__builtin__.STAT_BOOST = {}
__builtin__.STAT_BOOST["NONE"]              =   -1
__builtin__.STAT_BOOST["PLAYER_DEF_UP"]     =    0
__builtin__.STAT_BOOST["OP_DEF_DOWN"]       =    1
__builtin__.STAT_BOOST["PLAYER_ATK_UP"]     =    2
__builtin__.STAT_BOOST["OP_ATK_DOWN"]       =    3
__builtin__.STAT_BOOST["PLAYER_ACC_UP"]     =    4
__builtin__.STAT_BOOST["OP_ACC_DOWN"]       =    5
__builtin__.STAT_BOOST["PLAYER_EVASION_UP"] =    6
__builtin__.STAT_BOOST["OP_EVASION_DOWN"]   =    7

''' This class holds the information for each move in the game.  (this is more like a data structure [struct] than a class.) '''
class move:
    def __init__(self, name):
        self.name = name
        self._init_move(name)
        self.max_pp = self.pp  # Set the unchanging "max_pp" value

    def get_type(self):
        for name, value in TYPE.items():
            if value == self.type:
                return str(name)  # Returns the pokemon's type as a string.

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
