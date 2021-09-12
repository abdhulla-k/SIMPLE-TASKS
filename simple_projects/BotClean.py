def next_move(i,j,board):
    WaystPlaces = []
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'b':
                place = [i,j]
                WaystPlaces.append(place)





















game = [
    ['-', 'b', '-', 'd', '-'],
    ['-', 'd', '-', '-', '-'],
    ['-', '-', '-', 'd', '-'],
    ['-', 'd', '-', '-', 'd'],
    ['d', '-', '-', '-', '-']   
]
next_move(0,1,game)