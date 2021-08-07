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
