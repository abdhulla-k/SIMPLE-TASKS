import random

# lets create a board object to represent the minesweeper game


class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        #let's crate the board
        self.board = self.make_new_board()
        self.assign_values_to_board()

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
                #already existing a bomb. keep goning
                continue

            board[row][col] = '*' #planing a bomb
            bombs_planed += 1
            
        return board
    
    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board [r][c] == '*':
                    continue
                self.board [r][c] = self.get_num_neighboring_bombs(r,c)
    
    def get_num_neighboring_bombs(self, row, col):
        # let's iterate through each of the neighboring positions and sum number of bombs
        #top left: (row - 1, col - 1) , top middle: (row - 1, col) , top right: (row - 1, col + 1)
        #left: (row, col - 1) , right: (row, col+1 )
        #bottom left: ( row + 1, col - 1) , bottom middle: (row + 1, col) , bottom right: (row + 1, col + 1)

        number_neighber_bombs = 0
        for r in range(max(0,row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(1,col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:#our position
                    continue
                if self.board [r][c] == '*':
                    number_neighber_bombs += 1
                    
        return number_neighber_bombs
    
    def dig(self, row, col ):    # keep tracking
        # dig at the location
        # return True if successful dig, False if bomb dig
        self.dug.add((row,col))
        # a few scenarios:
        # hit a bomb. then game over
        if self.board[row][col] == '*':
            return False
        # dig at location with neighboring bombs 
        elif self.board[row][col] > 0:
            return True
        # dig at location with no neigboring boms
        
        for r in range(max(0,row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(1,col-1), min(self.dim_size-1, col+1)+1):
                if (r,c) in self.dug:
                    continue
                self.dig(r,c)
        
        return True
    
    def __str__(self):
        # firs let's crate a new array that represent what the user would see
        visible_board = [[None for i in range(self.dim_size)] for None in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                     visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        
        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep
                

            

def Play(dim_size = 10, num_bombs = 10):
    #create the board and plant the bombs
    board = Board(dim_size, num_bombs)