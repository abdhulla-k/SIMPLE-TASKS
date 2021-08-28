def find_next_empty(puzzle):
    # find next row and col on the puzzle that's not filled yet --> rep with -1
    # return row, col = non, non if there is not an empty space
    for r in range(9): # 9 == 0, 1, 2, ................ , 8.
        for c in range(9):
            if puzzle [r][c] == -1:
                return -1
    
    return None, None # there is not an empty space

def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is valid or guess
    # return True if is valid, False otherwise

    # incase of row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # incase of col

    # col_val = []
    # for i in range(9):
    #    col_val.append(puzzle[i][col]).  an another way is used below
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    # incase of square
    # figures out where the 3x3 square starts
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    # iterate over the 3 values in the row/column
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if guess == puzzle[r][c]:
                return False
    
    return True

def solve_sudoku(puzzle):
    # solve sudoku using backtracking
    # step 1: choose somewhere on the puzzle to make a guess.
    row, col = find_next_empty(puzzle)

    # if there's nowhere left
    if row == None:
        return True # becouse we've actually solved our puzle.
    
    # if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            # if this is valid, then placd that guess on puzzle
            puzzle[row][col] = guess
            # recursively call our function
            if solve_sudoku(puzzle):
                return True
        
        # if not valid or our guess does not solve the puzzle, then we need to  backtrack and try a new number
        puzzle[row][col] = -1
    
    # if non of the numbers that we try work, then we puzzle is unsolvable
    return False


