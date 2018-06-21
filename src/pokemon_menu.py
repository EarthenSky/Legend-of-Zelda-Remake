import pygame
import sys

# The asset manager helps render images.
sys.path.insert(0, 'src/managers/')  # This line tells the importer where to look for the module.
import text_manager
import pokemon_manager
import asset_manager
import text_manager

class Pokemon_Menu:

    def __init__(self, surface):
        self.surface = surface

    def update(self):  # Actually draw but... whatever.
        text_manager.draw_text_small(self.surface, "Fainted POKeMON: ", (7*4, 140*4))

        for i in range(len(pokemon_manager.pokemon_list)):
            if i == 0:
                asset_manager.draw_pokemon(self.surface, pokemon_manager.pokemon_list[i].pokemon_val, 2, (5*4, 22*4))
                text_manager.draw_text_small(self.surface, pokemon_manager.pokemon_list[i].name, (14*4, 56*4))
                text_manager.draw_text_small(self.surface, "lvl " + pokemon_manager.pokemon_list[i].get_level(), (38*4, 40*4))

                text_manager.draw_text_small(self.surface, "1", (2*4, 46*4))

                if pokemon_manager.pokemon_list[i].current_health <= 0:
                    text_manager.draw_text_small(self.surface, "1", (104*4, 140*4))

            elif i == 1:
                asset_manager.draw_pokemon(self.surface, pokemon_manager.pokemon_list[i].pokemon_val, 2, (92*4, 0*4))
                text_manager.draw_text_small(self.surface, pokemon_manager.pokemon_list[i].name + " lvl " + pokemon_manager.pokemon_list[i].get_level(), (124*4, 17*4))
                text_manager.draw_text_small(self.surface, "2", (90*4, 17*4))

                if pokemon_manager.pokemon_list[i].current_health <= 0:
                    text_manager.draw_text_small(self.surface, ",2", (111*4, 140*4))

            elif i == 2:
                asset_manager.draw_pokemon(self.surface, pokemon_manager.pokemon_list[i].pokemon_val, 2, (92*4, 24*4))
                text_manager.draw_text_small(self.surface, pokemon_manager.pokemon_list[i].name + " lvl " + pokemon_manager.pokemon_list[i].get_level(), (124*4, 41*4))
                text_manager.draw_text_small(self.surface, "3", (90*4, 41*4))

                if pokemon_manager.pokemon_list[i].current_health <= 0:
                    text_manager.draw_text_small(self.surface, ",3", (125*4, 140*4))

            elif i == 3:
                asset_manager.draw_pokemon(self.surface, pokemon_manager.pokemon_list[i].pokemon_val, 2, (92*4, 48*4))
                text_manager.draw_text_small(self.surface, pokemon_manager.pokemon_list[i].name + " lvl " + pokemon_manager.pokemon_list[i].get_level(), (124*4, 65*4))
                text_manager.draw_text_small(self.surface, "4", (90*4, 65*4))

                if pokemon_manager.pokemon_list[i].current_health <= 0:
                    text_manager.draw_text_small(self.surface, ",4", (139*4, 140*4))

            elif i == 4:
                asset_manager.draw_pokemon(self.surface, pokemon_manager.pokemon_list[i].pokemon_val, 2, (92*4, 72*4))
                text_manager.draw_text_small(self.surface, pokemon_manager.pokemon_list[i].name + " lvl " + pokemon_manager.pokemon_list[i].get_level(), (124*4, 89*4))
                text_manager.draw_text_small(self.surface, "5", (90*4, 89*4))

                if pokemon_manager.pokemon_list[i].current_health <= 0:
                    text_manager.draw_text_small(self.surface, ",5", (153*4, 140*4))

            elif i == 5:
                asset_manager.draw_pokemon(self.surface, pokemon_manager.pokemon_list[i].pokemon_val, 2, (92*4, 96*4))
                text_manager.draw_text_small(self.surface, pokemon_manager.pokemon_list[i].name + " lvl " + pokemon_manager.pokemon_list[i].get_level(), (124*4, 113*4))
                text_manager.draw_text_small(self.surface, "6", (90*4, 113*4))
