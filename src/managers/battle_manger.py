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

cursor = pygame.image.load("resc\images\menu_screens\m_cursor.png")

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

g_selected_move = 1  # Move goes from 1-4

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
    global g_selected_move
    # Draw the background
    asset_manager._draw(screen, background, (0, 0), (-1, -1, -1, -1))

    # Draw the menu item
    if current_battle_stage == 0:
        # Draw the text
        #text_manager.draw_text(screen, "What will", (12*4, 448 + 12*4))
        # The info box for the enemy's info and the eney pokemon's name
        asset_manager._draw(screen, enemy_info, (10*4, 10*4), (-1, -1, -1, -1))
        text_manager.draw_text_small(screen, g_other_pokemon.name, (18*4, 15*4))  # name
        text_manager.draw_text_small(screen, g_other_pokemon.get_level(), (92*4, 15*4))  # level
        text_manager.draw_text_small(screen, str(g_other_pokemon.current_health), (54*4, 25*4))  # level

        # The background for the player's info attack moves.
        asset_manager._draw(screen, player_info, (122*4, 75*4), (-1, -1, -1, -1))
        text_manager.draw_text_small(screen, g_active_pokemon.name, (139*4, 80*4))  # name
        text_manager.draw_text_small(screen, g_active_pokemon.get_level(), (213*4, 80*4))  # level
        text_manager.draw_text_small(screen, "{}-{}".format(g_active_pokemon.current_health, g_active_pokemon.max_health), (177*4, 90*4))  # level

        asset_manager.draw_pokemon( screen, g_active_pokemon.pokemon_val, POKEMON_TYPE["BACK"], [34*4, 65*4] )  # The good pokemon.
        asset_manager.draw_pokemon( screen, g_other_pokemon.pokemon_val, POKEMON_TYPE["FRONT"], [145*4, 22*4] )  # The bad pokemon.

        # Draw the attack moves info box.
        asset_manager._draw(screen, attack_box, (0, 448), (-1, -1, -1, -1))  # The background for the attack moves.

        # Get the variables that have to do with move list.
        move_list = g_active_pokemon.get_moves()
        move_count = len( move_list )

        # Draw the atack names by getting each name from the active pokemon's list of moves.  (btw, there is no way to have zero moves.)
        if move_count >= 1:
            text_manager.draw_text_small(screen, move_list[0].name, (16*4, 124*4))  # attack name

        if move_count >= 2:
            text_manager.draw_text_small(screen, move_list[1].name, (16*4, 140*4))  # attack name
        else:
            text_manager.draw_text_small(screen, "-", (16*4, 140*4))  # attack name

        if move_count >= 3:
            text_manager.draw_text_small(screen, move_list[2].name, (90*4, 124*4))  # attack name
        else:
            text_manager.draw_text_small(screen, "-", (90*4, 124*4))  # attack name

        if move_count >= 4:
            text_manager.draw_text_small(screen, move_list[3].name, (90*4, 140*4))  # attack name
        else:
            text_manager.draw_text_small(screen, "-", (90*4, 140*4))  # attack name

        # Draw selected move info if the move is an actual attack.
        if move_count >= g_selected_move:
            text_manager.draw_text_small(screen, str(move_list[g_selected_move-1].pp), (202*4, 124*4))  # pp
            text_manager.draw_text_small(screen, str(move_list[g_selected_move-1].max_pp), (221*4, 124*4))  # max_pp
            text_manager.draw_text_small(screen, str(move_list[g_selected_move-1].get_type()), (194*4, 142*4))  # type

        # Draw move cursor.
        if g_selected_move >= 4:
            screen.blit(cursor, (82*4, 140*4))
        elif g_selected_move >= 3:
            screen.blit(cursor, (82*4, 124*4))
        elif g_selected_move >= 2:
            screen.blit(cursor, (8*4, 140*4))
        elif g_selected_move >= 1:
            screen.blit(cursor, (8*4, 124*4))

    elif current_battle_stage == 1:
        asset_manager._draw(screen, battle_message_box, (0, 448), (-1, -1, -1, -1))  # The battle_message_box is drawn at the bottom.
    elif current_battle_stage == 2:
        pass

CHOOSE_ATTACK_STAGE = 0
MESSAGE_STAGE = 1

current_battle_stage = CHOOSE_ATTACK_STAGE
def update(dt):
    if current_battle_stage == CHOOSE_ATTACK_STAGE:
        pass
    elif current_battle_stage == MESSAGE_STAGE:
        pass
    elif current_battle_stage == 2:
        pass

# This function checks for any input.  (called after update)
def check_input():
    global g_selected_move

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Close pygame before application closes.
            pygame.quit()
            print "DEBUG: Application Complete."
            sys.exit(0)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if g_selected_move == 2:
                    g_selected_move = 1
                elif g_selected_move == 4:
                    g_selected_move = 3
            if event.key == pygame.K_DOWN:
                if g_selected_move == 1:
                    g_selected_move = 2
                elif g_selected_move == 3:
                    g_selected_move = 4
            if event.key == pygame.K_LEFT:
                if g_selected_move == 3:
                    g_selected_move = 1
                elif g_selected_move == 4:
                    g_selected_move = 2
            if event.key == pygame.K_RIGHT:
                if g_selected_move == 1:
                    g_selected_move = 3
                elif g_selected_move == 2:
                    g_selected_move = 4
            if event.key == pygame.K_z:
                pass  #TODO: use move.

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
