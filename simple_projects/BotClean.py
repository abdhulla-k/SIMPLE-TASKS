def next_move(posr,posc,board):

    # going to find all positions to clean
    WaystPlaces = []
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'd':
                place = [i,j]
                WaystPlaces.append(place)
    PositionBot = [posr,posc]        # bot position

    def MakeMove(PositionBot,CurrentLenI,CurrentLenJ):
        pass


    def FindDistance(PositionBot,waystPlaces):
        print(waystPlaces)
        for i in range(5):
           for j in range(5):
               if [i,j] in waystPlaces:
                   print('positionBot is: '+str(PositionBot))
                   print([i,j])
                   CurrentLenI = abs(i - PositionBot[0])# distance between bot space and waystPlace in i
                   CurrentLenJ = abs(j - PositionBot[1])# distance between bot space and waystPlace in j
                   print(str(i)+'-'+str(PositionBot[0]))
                   print(CurrentLenI)
                   print('j')
                   print(str(j)+'-'+str(PositionBot[1]))
                   print(CurrentLenJ)
                   MakeMove(PositionBot,CurrentLenI,CurrentLenJ)  # called PrintMove function
                   PositionBot = [i,j]


    FindDistance(PositionBot,WaystPlaces)
            






















game = [
    ['-', 'b', '-', 'd', '-'],
    ['-', 'd', '-', '-', '-'],
    ['-', '-', '-', 'd', '-'],
    ['-', 'd', '-', '-', 'd'],
    ['d', '-', '-', '-', '-']   
]
next_move(0,1,game)