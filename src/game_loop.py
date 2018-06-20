'''This file contains the main gameloop, which controls sequential
scenes (environment scenes), usually just called different scenes.'''

import sys
import pygame

import __builtin__  # TODO: PLEASE NO!!!

# Different Scene Constants.
__builtin__.PLAYER_HOUSE_UPSTAIRS = 0
__builtin__.PLAYER_HOUSE_DOWNSTAIRS = 1
__builtin__.OUTSIDE = 2
__builtin__.LAB = 3
# TODO: add more scenes.

# Constants.
SCREEN_SIZE = [240 * 4, 160 * 4]

# Starts and sets up pygame.
pygame.init()
DISPLAY_SURFACE = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Pokemon Wave Blue")

# Must be imported after pygame has been initialized.
sys.path.insert(0, 'src/objects/')  # This line tells the importer where to look for the module.
import tilemap

# Must be imported after pygame has been initialized.
sys.path.insert(0, 'src/managers/')  # This line tells the importer where to look for the module.
import desc_manager
import battle_manger
import pokemon_manager

import player  # The player needs to move.
import menu
import story
import npc

sys.path.insert(0, 'src/objects/')  # This line tells the importer where to look for the module.
import pokemon

# Globals.
__builtin__.g_game_stopped = False
__builtin__.g_current_scene = OUTSIDE

# Create & load the different scenes.
__builtin__.g_outside_tilemap = tilemap.Tilemap("outside.map", [0, 0], 0)
__builtin__.g_lab_tilemap = tilemap.Tilemap( "lab.map", [0, 0], pygame.image.load("resc/images/lab.png").convert() )
__builtin__.g_player_house_down_tilemap = tilemap.Tilemap( "player_house_down.map", [0, 0], pygame.image.load("resc/images/player_house_down.png").convert() )
__builtin__.g_player_house_up_tilemap = tilemap.Tilemap( "player_house_up.map", [0, 0], pygame.image.load("resc/images/player_house_up.png").convert() )
__builtin__.g_route_tilemap = tilemap.Tilemap( "route.map", [0, -64 * 64], 0 )

# Create the player object.
__builtin__.g_player = player.Player( [240*4/2-8*4, 160*4/2-4*4] )

# Create oak, and add his different images to a list
__builtin__.g_oak_grass = npc.NPC([1152, -64], pygame.image.load("resc\images\g_oak.png"), True, 0)
__builtin__.g_oak_lab = npc.NPC([448, 256], pygame.image.load("resc\images\g_oak.png"), False, 0)
__builtin__.g_oak_list = [g_oak_grass, g_oak_lab]


#Create rest of the npc/trainers
__builtin__.g_trainer_one = npc.NPC([1792, -656], pygame.image.load("resc\images\g_trainer.png"), False, 0)

# Create the menu class.
g_menu = menu.Menu(DISPLAY_SURFACE)
g_story = story.Story(DISPLAY_SURFACE)

# This function handles any input.  Called before update.
def handle_input():
    global g_game_stopped

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            g_game_stopped = True
        elif g_player.handle_input(event):
            pass
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                g_menu.enable_menu()

# Must be imported after pygame has been initialized.
sys.path.insert(0, 'src/managers/')  # This line tells the importer where to look for the module.
import asset_manager

# This is for drawing stuff.  Called before update.
def draw():
    if g_current_scene == PLAYER_HOUSE_UPSTAIRS:
        DISPLAY_SURFACE.fill( (0, 0, 0) )
        g_player_house_up_tilemap.draw(DISPLAY_SURFACE)
    elif g_current_scene == PLAYER_HOUSE_DOWNSTAIRS:
        DISPLAY_SURFACE.fill( (0, 0, 0) )
        g_player_house_down_tilemap.draw(DISPLAY_SURFACE)
    elif g_current_scene == OUTSIDE:
        DISPLAY_SURFACE.fill( (0, 0, 0) )
        g_outside_tilemap.draw(DISPLAY_SURFACE)
        g_route_tilemap.draw(DISPLAY_SURFACE)

        g_trainer_one.draw(DISPLAY_SURFACE)

        for i in range(len(g_oak_list)):
            if g_oak_list[i] == g_oak_grass:
                g_oak_grass.draw(DISPLAY_SURFACE)

    elif g_current_scene == LAB:
        DISPLAY_SURFACE.fill( (0, 0, 0) )
        g_lab_tilemap.draw(DISPLAY_SURFACE)

        for i in range(len(g_oak_list)):
	        if g_oak_list[i] == g_oak_lab:
	            g_oak_lab.draw(DISPLAY_SURFACE)
    else:
        print "GAME IS NOT IN ANY SCENE."

    #asset_manager.draw_pokemon( DISPLAY_SURFACE, (7, 10), POKEMON_TYPE["FRONT"], [100, 100] )
    #asset_manager.draw_pokemon( DISPLAY_SURFACE, (2, 6), POKEMON_TYPE["BACK"], [100, 300] )

    # Draw the player.
    g_player.draw(DISPLAY_SURFACE)

    # Stuff drawn over the player.
    if g_current_scene == PLAYER_HOUSE_UPSTAIRS:
        g_player_house_up_tilemap.over_draw(DISPLAY_SURFACE)
    elif g_current_scene == PLAYER_HOUSE_DOWNSTAIRS:
        g_player_house_down_tilemap.over_draw(DISPLAY_SURFACE)
    elif g_current_scene == OUTSIDE:
        g_outside_tilemap.over_draw(DISPLAY_SURFACE)
        g_route_tilemap.over_draw(DISPLAY_SURFACE)
    elif g_current_scene == LAB:
        g_lab_tilemap.over_draw(DISPLAY_SURFACE)

    # Check for any popup boxes.
    desc_manager.check_queue(DISPLAY_SURFACE)

# This is the "do game math" function.  Put any math or functional code here.
def update(dt):
    #pokemon_manager.pokemon_list.append( pokemon_manager.create_random_enemy() )  # Give player a random pokemon.
    #pokemon_manager.pokemon_list.append( pokemon_manager.create_random_enemy() )  # Give player a random pokemon.
    #battle_manger.start_grass_battle(DISPLAY_SURFACE)

    g_story.update()

    # Move the player and give the movement value to the other scenes.
    player_offset = g_player.update(dt, DISPLAY_SURFACE)

    if g_current_scene == PLAYER_HOUSE_UPSTAIRS:
        g_player_house_up_tilemap.update(dt)
        g_player_house_up_tilemap.get_offset(player_offset)
    elif g_current_scene == PLAYER_HOUSE_DOWNSTAIRS:
        g_player_house_down_tilemap.update(dt)
        g_player_house_down_tilemap.get_offset(player_offset)
    elif g_current_scene == OUTSIDE:
        # Update the tilemap, then translate it.
        g_outside_tilemap.update(dt)
        g_outside_tilemap.get_offset(player_offset)
        g_route_tilemap.update(dt)
        g_route_tilemap.get_offset(player_offset)
        g_trainer_one.get_offset(player_offset)
        g_oak_grass.get_offset(player_offset)
    elif g_current_scene == LAB:
        # Update the tilemap, then translate it.
        g_lab_tilemap.update(dt)
        g_lab_tilemap.get_offset(player_offset)
        g_oak_lab.get_offset(player_offset)
    else:
        print "GAME IS NOT IN ANY SCENE."

# This function returns if the game is completed or not.  Return true if game is done.
def is_exit():
    return g_game_stopped
