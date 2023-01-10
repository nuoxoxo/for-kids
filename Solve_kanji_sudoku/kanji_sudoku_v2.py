"""
     //
   _'丶''丶'\
  (__/ \  _  _
     \  \/ \/ \
     (         )\
      \_______/  \
       [[] [[]
       [[] [[]
"""

"""
[
    ['丶', '丶', '丶',  '丶', '丶', '丶',  '丶', '丶', '丶'],
    ['丶', '丶', '丶',  '丶', '丶', '丶',  '丶', '丶', '丶'],
    ['丶', '丶', '丶',  '丶', '丶', '丶',  '丶', '丶', '丶'],

    ['丶', '丶', '丶',  '丶', '丶', '丶',  '丶', '丶', '丶'],
    ['丶', '丶', '丶',  '丶', '丶', '丶',  '丶', '丶', '丶'],
    ['丶', '丶', '丶',  '丶', '丶', '丶',  '丶', '丶', '丶'],

    ['丶', '丶', '丶',  '丶', '丶', '丶',  '丶', '丶', '丶'],
    ['丶', '丶', '丶',  '丶', '丶', '丶',  '丶', '丶', '丶'],
    ['丶', '丶', '丶',  '丶', '丶', '丶',  '丶', '丶', '丶']
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
# search for '丶'-marked square
# return the top-left most one
#

def find_next_move(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == '丶':
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
    if r is None: # solved if board has no '丶'
        return True 
    for guess in arr:
        if Brain(puzzle, guess, r, c):
            puzzle[r][c] = guess # btk guess
            if solver(puzzle): # btk recurse
                return True
        # backtrack reset
        puzzle[r][c] = '丶'
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
        [W, '丶', '丶',  '丶', '丶', '丶',  '丶', '丶', S],
        ['丶', Y, '丶',  '丶', P, '丶',  W, '丶', '丶'],
        [P, '丶', '丶',  '丶', '丶', '丶',  '丶', Y, J],

        ['丶', L, W,  P, '丶', Q,  Y, '丶', D],
        [J, '丶', '丶',  Y, '丶', D,  '丶', '丶', P],
        [Y, '丶', D,  X, '丶', L,  S, J, '丶'],

        [D, Q, '丶',  '丶', '丶', '丶',  '丶', '丶', Y],
        ['丶', '丶', J,  '丶', D, '丶',  '丶', Q, '丶'],
        [L, '丶', '丶',  '丶', '丶', '丶',  '丶', '丶', W]
    ]
    
    Game_1 = [
        ['丶', '丶', '丶',  P, '丶', '丶',  S, '丶', '丶'],
        ['丶', P, X,  Y, S, '丶',  '丶', W, '丶'],
        [S, '丶', W,  '丶', '丶', Q,  '丶', '丶', '丶'],

        [P, D, S,  L, '丶', X,  '丶', '丶', '丶'],
        ['丶', '丶', '丶',  '丶', '丶', '丶',  '丶', '丶', '丶'],
        ['丶', '丶', '丶',  Q, '丶', W,  L, D, S],

        ['丶', '丶', '丶',  W, '丶', '丶',  Y, '丶', D],
        ['丶', Y, '丶',  '丶', Q, D,  X, S, '丶'],
        ['丶', '丶', L,  '丶', '丶', Y,  '丶', '丶', '丶']
    ]

    Game_2 = [
        ['丶', J, '丶',  '丶', '丶', '丶',  '丶', '丶', D],
        ['丶', P, W,  '丶', '丶', S,  '丶', Q, '丶'],
        ['丶', Y, '丶',  '丶', D, X,  '丶', '丶', L],

        ['丶', '丶', '丶',  '丶', '丶', '丶',  D, '丶', S],
        ['丶', D, '丶',  '丶', J, '丶',  '丶', L, '丶'],
        [L, '丶', P,  '丶', '丶', '丶',  '丶', '丶', '丶'],

        [S, '丶', '丶',  Q, W, '丶',  '丶', X, '丶'],
        ['丶', Q, '丶',  P, '丶', '丶',  S, J, '丶'],
        [P, '丶', '丶',  '丶', '丶', '丶',  '丶', D, '丶']
    ]

    Game_3 = [
        ['丶', X, Q,  S, Y, '丶',  '丶', '丶', '丶'],
        ['丶', '丶', '丶',  '丶', '丶', '丶',  '丶', '丶', '丶'],
        [L, '丶', '丶',  '丶', J, '丶',  P, '丶', S],

        ['丶', L, Y,  '丶', '丶', '丶',  '丶', S, '丶'],
        [S, '丶', '丶',  '丶', D, '丶',  '丶', '丶', W],
        ['丶', '丶', '丶',  '丶', '丶', '丶',  X, J, '丶'],

        [W, '丶', L,  '丶', S, '丶',  '丶', '丶', D],
        ['丶', '丶', '丶',  '丶', '丶', '丶',  '丶', '丶', '丶'],
        ['丶', '丶', '丶',  '丶', L, J,  W, X, '丶']
    ]

    def Counting(): # hack c++ static int
        Counting.i += 1
    Counting.i = 0

    def SolveGame(Game):
        Counting()
        print(f'Game {Counting.i}')
        PrintGrid(Game)
        solver(Game)
        PrintGrid(Game)

    SolveGame(Game_0)
    SolveGame(Game_1)
    SolveGame(Game_2)
    SolveGame(Game_3)
