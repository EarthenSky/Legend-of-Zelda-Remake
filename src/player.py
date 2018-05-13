'''This is the player, who moves and is animated.'''

import sys

import pygame

# The asset manager helps render images.
sys.path.insert(0, 'src/managers/')  # This line tells the importer where to look for the module.
import asset_manager

SPEED = 180

class Player:

    def __init__(self, start_position):
        # Where the player is drawn. (center of screen.)
        self._draw_position = start_position

        # The mathematical position of the player.
        self.position = list(start_position)

        # The last position of the player (create a new instance of start_position)
        self._last_position = list(start_position)

        print(id(self.position), id(self._last_position))

        # The value of the current frame of the player's animation.
        self._current_animation = 0

        # The direction the player is facing.  down, up, left, right is 0, 1, 2, 3.
        self.direction = 0

        # If the player is moving to the next tile.
        self._move = False

        # If the player is running.
        self._running = False

        # Keys that are down.
        self.left_key_down = False
        self.right_key_down = False
        self.up_key_down = False
        self.down_key_down = False

        # The timer varaibles.
        self._timer_on = False
        self._timer_val = 0

    def _check_new_move_dir(self, dt):
        # Check if need to move another direction
        if (self.left_key_down and self.left_key_down and self.left_key_down and self.left_key_down) == False:
            self._move = False
            return (0, 0)
        else:
            # If a key is pressed, turn in that direction, don't start a timer.  Start moving.
            if self.left_key_down == True:
                self.direction = 2
                self.position[0] += -SPEED * dt
                return (SPEED * dt, 0)

            elif self.right_key_down == True:
                self.direction = 3
                self.position[0] += SPEED * dt
                return (-SPEED * dt, 0)


    def _move_player(self, dt):
            if self.direction == 0:
                pass
            elif self.direction == 1:
                pass
            elif self.direction == 2:
                # Case: player needs to move more, until they are on the tile.
                if self.position[0] > self._last_position[0] - 64:
                    self.position[0] += -SPEED * dt
                    return (SPEED * dt, 0)
                else:
                    # Hit tile so flush the position values.
                    self.position[0] = self._last_position[0] - 64
                    self._last_position[0] = self.position[0]

                    return self._check_new_move_dir(dt)

                    '''
                    # Finish moving if key is up.
                    if self.left_key_down == True:
                        self._last_position[0] -= 64
                        self.position[0] += -SPEED * dt
                        return (SPEED * dt, 0)
                    else:
                        self._move = False
                        self.position[0] = self._last_position[0] - 64
                        return (0, 0)
                    '''

            elif self.direction == 3:
                # Case: player needs to move more, until they are on the tile.
                if self.position[0] < self._last_position[0] + 64:
                    self.position[0] += SPEED * dt
                    return (-SPEED * dt, 0)
                else:
                    # Hit tile so flush the position values.
                    self.position[0] = self._last_position[0] + 64
                    self._last_position[0] = self.position[0]

                    return self._check_new_move_dir(dt)


    # Moving and stuff.
    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                '''
                if self._move == False:
                    if self.direction == 2:
                        # Start moving if the player is already pointing in the direction of the key that is pressed.
                        self._move = True
                        self._last_position = list(self.position)
                    else:
                        self.direction = 2
                '''
                self.left_key_down = True
                return True
            elif event.key == pygame.K_RIGHT:
                '''
                if self._move == False:
                    if self.direction == 3:
                        # Start moving if the player is already pointing in the direction of the key that is pressed.
                        self._move = True
                        self._last_position = list(self.position)
                    else:
                        self.direction = 3
                '''
                self.right_key_down = True
                return True
            elif event.key == pygame.K_UP:
                self.direction = 1

                self.up_key_down = True
                return True
            elif event.key == pygame.K_DOWN:
                self.direction = 0

                self.down_key_down = True
                return True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.left_key_down = False
                return True
            elif event.key == pygame.K_RIGHT:
                self.right_key_down = False
                return True
            elif event.key == pygame.K_UP:
                self.up_key_down = False
                return True
            elif event.key == pygame.K_DOWN:
                self.down_key_down = False
                return True
        else:
            return False

    def draw(self, surface):
        asset_manager.draw_player(surface, self._draw_position, self.direction, 0, True)

    def update(self, dt):
        if self._move == False:
            # If a key is pressed, turn in that direction and start a timer.
            if self.left_key_down == True:
                # If player is already facing the direction they need to move, don't start timer.
                if self.direction == 2:
                    self._timer_on = True
                    self._timer_val = 0

                self.direction = 2
                self._move = True

            elif self.right_key_down == True:
                if self.direction == 3:
                    self._timer_on = True
                    self._timer_val = 0

                self.direction = 3
                self._move = True

            return (0, 0)  # No movement
        else:
            # Increase the timer by the amount of time passed.
            if self._timer_on == True:
                self._timer_val += dt
                print (self._timer_val)

                # 100 ms or 0.1s is how long a direction key has to be pressed to start moving, not just direction turn.
                if self._timer_val >= 0.2:
                    # Turn off timer and flush it.
                    self._timer_on = False
                    self._timer_val = 0

                    # If the pressed key is up, don't move.
                    if self.direction == 2 and self.left_key_down == False:
                        self._move = False
                    elif self.direction == 3 and self.right_key_down == False:
                        self._move = False

                return (0, 0)  # No movement
            else:
                return self._move_player(dt)

'''
    # This function WILL return the offset of it's movement, to move the tilemaps.
    def move_player(self, dt):
        if self._move == True:
            if self.direction == 0:
                pass
            elif self.direction == 1:
                pass
            elif self.direction == 2:
                # Case: player needs to move more, until they are on the tile.
                if self.position[0] > self._last_position[0] - 64:
                    self.position[0] += -SPEED * dt
                    return (SPEED * dt, 0)
                else:
                    # Finish moving if key is up.
                    if self.left_key_down == True:
                        self._last_position[0] -= 64
                        self.position[0] += -SPEED * dt
                        return (SPEED * dt, 0)
                    else:
                        self._move = False
                        self.position[0] = self._last_position[0] - 64
                        return (0, 0)

            elif self.direction == 3:
                # Case: player needs to move more, until they are on the tile.
                if self.position[0] < self._last_position[0] + 64:
                    self.position[0] += SPEED * dt
                    return (-SPEED * dt, 0)
                else:
                    # Finish moving if key is up.
                    if self.right_key_down == True:
                        self._last_position[0] += 64
                        self.position[0] += SPEED * dt
                        return (-SPEED * dt, 0)
                    else:
                        self._move = False
                        self.position[0] = self._last_position[0] + 64
                        return (0, 0)
        else:
            return (0, 0)
'''
