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

