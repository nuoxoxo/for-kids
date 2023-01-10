"""
[
    [0, 0, 0,  0, 0, 0,  0, 0, 0],
    [0, 0, 0,  0, 0, 0,  0, 0, 0],
    [0, 0, 0,  0, 0, 0,  0, 0, 0],

    [0, 0, 0,  0, 0, 0,  0, 0, 0],
    [0, 0, 0,  0, 0, 0,  0, 0, 0],
    [0, 0, 0,  0, 0, 0,  0, 0, 0],

    [0, 0, 0,  0, 0, 0,  0, 0, 0],
    [0, 0, 0,  0, 0, 0,  0, 0, 0],
    [0, 0, 0,  0, 0, 0,  0, 0, 0]
]
"""

S = '四'
W = '五'
L = '六'
Q = '七'
J = '九'
P = '平'
Y = '月'
D = '大'
X = '小'

arr = [S, W, L, Q, J, P, Y, D, X]



def next_move(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r, c
    return None, None



def move_is_valid(puzzle, guess, R, C): 

    guessed_row = puzzle[R] # check current row

    if guess in guessed_row:
        return False

    guessed_col = [puzzle[i][C] for i in range(9)] # check current col

    if guess in guessed_col:
        return False

    # check 3x3 grid
    grid_row_start = (R // 3) * 3
    grid_col_start = (C // 3) * 3

    for r in range(grid_row_start, grid_row_start + 3):
        for c in range(grid_col_start, grid_col_start + 3):
            if puzzle[r][c] == guess: # unsolved
                return False
    return True



def solver(puzzle):
    r, c = next_move(puzzle)
    if r is None:
        return True

    for guess in arr:  
        if move_is_valid(puzzle, guess, r, c):
            puzzle[r][c] = guess
            if solver(puzzle):
                return True
        # backtrack
        puzzle[r][c] = 0
    return False



def PrintGrid(Game):
    for r in range(9):
        for c in range(9):
            print(Game[r][c], end=' ')
        print()
    print()



def Play(No, Game):
    print(f'Game {No}')
    PrintGrid(Game)
    solver(Game)
    PrintGrid(Game)
    
    # pprint(Game_0)
    # print()
    # print(solver(Game_0))
    # print()
    # pprint(Game_0)
    # print()

# D R I V E
if __name__ == '__main__':

    Game_0 = [
        [W, 0, 0,  0, 0, 0,  0, 0, S],
        [0, Y, 0,  0, P, 0,  W, 0, 0],
        [P, 0, 0,  0, 0, 0,  0, Y, J],

        [0, L, W,  P, 0, Q,  Y, 0, D],
        [J, 0, 0,  Y, 0, D,  0, 0, P],
        [Y, 0, D,  X, 0, L,  S, J, 0],

        [D, Q, 0,  0, 0, 0,  0, 0, Y],
        [0, 0, J,  0, D, 0,  0, Q, 0],
        [L, 0, 0,  0, 0, 0,  0, 0, W]
    ]
    
    Game_1 = [
        [0, 0, 0,  P, 0, 0,  S, 0, 0],
        [0, P, X,  Y, S, 0,  0, W, 0],
        [S, 0, W,  0, 0, Q,  0, 0, 0],

        [P, D, S,  L, 0, X,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  Q, 0, W,  L, D, S],

        [0, 0, 0,  W, 0, 0,  Y, 0, D],
        [0, Y, 0,  0, Q, D,  X, S, 0],
        [0, 0, L,  0, 0, Y,  0, 0, 0]
    ]

    Game_2 = [
        [0, J, 0,  0, 0, 0,  0, 0, D],
        [0, P, W,  0, 0, S,  0, Q, 0],
        [0, Y, 0,  0, D, X,  0, 0, L],

        [0, 0, 0,  0, 0, 0,  D, 0, S],
        [0, D, 0,  0, J, 0,  0, L, 0],
        [L, 0, P,  0, 0, 0,  0, 0, 0],

        [S, 0, 0,  Q, W, 0,  0, X, 0],
        [0, Q, 0,  P, 0, 0,  S, J, 0],
        [P, 0, 0,  0, 0, 0,  0, D, 0]
    ]

    Game_3 = [
        [0, X, Q,  S, Y, 0,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
        [L, 0, 0,  0, J, 0,  P, 0, S],

        [0, L, Y,  0, 0, 0,  0, S, 0],
        [S, 0, 0,  0, D, 0,  0, 0, W],
        [0, 0, 0,  0, 0, 0,  X, J, 0],

        [W, 0, L,  0, S, 0,  0, 0, D],
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  0, L, J,  W, X, 0]
    ]
    Play(0, Game_0)
    Play(1, Game_1)
    Play(2, Game_2)
    Play(3, Game_3)
