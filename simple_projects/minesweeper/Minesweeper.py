import random

# lets create a board object to represent the minesweeper game


class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        #let's crate the board
        self.board = self.make_new_board()

        #initialize a set to keep track of which location we have uncovered
        #we will save (row, cal) tuples into this set
        self.dug = set()

    def make_new_board(self):
        #cunstruct a new board based on the dim_size and num_bombs
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # this crate an array:
        #[[Non, Non,.....,Non],
        # [Non, Non,.....,Non]
        # [Non, Non,..... Non]]

        #plant bombs
        bombs_planed = 0
        while bombs_planed < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size
            
            if board[row][col] == '*':
                #already existing a bomb
                continue

            board[row][col] = '*' #planing a bomb
            bombs_planed += 1
            
        return board



def Play(dim_size = 10, num_bombs = 10):
    pass