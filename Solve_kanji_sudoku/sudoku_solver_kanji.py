arr = ['S', 'W', 'L', 'Q', 'J', 'P', 'Y', 'D', 'X']
void = '.'
charset = {}
charset['S'] = '四'
charset['W'] = '五'
charset['L'] = '六'
charset['Q'] = '七'
charset['J'] = '九'
charset['P'] = '平'
charset['Y'] = '月'
charset['D'] = '大'
charset['X'] = '小'
charset[void] = '｀'#'＿''丶'

def find_next_move(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == void:
                return r, c
    return None, None

def Brain(puzzle, poss, R, C): 
    if poss in puzzle[R]:
        return False
    if poss in [row[C] for row in puzzle]:
        return False
    r, c = (R // 3) * 3, (C // 3) * 3
    for rr in range(r, r + 3):
        for cc in range(c, c + 3):
            if poss == puzzle[rr][cc]:
                return False
    return True

def solvegame(puzzle):
    r, c = find_next_move(puzzle)
    if r is None:
        return True 
    for poss in arr:
        if Brain(puzzle, poss, r, c):
            puzzle[r][c] = poss
            if solvegame(puzzle):
                return True
            puzzle[r][c] = void#'丶'
    return False

gg, yy, cc, rest, nl = '\033[32m', '\033[33m', '\033[36m', '\033[0m', '\n'
def yellow(s: str) -> str: return yy + s + rest
def green(s: str) -> str: return gg + s + rest
def cyan(s: str) -> str: return cc + s + rest

def printgame(Game,src_grid=None):
    for r in range(9):
        for c in range(9):
            char = Game[r][c]
            if src_grid and Game[r][c] != src_grid[r][c]:
                print( green( charset[char] ), end='')
            else:
                print( charset[char], end='')
        print()
    print()

if __name__ == '__main__':
    
    stringlist_0 = [
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
    
    stringlist_1 = [
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

    stringlist_2 = [
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

    stringlist_3 = [
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

    def count():
        count.i += 1
    count.i = 0

    def solver(stringlist):
        count()
        print(f'Game {count.i} {'-'*21}\n')
        game = [[c for c in line] for line in stringlist]
        src_grid = [_[:]for _ in game]
        printgame( game )
        solvegame( game )
        printgame( game, src_grid )

    for sl in [
        stringlist_0,
        stringlist_1,
        stringlist_2,
        stringlist_3,
    ]: solver( sl )

