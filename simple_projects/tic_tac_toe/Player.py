import math
import random

class player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self):
        pass
class HumanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move(0-9): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('invalid square. Try again')
            return val

class RandomComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.avilable_moves())
        return square