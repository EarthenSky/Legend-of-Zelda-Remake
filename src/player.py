'''This is the player, who moves and is animated.  Movement is a little complicated.'''

import sys
import pygame

#import __builtin__  # This is a terrible solution.  Fix this. TODO: DONT DO THIS!!!!!

# The asset manager helps render images.
sys.path.insert(0, 'src/managers/')  # This line tells the importer where to look for the module.
import asset_manager

SPEED = 235
ANIMATION_SPEED = 0.138  # 0.138s or 138ms per frame.

class Player:
    def __init__(self, start_position):
        self._draw_position = start_position  # Where the player is drawn. (center of screen.)
        self.position = list(start_position)  # The mathematical position of the player.
        self._last_position = list(start_position) # The last position of the player

        self._current_animation = 0  # The current frame of the player's animation.
        self._animation_key = [0, 2, 0, 1]  # This holds which animation to play on which frame.

        self.direction = 0  # The direction the player is facing.  down, up, left, right is 0, 1, 2, 3.

        self._move = False  # If the player is moving to the next tile.

        self._running = False  # If the player is running.

        # Keys that are down.
        self.left_key_down = False
        self.right_key_down = False
        self.up_key_down = False
        self.down_key_down = False

        # The timer varaibles.
        self._timer_on = False
        self._timer_val = 0

        # The value used for the timer for the player's animation.
        self._animation_timer_val = 0

        # If this variable is true, check for collision just before moving.
        self._check_collision = False

    # Moving and stuff.
    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.left_key_down = True
                return True
            elif event.key == pygame.K_RIGHT:
                self.right_key_down = True
                return True
            elif event.key == pygame.K_UP:
                self.up_key_down = True
                return True
            elif event.key == pygame.K_DOWN:
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
        asset_manager.draw_player(surface, self._draw_position, self.direction, self._animation_key[self._current_animation], True)

    # Check for collision.
    def check_collision(self):
        if g_current_scene == OUTSIDE:
            pass

        # I know it's backwards... just..y'know..JUSt... ok?
        # If a key is pressed, turn in that direction, don't start a timer.  Start moving.
        if self.direction == 2:
            tiley, tilex = g_outside_tilemap.get_tile( int(round(self.position[0]/64)) - 1, int(round(self.position[1]/64)) )

        elif self.direction == 3:
            tiley, tilex = g_outside_tilemap.get_tile( int(round(self.position[0]/64)) + 1, int(round(self.position[1]/64)) )

        elif self.direction == 1:
            tiley, tilex = g_outside_tilemap.get_tile( int(round(self.position[0]/64)), int(round(self.position[1]/64)) - 1)

        elif self.direction == 0:
            tiley, tilex = g_outside_tilemap.get_tile( int(round(self.position[0]/64)), int(round(self.position[1]/64)) + 1)

        # Check for the tiles that mean collision
        if tiley == 9 or tiley == 10 or tiley == 3 or tiley == 8:
            # Stop moving.
            self._move = False

            # Turn off timer and flush it.
            self._timer_on = False
            self._timer_val = 0

            return True

        elif (tiley == 1 or tiley == 2) and (tilex > 1):
            # Stop moving.
            self._move = False

            # Turn off timer and flush it.
            self._timer_on = False
            self._timer_val = 0

            return True

        elif tiley == 6 and (tilex == 1 or tilex == 2 or tilex == 3):
            # Stop moving.
            self._move = False

            # Turn off timer and flush it.
            self._timer_on = False
            self._timer_val = 0

            return True

        else:
            return False

    def _update_animation(self, dt):
        self._animation_timer_val += dt

        # If the timer has gone on for 0.2 seconds, change to the next animation frame.
        if self._animation_timer_val >= ANIMATION_SPEED:
            self._animation_timer_val = 0

            # Update frame number
            self._current_animation += 1
            if self._current_animation >= 4:
                self._current_animation = 0

    # Check if the player needs to move in another direction before stopping.
    def _check_new_move_dir(self, dt):
        # Check if need to move another direction  # Case: the player has stopped moving because all keys are up
        if (self.left_key_down or self.right_key_down or self.up_key_down or self.down_key_down) == False:
            self._move = False

        else:
            # If a key is pressed, turn in that direction, don't start a timer.  Start moving.
            if self.left_key_down == True:
                self.direction = 2

                # Only move if there is no collsion found.
                if self.check_collision() == False:
                    self.position[0] += -SPEED * dt

            elif self.right_key_down == True:
                self.direction = 3

                # Only move if there is no collsion found.
                if self.check_collision() == False:
                    self.position[0] += SPEED * dt

            elif self.up_key_down == True:
                self.direction = 1

                # Only move if there is no collsion found.
                if self.check_collision() == False:
                    self.position[1] += -SPEED * dt

            elif self.down_key_down == True:
                self.direction = 0

                # Only move if there is no collsion found.
                if self.check_collision() == False:
                    self.position[1] += SPEED * dt

    # This function handles calculating what amount the player needs to move.
    def _move_player(self, dt):
        if self.direction == 0:
            # Case: player needs to move more, until they are on / past the tile.
            if self.position[1] <= self._last_position[1] + 64:
                self.position[1] += SPEED * dt
                return (0, 0, -SPEED * dt)
            else:
                # Check if the player is stopping or keeps moving.
                self._last_position[1] = self._last_position[1] + 64
                self.position[1] = self._last_position[1]

                self._check_new_move_dir(dt)
                return (1, -self.position[0] + self._draw_position[0], -self.position[1] + self._draw_position[1])

        elif self.direction == 1:
            # Case: player needs to move more, until they are on / past the tile.
            if self.position[1] >= self._last_position[1] - 64:
                self.position[1] += -SPEED * dt
                return (0, 0, SPEED * dt)
            else:
                # Check if the player is stopping or keeps moving.
                self._last_position[1] = self._last_position[1] - 64
                self.position[1] = self._last_position[1]

                self._check_new_move_dir(dt)
                return (1, -self.position[0] + self._draw_position[0], -self.position[1] + self._draw_position[1])

        elif self.direction == 2:
            # Case: player needs to move more, until they are on / past the tile.
            if self.position[0] >= self._last_position[0] - 64:
                self.position[0] += -SPEED * dt
                return (0, SPEED * dt, 0)
            else:
                # Check if the player is stopping or keeps moving.
                self._last_position[0] = self._last_position[0] - 64
                self.position[0] = self._last_position[0]
                self._check_new_move_dir(dt)
                return (1, -self.position[0] + self._draw_position[0], -self.position[1] + self._draw_position[1])

        elif self.direction == 3:
            # Case: player needs to move more, until they are on / past the tile.
            if self.position[0] <= self._last_position[0] + 64:
                self.position[0] += SPEED * dt
                return (0, -SPEED * dt, 0)
            else:
                # Check if the player is stopping or keeps moving.
                self._last_position[0] = self._last_position[0] + 64
                self.position[0] = self._last_position[0]

                self._check_new_move_dir(dt)
                return (1, -self.position[0] + self._draw_position[0], -self.position[1] + self._draw_position[1])

    def check_movement(self, dt):
        if self._move == False:
            if self._current_animation == 1:
                self._current_animation = 2
            elif self._current_animation == 3:
                self._current_animation = 0

            # If a key is pressed, turn in that direction and start a timer.
            if self.left_key_down == True:
                # If player is already facing the direction they need to move, don't start timer.
                if self.direction != 2:
                    self._timer_on = True
                    self._timer_val = 0

                # Set move direction and start moving when timer is done.
                self.direction = 2
                self._move = True

                # Check for any collision.
                self.check_collision()

            elif self.right_key_down == True:
                # If player is already facing the direction they need to move, don't start timer.
                if self.direction != 3:
                    self._timer_on = True
                    self._timer_val = 0

                # Set move direction and start moving when timer is done.
                self.direction = 3
                self._move = True

                # Check for any collision.
                self.check_collision()

            elif self.up_key_down == True:
                # If player is already facing the direction they need to move, don't start timer.
                if self.direction != 1:
                    self._timer_on = True
                    self._timer_val = 0

                # Set move direction and start moving when timer is done.
                self.direction = 1
                self._move = True

                # Check for any collision.
                self.check_collision()

            elif self.down_key_down == True:
                # If player is already facing the direction they need to move, don't start timer.
                if self.direction != 0:
                    self._timer_on = True
                    self._timer_val = 0

                # Set move direction and start moving when timer is done.
                self.direction = 0
                self._move = True

                # Check for any collision.
                self.check_collision()

            return (0, 0, 0)  # No movement

        # Check again, in case the last bool check fired and swapped the value.  ACTGUALLY NOPE !!!!!!!!
        else:
            # Animate player movement.
            self._update_animation(dt)

            # Increase the timer by the amount of time passed.
            if self._timer_on == True:
                self._timer_val += dt
                #print self._timer_val

                # 120 ms or 0.12s is how long a direction key has to be pressed to start moving, not just direction turn.
                if self._timer_val >= 0.120:
                    # Turn off timer and flush it.
                    self._timer_on = False
                    self._timer_val = 0

                    # If the pressed key is up, don't move.
                    if self.direction == 2 and self.left_key_down == False:
                        self._move = False
                    elif self.direction == 3 and self.right_key_down == False:
                        self._move = False
                    elif self.direction == 0 and self.down_key_down == False:
                        self._move = False
                    elif self.direction == 1 and self.up_key_down == False:
                        self._move = False

                return (0, 0, 0)  # No movement
            else:
                # In this function the player is moved in a direction.
                return self._move_player(dt)

    def update(self, dt):
        # Check if the player should move, or moves the player.
        # output_offset holds the amount to move the scenes.
        output_offset = self.check_movement(dt)

        #print str(self.position)

        return output_offset
