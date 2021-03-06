import sys
import pygame
import math
import random
import __builtin__

sys.path.insert(0, 'src/managers/')  # This line tells the importer where to look for the module.
import pokemon_manager
import asset_manager
import text_manager
import desc_manager

# Init images here.
background = pygame.image.load("resc/images/battle_background.png").convert()

player_info = pygame.image.load("resc/images/good_info_panel.png").convert_alpha()
enemy_info = pygame.image.load("resc/images/enemy_info_panel.png").convert_alpha()

attack_box = pygame.image.load("resc/images/attacks_box.png").convert()

battle_message_box = pygame.image.load("resc/images/battle_message_box.png").convert()

cursor = pygame.image.load("resc\images\menu_screens\m_cursor.png")

player_defence_mod = 0
enemy_defence_mod = 0
player_attack_mod = 0
enemy_attack_mod = 0

# This function starts a battle.
def start_grass_battle(screen):
    global player_defence_mod, enemy_defence_mod, player_attack_mod, enemy_attack_mod, keep_looping

    set_active_pokemon( pokemon_manager.get_next_pokemon(screen, True) )
    if random.randint(1, 2) == 1:
        set_other_pokemon( pokemon_manager.create_random_enemy_by_level( int(pokemon_manager.get_next_pokemon(-1, True).get_level())-1 ) )
    else:
        set_other_pokemon( pokemon_manager.create_random_enemy_by_level( int(pokemon_manager.get_next_pokemon(-1, True).get_level())+2 ) )

    # Do init stuff.
    current_battle_stage = CHOOSE_ATTACK_STAGE

    # Init the modifiers.
    player_defence_mod = 0
    enemy_defence_mod = 0
    player_attack_mod = 0
    enemy_attack_mod = 0

    keep_looping = True
    battle_loop(screen)  # Starts the battle_loop.

# These will be classes, not ints.
g_active_pokemon = -1
g_other_pokemon = -1

g_selected_move = 1  # Move goes from 1-4

def set_active_pokemon(pokemon):
    global g_active_pokemon
    g_active_pokemon = pokemon

def set_other_pokemon(pokemon):
    global g_other_pokemon
    g_other_pokemon = pokemon

# Do Player attack.
def _player_attack(active_pokemon_move, other_pokemon_move):
    global player_defence_mod, enemy_defence_mod, player_attack_mod, enemy_attack_mod

    # Do Player attack.
    if active_pokemon_move.pp != 0:
        g_active_pokemon.get_moves()[g_selected_move-1].pp -= 1  # Make pp go down by one

        if active_pokemon_move.stat_boost == STAT_BOOST["OP_DEF_DOWN"]:
            enemy_defence_mod -= 8
            desc_manager.add_message_to_queue("The opponent POKeMON's", "defence is lowered...")
        elif active_pokemon_move.stat_boost == STAT_BOOST["OP_ATK_DOWN"]:
            enemy_attack_mod -= 8
            desc_manager.add_message_to_queue("The opponent POKeMON's", "attack is lowered...")
        elif active_pokemon_move.stat_boost == STAT_BOOST["PLAYER_DEF_UP"]:
            player_defence_mod += 8
            desc_manager.add_message_to_queue("Your POKeMON's defence is", "increased...")
        elif active_pokemon_move.stat_boost == STAT_BOOST["PLAYER_ATK_UP"]:
            player_attack_mod += 8
            desc_manager.add_message_to_queue("Your POKeMON's attack is", "increased...")

        attack_dif = (g_other_pokemon.defence - g_active_pokemon.attack) + enemy_defence_mod - player_attack_mod

        damage = int(active_pokemon_move.damage * (1 - (0.03 * attack_dif)) / 3)  # Big attack dif means less damage.  Negitave means more damage.

        if damage != 0:
            # If the pokemon is too low-leveled for a high damage, attack, do less damage.
            if g_active_pokemon.get_level() < int(active_pokemon_move.damage/3):
                damage *= ( ( g_active_pokemon.get_level()/int(active_pokemon_move.damage/3) ) / 3 ) + 2/3

            if active_pokemon_move.type == TYPE["POISON"] and g_other_pokemon.type == TYPE["GRASS"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif active_pokemon_move.type == TYPE["POISON"] and g_other_pokemon.type == TYPE["BUG"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif active_pokemon_move.type == TYPE["POISON"] and g_other_pokemon.type == TYPE["GROUND"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")
            elif active_pokemon_move.type == TYPE["POISON"] and g_other_pokemon.type == TYPE["POISON"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")
            elif active_pokemon_move.type == TYPE["POISON"] and g_other_pokemon.type == TYPE["ROCK"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")

            elif active_pokemon_move.type == TYPE["GRASS"] and g_other_pokemon.type == TYPE["BUG"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")
            elif active_pokemon_move.type == TYPE["GRASS"] and g_other_pokemon.type == TYPE["FIRE"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")
            elif active_pokemon_move.type == TYPE["GRASS"] and g_other_pokemon.type == TYPE["FLYING"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")
            elif active_pokemon_move.type == TYPE["GRASS"] and g_other_pokemon.type == TYPE["GRASS"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")
            elif active_pokemon_move.type == TYPE["GRASS"] and g_other_pokemon.type == TYPE["GROUND"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif active_pokemon_move.type == TYPE["GRASS"] and g_other_pokemon.type == TYPE["POISON"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")
            elif active_pokemon_move.type == TYPE["GRASS"] and g_other_pokemon.type == TYPE["ROCK"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif active_pokemon_move.type == TYPE["GRASS"] and g_other_pokemon.type == TYPE["WATER"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")

            elif active_pokemon_move.type == TYPE["WATER"] and g_other_pokemon.type == TYPE["FIRE"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif active_pokemon_move.type == TYPE["WATER"] and g_other_pokemon.type == TYPE["GRASS"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")
            elif active_pokemon_move.type == TYPE["WATER"] and g_other_pokemon.type == TYPE["GROUND"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif active_pokemon_move.type == TYPE["WATER"] and g_other_pokemon.type == TYPE["ROCK"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")

            elif active_pokemon_move.type == TYPE["ROCK"] and g_other_pokemon.type == TYPE["BUG"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif active_pokemon_move.type == TYPE["ROCK"] and g_other_pokemon.type == TYPE["FIRE"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif active_pokemon_move.type == TYPE["ROCK"] and g_other_pokemon.type == TYPE["FLYING"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif active_pokemon_move.type == TYPE["ROCK"] and g_other_pokemon.type == TYPE["ROCK"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")

            elif active_pokemon_move.type == TYPE["GROUND"] and g_other_pokemon.type == TYPE["FIRE"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif active_pokemon_move.type == TYPE["GROUND"] and g_other_pokemon.type == TYPE["FLYING"]:
                damage *= 0
                desc_manager.add_message_to_queue("Your ground move deals 0 damage", "against the opponent flying pokemon!")
            elif active_pokemon_move.type == TYPE["GROUND"] and g_other_pokemon.type == TYPE["GRASS"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")
            elif active_pokemon_move.type == TYPE["GROUND"] and g_other_pokemon.type == TYPE["POISON"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif active_pokemon_move.type == TYPE["GROUND"] and g_other_pokemon.type == TYPE["ROCK"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")

            elif active_pokemon_move.type == TYPE["FIRE"] and g_other_pokemon.type == TYPE["BUG"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif active_pokemon_move.type == TYPE["FIRE"] and g_other_pokemon.type == TYPE["GRASS"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif active_pokemon_move.type == TYPE["FIRE"] and g_other_pokemon.type == TYPE["ROCK"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")
            elif active_pokemon_move.type == TYPE["FIRE"] and g_other_pokemon.type == TYPE["WATER"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")

            elif active_pokemon_move.type == TYPE["NORMAL"] and g_other_pokemon.type == TYPE["ROCK"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")

            elif active_pokemon_move.type == TYPE["FLYING"] and g_other_pokemon.type == TYPE["BUG"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif active_pokemon_move.type == TYPE["FLYING"] and g_other_pokemon.type == TYPE["GRASS"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif active_pokemon_move.type == TYPE["FLYING"] and g_other_pokemon.type == TYPE["ROCK"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")

    else:  # If no pp, do 5 damage.
        damage = 5

    damage *= 0.8

    if damage < 1 and active_pokemon_move.damage != 0:
        damage = 1

    g_other_pokemon.current_health -= int(damage)  # Decrement the enemy's hp.

    # Check if the opponent is dead.
    if g_other_pokemon.current_health <= 0:
        g_other_pokemon.current_health = 0
        desc_manager.add_message_to_queue("The opponent's " + g_other_pokemon.name, "has fainted...")

    if active_pokemon_move.pp == 0:
        desc_manager.add_message_to_queue("Your POKeMON uses flail", "It deals 5 damage")
    else:
        desc_manager.add_message_to_queue("Your POKeMON uses " + active_pokemon_move.name, "It deals {} damage".format( int(damage) ))

    if g_other_pokemon.current_health <= 0:
        return 1  # This means stop the battle.

    return 0

def _enemy_attack(active_pokemon_move, other_pokemon_move, enemy_random_move):
    global player_defence_mod, enemy_defence_mod, player_attack_mod, enemy_attack_mod

    # Do Enemy attack.
    if other_pokemon_move.pp != 0:
        g_other_pokemon.get_moves()[enemy_random_move-1].pp -= 1  # Make pp go down by one.

        if other_pokemon_move.stat_boost == STAT_BOOST["OP_DEF_DOWN"]:
            player_defence_mod -= 8
            desc_manager.add_message_to_queue("Your POKeMON's defence is", "lowered...")
        elif other_pokemon_move.stat_boost == STAT_BOOST["OP_ATK_DOWN"]:
            player_attack_mod -= 8
            desc_manager.add_message_to_queue("Your POKeMON's attack is", "lowered...")
        elif other_pokemon_move.stat_boost == STAT_BOOST["PLAYER_DEF_UP"]:
            enemy_defence_mod += 8
            desc_manager.add_message_to_queue("The opposing POKeMON's", "defence is increased...")
        elif other_pokemon_move.stat_boost == STAT_BOOST["PLAYER_ATK_UP"]:
            enemy_attack_mod += 8
            desc_manager.add_message_to_queue("The opposing POKeMON's", "attack is increased...")

        attack_dif = (g_active_pokemon.defence - g_other_pokemon.attack) + player_defence_mod - enemy_attack_mod

        damage = int(other_pokemon_move.damage * (1 - (0.03 * attack_dif)) / 3)  # Big attack dif means less damage.  Negitave means more damage.

        if damage != 0:
            # If the pokemon is too low-leveled for a high damage, attack, do less damage.
            if g_other_pokemon.get_level() < int(other_pokemon_move.damage/3):
                damage *= ( ( g_other_pokemon.get_level()/int(other_pokemon_move.damage/3) ) / 3 ) + 2/3

            if other_pokemon_move.type == TYPE["POISON"] and g_active_pokemon.type == TYPE["GRASS"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif other_pokemon_move.type == TYPE["POISON"] and g_active_pokemon.type == TYPE["BUG"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif other_pokemon_move.type == TYPE["POISON"] and g_active_pokemon.type == TYPE["GROUND"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")
            elif other_pokemon_move.type == TYPE["POISON"] and g_active_pokemon.type == TYPE["POISON"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")
            elif other_pokemon_move.type == TYPE["POISON"] and g_active_pokemon.type == TYPE["ROCK"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")

            elif other_pokemon_move.type == TYPE["GRASS"] and g_active_pokemon.type == TYPE["BUG"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")
            elif other_pokemon_move.type == TYPE["GRASS"] and g_active_pokemon.type == TYPE["FIRE"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")
            elif other_pokemon_move.type == TYPE["GRASS"] and g_active_pokemon.type == TYPE["FLYING"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")
            elif other_pokemon_move.type == TYPE["GRASS"] and g_active_pokemon.type == TYPE["GRASS"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")
            elif other_pokemon_move.type == TYPE["GRASS"] and g_active_pokemon.type == TYPE["GROUND"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif other_pokemon_move.type == TYPE["GRASS"] and g_active_pokemon.type == TYPE["POISON"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")
            elif other_pokemon_move.type == TYPE["GRASS"] and g_active_pokemon.type == TYPE["ROCK"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif other_pokemon_move.type == TYPE["GRASS"] and g_active_pokemon.type == TYPE["WATER"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")

            elif other_pokemon_move.type == TYPE["WATER"] and g_active_pokemon.type == TYPE["FIRE"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif other_pokemon_move.type == TYPE["WATER"] and g_active_pokemon.type == TYPE["GRASS"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")
            elif other_pokemon_move.type == TYPE["WATER"] and g_active_pokemon.type == TYPE["GROUND"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif other_pokemon_move.type == TYPE["WATER"] and g_active_pokemon.type == TYPE["ROCK"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")

            elif other_pokemon_move.type == TYPE["ROCK"] and g_active_pokemon.type == TYPE["BUG"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif other_pokemon_move.type == TYPE["ROCK"] and g_active_pokemon.type == TYPE["FIRE"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif other_pokemon_move.type == TYPE["ROCK"] and g_active_pokemon.type == TYPE["FLYING"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif other_pokemon_move.type == TYPE["ROCK"] and g_active_pokemon.type == TYPE["ROCK"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")

            elif other_pokemon_move.type == TYPE["GROUND"] and g_active_pokemon.type == TYPE["FIRE"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif other_pokemon_move.type == TYPE["GROUND"] and g_active_pokemon.type == TYPE["FLYING"]:
                damage *= 0
                desc_manager.add_message_to_queue("The GROUND move deals 0 damage", "against the flying pokemon.")
            elif other_pokemon_move.type == TYPE["GROUND"] and g_active_pokemon.type == TYPE["GRASS"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")
            elif other_pokemon_move.type == TYPE["GROUND"] and g_active_pokemon.type == TYPE["POISON"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif other_pokemon_move.type == TYPE["GROUND"] and g_active_pokemon.type == TYPE["ROCK"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")

            elif other_pokemon_move.type == TYPE["FIRE"] and g_active_pokemon.type == TYPE["BUG"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif other_pokemon_move.type == TYPE["FIRE"] and g_active_pokemon.type == TYPE["GRASS"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif other_pokemon_move.type == TYPE["FIRE"] and g_active_pokemon.type == TYPE["ROCK"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")
            elif other_pokemon_move.type == TYPE["FIRE"] and g_active_pokemon.type == TYPE["WATER"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")

            elif other_pokemon_move.type == TYPE["NORMAL"] and g_active_pokemon.type == TYPE["ROCK"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")

            elif other_pokemon_move.type == TYPE["FLYING"] and g_active_pokemon.type == TYPE["BUG"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif other_pokemon_move.type == TYPE["FLYING"] and g_active_pokemon.type == TYPE["GRASS"]:
                damage *= 2
                desc_manager.add_message_to_queue("It's super effective!", "...")
            elif other_pokemon_move.type == TYPE["FLYING"] and g_active_pokemon.type == TYPE["ROCK"]:
                damage *= 0.5
                desc_manager.add_message_to_queue("It's not very effective", "...")

    else:  # If no pp, do 5 dps.
        damage = 5

    damage *= 0.8

    if damage < 1 and other_pokemon_move.damage != 0:
        damage = 1

    g_active_pokemon.current_health -= int(damage)  # Decrement the player's hp.

    # Check if the player's pokemon is dead.
    if g_active_pokemon.current_health <= 0:
        g_active_pokemon.current_health = 0
        desc_manager.add_message_to_queue("Your " + g_active_pokemon.name, "has fainted...")

    if other_pokemon_move.pp == 0:
        desc_manager.add_message_to_queue("The Enemy POKeMON uses flail", "It deals 5 damage")
    else:
        desc_manager.add_message_to_queue("The Enemy POKeMON uses " + other_pokemon_move.name, "It deals {} damage".format( int(damage) ))

    if g_active_pokemon.current_health <= 0:
        return 2  # This means to swap pokemon.  If no pokemon left, death message, then close screen.  (darksouls sound effect)

    return 0

# Deal damage and stuff here.
def trade_attacks(screen):
    active_pokemon_move = g_active_pokemon.get_moves()[g_selected_move-1]

    # Pick a random move for the enemy.
    enemy_random_move = random.randint(1, len( g_other_pokemon.get_moves() ))
    other_pokemon_move = g_other_pokemon.get_moves()[enemy_random_move-1]

    # Pokemon with highest speed attacks first.
    if g_active_pokemon.speed > g_other_pokemon.speed:
        # Do Player attack first.
        if _player_attack(active_pokemon_move, other_pokemon_move) == 1:
            desc_manager.check_queue(screen)
            draw(screen)
            return 1  # This means stop the battle.

        desc_manager.check_queue(screen)
        draw(screen)

        # Do Enemy attack second.
        if _enemy_attack(active_pokemon_move, other_pokemon_move, enemy_random_move) == 2:
            desc_manager.check_queue(screen)
            draw(screen)
            return 2  # This means stop the battle.

        desc_manager.check_queue(screen)
        draw(screen)

    else:
        # Do Enemy attack first.
        if _enemy_attack(active_pokemon_move, other_pokemon_move, enemy_random_move) == 2:
            desc_manager.check_queue(screen)
            draw(screen)
            return 2  # This means stop the battle.

        desc_manager.check_queue(screen)
        draw(screen)

        # Do Player attack second.
        if _player_attack(active_pokemon_move, other_pokemon_move) == 1:
            desc_manager.check_queue(screen)
            draw(screen)
            return 1  # This means stop the battle.

        desc_manager.check_queue(screen)
        draw(screen)

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
        text_manager.draw_text_small(screen, "{}/{}".format(int(g_other_pokemon.current_health), int(g_other_pokemon.max_health)), (56*4, 25*4))  # level

        # The background for the player's info attack moves.
        asset_manager._draw(screen, player_info, (122*4, 75*4), (-1, -1, -1, -1))
        text_manager.draw_text_small(screen, g_active_pokemon.name, (139*4, 80*4))  # name
        text_manager.draw_text_small(screen, g_active_pokemon.get_level(), (213*4, 80*4))  # level
        text_manager.draw_text_small(screen, "{}/{}".format(int(g_active_pokemon.current_health), int(g_active_pokemon.max_health)), (177*4, 90*4))  # hp and max hp
        text_manager.draw_text_small(screen, "{}/{}".format(g_active_pokemon.exp, int(int(g_active_pokemon.get_level()) ** 1.2) * 8), (177*4, 99*4))  # xp and max xp

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
BAG = 1

current_battle_stage = CHOOSE_ATTACK_STAGE
def update(dt):
    if current_battle_stage == CHOOSE_ATTACK_STAGE:
        pass
    elif current_battle_stage == BAG:
        pass

# This function checks for any input.  (called after update)
def check_input(screen):
    global g_selected_move, keep_looping, player_attack_mod, player_defence_mod

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
            if event.key == pygame.K_z and current_battle_stage == CHOOSE_ATTACK_STAGE and g_selected_move <= len(g_active_pokemon.get_moves()):
                result = trade_attacks(screen)  # Tell the pokemon to trade moves. (only do this if the player is selecting a valid move.)

                if result == 1:
                    keep_looping = False  # End battle.

                    # Give exp to the alive POKeMON
                    new_exp = int( int(g_other_pokemon.get_level()) ** 1.3 * random.randint(4, 10) )
                    g_active_pokemon.exp += new_exp

                    draw(screen)
                    desc_manager.add_message_to_queue("Your POKeMON's gains", "{} experience points".format(new_exp))
                    desc_manager.check_queue(screen)

                    # If the pokemon has enough exp, level it up.
                    while g_active_pokemon.exp > int(int(g_active_pokemon.get_level()) ** 1.2) * 8:
                        g_active_pokemon.exp -= int(int(g_active_pokemon.get_level()) ** 1.2) * 8
                        g_active_pokemon.level_up()

                        draw(screen)
                        desc_manager.add_message_to_queue( "It's stats increase", "..." )
                        desc_manager.add_message_to_queue( "Your POKeMON grows stronger", "and reaches level {}".format(g_active_pokemon.get_level()) )
                        desc_manager.check_queue(screen)

                elif result == 2:
                    player_attack_mod = 0
                    player_defence_mod = 0
                    set_active_pokemon( pokemon_manager.get_next_pokemon(screen, False) )  # Swap pokemon to next pokemon, or LOSE.

                desc_manager.check_queue(screen)

keep_looping = True
def battle_loop(screen):
    global keep_looping

    # Create the object that handles framerate regulation and delta_time.
    framerate_clock = pygame.time.Clock()
    delta_time = framerate_clock.tick(60) / 1000.0

    while keep_looping:
        draw(screen)

        pygame.display.update()  # Updates the display with any changes.

        update(delta_time)

        check_input(screen)

        # Pause pygame and calculate delta time.
        delta_time = framerate_clock.tick(60) / 1000.0
