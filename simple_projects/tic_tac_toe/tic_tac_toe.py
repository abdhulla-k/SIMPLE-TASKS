# going to create a design for tic tac toe

def make_board(values):
    print(' ____   ____   ____')
    print('\n')
    print('| {}  |  {}  |  {}  |'.format(values[0], values[1], values[2]))
    print(' ____   ____   ____')
    print('\n')
    print('| {}  |  {}  |  {}  |'.format(values[3], values[4], values[5]))
    print(' ____   ____   ____')
    print('\n')
    print('| {}  |  {}  |  {}  |'.format(values[6], values[7], values[8]))
    print(' ____   ____   ____')

def score_board(score_board):
    print("\n\t         SCOREBOARD       ")
    print("\t==============================")
 
    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])
 
    print("\t==============================\n")

# values are below
# want remember the past and prescent moves of player
def move(cur_player):
    values = [' ' for x in range(9)]
    player_pse = {'x':[], 'o':[]}

    while True:
        make_board(values)
        # exepting an error
        # if a player enters unintended value
        try:
            print("player ", cur_player +"turn. which box? : ", end="")
            move(int(input()))
        # check the input. is it currect or not?
        except ValueError:
            print('wring input!! Try again')
            continue
        # check if the box is not sccupied olready
        if move < 1 or move < 9:
            print('wring input!!  Try again')
            continue

if __name__ == "__main__":

    print('player 1')
    player1 = print(input('enter the name:'))
    print('\n')
    print('playar 2')
    player2 = print(input('enter the name:'))
    print('\n')
    
    current_player = player1
    player_choice = {"x" : "", "o" : ""}
    options = ['x', 'o']
 
    scoreBoard = {player1: 0, player2: 0}
    score_board(scoreBoard)

    # going to create game loop
    
    while True:
        #playar choice menu
        print("Turn to choose for "+ current_player)
        print("Enter 1 for 'x' \nEnter 2 for 'o' \nEnter 3 for Quite game")
        
        try:
            Choice = int(input())
        except ValueError:
            print('wrong input!!  Try again')
            continue
        #conditions
        if Choice == 1:
            player_choice ['x'] = current_player
            if current_player == player1:
                player_choice ['o'] = player2
            else:
                player_choice ['o'] = player1
        
        elif Choice == 2:
            player_choice ['o'] = current_player
            if current_player == player1:
                player_choice['x'] = player1
            else:
                player_choice ['x'] = player2
        
        elif Choice == 3:
            print('final scores')
            score_board(scoreBoard)
            break




