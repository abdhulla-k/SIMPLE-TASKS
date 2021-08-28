def find_next_empty(puzzle):
    # find next row and col on the puzzle that's not filled yet --> rep with -1
    # return row, col = non, non if there is not an empty space
    for r in range(9): # 9 == 0, 1, 2, ................ , 8.
        for c in range(9):
            if puzzle [r][c] == -1:
                return -1
    
    return None, None # there is not an empty space

def solve_sudoku(puzzle):
    # solve sudoku using backtracking
    # step 1: choose somewhere on the puzzle to make a guess.
    row, col = find_next_empty(puzzle)
