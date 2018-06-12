import sys
import pygame

sys.path.insert(0, 'src/managers/')  # This line tells the importer where to look for the module.
import pokemon_manager
import asset_manager
import text_manager

# Init images here.
background = pygame.image.load("resc/images/battle_background.png").convert()

player_info = pygame.image.load("resc/images/good_info_panel.png").convert_alpha()
enemy_info = pygame.image.load("resc/images/enemy_info_panel.png").convert_alpha()

attack_box = pygame.image.load("resc/images/attacks_box.png").convert()

battle_message_box = pygame.image.load("resc/images/battle_message_box.png").convert()

# This function starts a battle.
def start_grass_battle(screen):
    set_active_pokemon( pokemon_manager.get_next_pokemon() )
    set_other_pokemon( pokemon_manager.create_random_enemy() )

    # Do init stuff.
    current_battle_stage = 0

    battle_loop(screen)  # Starts the battle_loop.

# These will be classes.
g_active_pokemon = -1
g_other_pokemon = -1

def set_active_pokemon(pokemon):
    global g_active_pokemon
    g_active_pokemon = pokemon

def set_other_pokemon(pokemon):
    global g_other_pokemon
    g_other_pokemon = pokemon

# Deal damage and stuff here.
def do_attacks(active_pokemon_move_index, other_pokemon_move_index):
    pass

def draw(screen):
    # Draw the background
    asset_manager._draw(screen, background, (0, 0), (-1, -1, -1, -1))

    # Draw the menu item
    if current_battle_stage == 0:
        # Draw the text
        #text_manager.draw_text(screen, "What will", (12*4, 448 + 12*4))
        #text_manager.draw_text(screen, "{} do?".format(g_active_pokemon.name), (12*4, 448 + 26*4))

        asset_manager._draw(screen, attack_box, (0, 448), (-1, -1, -1, -1))  # The background for the attack moves.

        asset_manager._draw(screen, enemy_info, (0, 0), (-1, -1, -1, -1))  # The background for the attack moves.
        asset_manager._draw(screen, player_info, (136*4, 75*4), (-1, -1, -1, -1))  # The background for the attack moves.
    elif current_battle_stage == 1:
        asset_manager._draw(screen, battle_message_box, (0, 448), (-1, -1, -1, -1))  # The battle_message_box is drawn at the bottom.
    elif current_battle_stage == 2:
        pass

current_battle_stage = 0
def update(dt):
    if current_battle_stage == 0:
        pass
    elif current_battle_stage == 1:
        pass
    elif current_battle_stage == 2:
        pass

# This function checks for any input.  (called after update)
def check_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Close pygame before application closes.
            pygame.quit()
            print "DEBUG: Application Complete."
            sys.exit(0)

def battle_loop(screen):
    # Create the object that handles framerate regulation and delta_time.
    framerate_clock = pygame.time.Clock()
    delta_time = framerate_clock.tick(60) / 1000.0
    everysecond_val = 0

    keep_looping = True
    while keep_looping:
        draw(screen)

        pygame.display.update()  # Updates the display with any changes.

        update(delta_time)

        check_input()

        # Pause pygame and calculate delta time.
        delta_time = framerate_clock.tick(60) / 1000.0

        everysecond_val += delta_time

        # Tells person they are in a message
        if everysecond_val > 1:
            everysecond_val = 0
            print "In a BATTLE!"
