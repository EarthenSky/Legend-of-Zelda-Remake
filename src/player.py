'''This is the player, who moves and is animated.  Movement is a little complicated.'''

import sys
import pygame

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
        return False
        global g_outside_tilemap

        if g_current_scene == OUTSIDE:
            pass

        tilex, tiley = g_outside_tilemap.get_tile(round(position.x/64), round(position.y/64))

        if tilex == 10:
            # Stop movement.
            pass
            print "stawp"

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

            if self.direction == 0:
                # Player has stopped so flush the position values.
                self.position[1] = self._last_position[1]
                print "FLUSH"

            elif self.direction == 1:
                # Hit tile so flush the position values.
                self.position[1] = self._last_position[1]
                print "FLUSH"

            elif self.direction == 2:
                # Hit tile so flush the position values.
                self.position[0] = self._last_position[0]
                print "FLUSH"

            elif self.direction == 3:
                # Hit tile so flush the position values.
                self.position[0] = self._last_position[0]
                print "FLUSH"

        else:
            # If a key is pressed, turn in that direction, don't start a timer.  Start moving.
            if self.left_key_down == True:
                if self.direction != 2:
                    # Turned direction so flush the position values.
                    self.position[0] = self._last_position[0]
                    print "FLUSH"

                self.direction = 2
                self.position[0] += -SPEED * dt

            elif self.right_key_down == True:
                if self.direction != 3:
                    # Turned direction so flush the position values.
                    self.position[0] = self._last_position[0]
                    print "FLUSH"

                self.direction = 3
                self.position[0] += SPEED * dt

            elif self.up_key_down == True:
                if self.direction != 1:
                    # Turned direction so flush the position values.
                    self.position[1] = self._last_position[1]
                    print "FLUSH"

                self.direction = 1
                self.position[1] += -SPEED * dt

            elif self.down_key_down == True:
                if self.direction != 0:
                    # Turned direction so flush the position values.
                    self.position[1] = self._last_position[1]
                    print "FLUSH"

                self.direction = 0
                self.position[1] += SPEED * dt

            self.check_collision()

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
                self._check_new_move_dir(dt)
                return (1, -self.position[0] + self._draw_position[0], -self.position[1] + self._draw_position[1])

    def update(self, dt):
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

            elif self.right_key_down == True:
                # If player is already facing the direction they need to move, don't start timer.
                if self.direction != 3:
                    self._timer_on = True
                    self._timer_val = 0

                # Set move direction and start moving when timer is done.
                self.direction = 3
                self._move = True

            elif self.up_key_down == True:
                # If player is already facing the direction they need to move, don't start timer.
                if self.direction != 1:
                    self._timer_on = True
                    self._timer_val = 0

                # Set move direction and start moving when timer is done.
                self.direction = 1
                self._move = True

                print "next1"

            elif self.down_key_down == True:
                # If player is already facing the direction they need to move, don't start timer.
                if self.direction != 0:
                    self._timer_on = True
                    self._timer_val = 0

                # Set move direction and start moving when timer is done.
                self.direction = 0
                self._move = True

                print "next1"

            else:
                return (0, 0, 0)  # No movement

        # Check again, in case the last bool check fired and swapped the value.
        if self._move == True:
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
