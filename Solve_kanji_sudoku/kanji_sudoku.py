"""
     //
   _00\
  (__/ \  _  _
     \  \/ \/ \
     (         )\
      \_______/  \
       [[] [[]
       [[] [[]
"""

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

#
# search for 0-marked square
# return the top-left most one
#

def find_next_move(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r, c
    return None, None

#
# brain
#

def Brain(puzzle, guess, R, C): 

    guessed_row = puzzle[R]
    if guess in guessed_row: # check dup in current row
        return False

    guessed_col = [puzzle[i][C] for i in range(9)]
    if guess in guessed_col: # check dup in same col
        return False

    r = (R // 3) * 3
    c = (C // 3) * 3 # check the 3x3 where {R, C} is 
    for rr in range(r, r + 3):
        for cc in range(c, c + 3):
            if guess == puzzle[rr][cc]:
                return False
    return True



def solver(puzzle):
    r, c = find_next_move(puzzle)
    if r is None: # solved if board has no 0
        return True 
    for guess in arr:
        if Brain(puzzle, guess, r, c):
            puzzle[r][c] = guess # btk guess
            if solver(puzzle): # btk recurse
                return True
        # backtrack reset
        puzzle[r][c] = 0
    return False



def PrintGrid(Game):
    for r in range(9):
        for c in range(9):
            print(Game[r][c], end=' ')
        print()
    print()

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

    def Index(): # hack c++ static int
        Index.i += 1
    Index.i = 0

    def SolveGame(Game):
        print(f'Game {Index.i}')
        PrintGrid(Game)
        solver(Game)
        PrintGrid(Game)

    SolveGame(Game_0)
    SolveGame(Game_1)
    SolveGame(Game_2)
    SolveGame(Game_3)
