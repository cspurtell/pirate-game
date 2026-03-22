class GameState:
    def __init__(self, player, world, current_location):
        self.player = player
        self.world = world
        self.current_location = current_location
        self.day = 1

    def move_to(self, location):
        self.current_location = location
        self.day += 1