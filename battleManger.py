import sys

sys.path.insert(0, 'src/managers/')  # This line tells the importer where to look for the module.
import pokemon_manager

# This function starts a battle.
def start_grass_battle(screen):
    set_active_pokemon( pokemon_manager.get_next_pokemon() )
    set_other_pokemon( pokemon_manager.create_random_enemy() )

    # Do init stuff.
    current_battle_stage = 0

    battle_loop(screen)  # Starts the battle_loop.

active_pokemon = -1
other_pokemon = -1

def set_active_pokemon(pokemon):
    active_pokemon = pokemon

def set_other_pokemon(pokemon):
    other_pokemon = pokemon

# Deal damage and stuff here.
def do_attacks(active_pokemon_move_index, other_pokemon_move_index):
    pass

def draw(screen):
    pass
    # Draw the background

current_battle_stage = 0

def update(dt):
    if current_battle_stage == 0:
        pass
    elif current_battle_stage == 1:
        pass
    elif current_battle_stage == 2:
        pass

def battle_loop(screen):
    # Create the object that handles framerate regulation and delta_time.
    framerate_clock = pygame.time.Clock()
    delta_time = framerate_clock.tick(60) / 1000.0
    everysecond_val = 0

    keep_looping = True
    while keep_looping:
        draw(screen)
        update(delta_time)

        # Pause pygame and calculate delta time.
        delta_time = framerate_clock.tick(60) / 1000.0

        everysecond_val += delta_time

        # Tells person they are in a message
        if everysecond_val > 1:
            everysecond_val = 0
            print "In a BATTLE!


''' This class holds the informatino for each move in the game.  (this is more like a data structure [struct] than a class.) '''
class move:
    # if stat_boost == -1, no stat boost.
    # 0 = my_def_up
    # 1 = their_def_down
    # 2 = my_attack_up
    # 3 = their_attack_down

    # type, i.e. grass, fire, etc.
    # 0 = grass, fire, water, flying, rock, ground, bug, poison, normal.

    def __init__(self, name, damage, stat_boost, type):
        self.name = name
        self.damage = damage
        self.stat_boost = stat_boost
        self.type = type
