import math
import time
from Player import HumanPlayer, RandomComputerPlayer
class TicTacToe:                         # going to create game
    def __init__(self):                  # need a board for play.
        self.board = self.make_board()
        self.curret_winner = None         # keep track of winner.

    @staticmethod
    def make_board():
        return [' ' for _  in range(9)]
    
    def print_board(self):
        for row in[self.board[i*3(i+1) *3]for i in range(3)]:
            print('| ' + ' | '.join(self.board) + ' |')
    
    @staticmethod
    def print_board_num():                             #print bord numbers
        number_board = [[str(i)for i in range(j*3, (j+1)*3)for j in range(3)]]
        for row in number_board:
            print('| '+' | '.join(row)+ ' |')
    
    def avilable_moves(self):
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
        return moves 
    def empty_squares(self):
        return self.board
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square,letter):
                self.curret_winner = letter
            return True
        return False
    def winner(self, square, letter):
        # check all possibilities

        #check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([s == letter for s in row]):
            return True

        #check the column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True

        #check the digonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True
        return False

def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.empty_squares()
    
    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.getmove(game)
        else:
            square = x_player.getmove(game)
        # define make move. when we make a move, we need information about what square the user wats their move to be at.
        # and what letter the player is?
        if game.make_move(square, letter):
            
            if print_game:
                print(letter + f'makes a move to square {square}')
                game.print_board()
                print('') # an empty line
                # find winner
            if game.current_winner:
                if print_game:
                    print(letter + "winns !")
                    return letter  # ends the loop and exits the game.
            letter = 'O' if letter == 'X' else 'X' # switches player

        time.sleep(.8)
    if print_game:
        print("It\'s a tie")
    
