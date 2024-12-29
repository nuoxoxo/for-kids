"""
g = [
    '丶丶丶丶丶丶丶丶丶',
    '丶丶丶丶丶丶丶丶丶',
    '丶丶丶丶丶丶丶丶丶',
    '丶丶丶丶丶丶丶丶丶',
    '丶丶丶丶丶丶丶丶丶',
    '丶丶丶丶丶丶丶丶丶',
    '丶丶丶丶丶丶丶丶丶',
    '丶丶丶丶丶丶丶丶丶',
    '丶丶丶丶丶丶丶丶丶'
]
gg = [''.join(_) for _ in g]
for l in gg: print(l)
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

d = {}
dot = '.'
chinesedot = '｀'#'＿'#'丶'
d['四'] = 'S'
d['五'] = 'W'
d['六'] = 'L'
d['七'] = 'Q'
d['九'] = 'J'
d['平'] = 'P'
d['月'] = 'Y'
d['大'] = 'D'
d['小'] = 'X'
d['丶'] = dot
d['S'] = S
d['W'] = W
d['L'] = L#'六'
d['Q'] = Q#'七'
d['J'] = J#'九'
d['P'] = P#'平'
d['Y'] = Y#'月'
d['D'] = D#'大'
d['X'] = X#'小'
d[dot] = chinesedot
d[chinesedot] = dot

#
# search for '丶'-marked square
# return the top-left most one
#

def find_next_move(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == dot:
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

gg, yy, cc, rest, nl = '\033[32m', '\033[33m', '\033[36m', '\033[0m', '\n'
def yellow(s: str) -> str: return yy + s + rest
def green(s: str) -> str: return gg + s + rest
def cyan(s: str) -> str: return cc + s + rest

def PrintGrid(Game,original_grid=None):
    for r in range(9):
        for c in range(9):
            char = Game[r][c]
            tchar = d[Game[r][c]]
            #if original_grid: print('dbg/', char, '-', original_grid[r][c])
            if original_grid and char != original_grid[r][c]:
                print( green( char ), end='')
            else:
                print( tchar, end='')
        print()
    print()

# D R I V E
if __name__ == '__main__':
    
    Game_0 = [
        'W.......S',
        '.Y..P.W..',
        'P......YJ',
        '.LWP.QY.D',
        'J..Y.D..P',
        'Y.DX.LSJ.',
        'DQ......Y',
        '..J.D..Q.',
        'L.......W',
    ]
    
    Game_1 = [
        '...P..S..',
        '.PXYS..W.',
        'S.W..Q...',
        'PDSL.X...',
        '.........',
        '...Q.WLDS',
        '...W..Y.D',
        '.Y..QDXS.',
        '..L..Y...',
    ]

    Game_2 = [
        '.J......D',
        '.PW..S.Q.',
        '.Y..DX..L',
        '......D.S',
        '.D..J..L.',
        'L.P......',
        'S..QW..X.',
        '.Q.P..SJ.',
        'P......D.',
    ]

    Game_3 = [
        '.XQSY....',
        '.........',
        'L...J.P.S',
        '.LY....S.',
        'S...D...W',
        '......XJ.',
        'W.L.S...D',
        '.........',
        '....LJWX.',
    ]

    def count(): # hack c++ static int
        count.i += 1
    count.i = 0

    """
    #for game in [Game_0,Game_1,Game_2,Game_3]:
    for game in [Game_0,Game_1,Game_2,Game_3]:
        for line in game:
            line = [d[_] for _ in line]
            print(f"'{''.join(line)}',")
        print(222)
    """

    def SolveGame(G):
        count()
        print(f'Game {count.i}')
        Game = [[c for c in line] for line in G]
        original_grid = [_[:]for _ in Game]
        PrintGrid(Game)
        solver(Game)
        PrintGrid(Game,original_grid)
        print('from/')
        PrintGrid(original_grid)

    SolveGame(Game_0)
    SolveGame(Game_1)
    SolveGame(Game_2)
    SolveGame(Game_3)
