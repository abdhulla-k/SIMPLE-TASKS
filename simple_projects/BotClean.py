def next_move(posr,posc,board):

    # going to find all positions to clean
    WaystPlaces = []
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'd':
                place = [i,j]
                WaystPlaces.append(place)
    PositionBot = [posr,posc]        # bot position

    def MakeMove(PositionBot,CurrentLenI,CurrentLenJ,LhsOrRhs):
        for i in range(CurrentLenI):
            print('DOWN')
        if CurrentLenJ == 0:
            print('CLEAR')
        if LhsOrRhs == -1:
            for i in range(CurrentLenJ):
                print('LEFT')
            print('CLEAR')
        elif LhsOrRhs == 0:
            for i in range(CurrentLenJ):
                print('CLEAR')
        elif LhsOrRhs == 1:
            for i in range(CurrentLenJ):
                print('RIGHT')
            print('CLEAR')


    def FindDistance(PositionBot,waystPlaces):
        for i in range(5):
           for j in range(5):
               if [i,j] in waystPlaces:
                   LhsOrRhs = 0
                   CurrentLenI = abs(i - PositionBot[0])# distance between bot space and waystPlace in i
                   CurrentLenJ = abs(j - PositionBot[1])# distance between bot space and waystPlace in j
                   if PositionBot[1] > j:
                       LhsOrRhs = -1
                   elif PositionBot[1] == j:
                       LhsOrRhs = 0
                   else:
                       LhsOrRhs = 1
                   MakeMove(PositionBot,CurrentLenI,CurrentLenJ,LhsOrRhs)  # called PrintMove function
                   PositionBot = [i,j]


    FindDistance(PositionBot,WaystPlaces)
    
            






















game = [
    ['-', 'b', '-', 'd', '-'],
    ['-', 'd', '-', '-', '-'],
    ['-', '-', '-', 'd', '-'],
    ['-', 'd', '-', '-', 'd'],
    ['d', '-', '-', '-', '-']   
]
game2 = [
    ['b', 'd', '-', '-', '-'],
    ['-', 'd', '-', '-', '-'],
    ['-', '-', '-', 'd', '-'],
    ['-', '-', '-', 'd', '-'],
    ['-', '-', 'd', '-', 'd']   
]
next_move(0,0,game2)