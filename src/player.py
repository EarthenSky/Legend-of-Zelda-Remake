'''This is the player, who moves and is animated.'''
class Player:

    def __init__(self, start_position):
        self.position = start_position

        # The value of the current frame of the player's animation.
        self._current_animation = 0

        # The direction the player is facing.  Up, right, down, left is 0, 1, 2, 3.
        self.direction = 0

    # Moving and stuff.
    def handle_input(self):
        pass

    def draw(self):
        pass

    def update(self, dt):
        pass
