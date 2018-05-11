'''This is the player, who moves and is animated.'''

import sys

import pygame

# The asset manager helps render images.
sys.path.insert(0, 'src/managers/')  # This line tells the importer where to look for the module.
import asset_manager

SPEED = 60

class Player:

    def __init__(self, start_position):
        self.position = start_position

        # The last position of the player (create a new instance of start_position)
        self._last_position = list(start_position)

        # The value of the current frame of the player's animation.
        self._current_animation = 0

        # The direction the player is facing.  down, up, left, right is 0, 1, 2, 3.
        self.direction = 0

        # If the player is moving to the next tile.
        self._move = False

        # If the player is running.
        self._running = False

    # Moving and stuff.
    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if self.direction == 2:
                    # Start moving if the player is already pointing in the direction of the key that is pressed.
                    self._move = True
                    self._last_position = self.position
                    print "start move"
                else:
                    self.direction = 2

                return True
            elif event.key == pygame.K_RIGHT:
                self.direction = 3
                return True
            elif event.key == pygame.K_UP:
                self.direction = 1
                return True
            elif event.key == pygame.K_DOWN:
                self.direction = 0
                return True
        elif event.type == pygame.KEYUP:
            pass
        else:
            return False

    def draw(self, surface):
        asset_manager.draw_player(surface, self.position, self.direction, 0, True)

    def update(self, dt):
        pass

    # This function returns the offset of it's movement, to move the tilemaps.
    def move_player(self, dt):
        if self._move == True:
            if self.direction == 0:
                pass
            elif self.direction == 1:
                pass
            elif self.direction == 2:
                # case: player needs to move more, until they are on the tile.
                if self.position[0] > self._last_position[0] - 16:
                    # Move the player.
                    self.position[0] -= SPEED * dt
                    print str(self._last_position[0] - 16)
                else:
                    print "moved"
                    # Finish moving.
                    self._move = False
                    self.position[0] = self._last_position[0] - 16

            elif self.direction == 3:
                pass
