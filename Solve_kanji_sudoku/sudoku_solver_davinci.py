arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
void = '.'
charset = {}
charset['5'] = '⊙'#平'
charset['6'] = '◠'#月'
charset['7'] = '♅'#大'
charset['8'] = '🜱'#小'
charset['0'] = '♁'#四'
charset['1'] = '♃'#五'
charset['2'] = '🜘'#六'
charset['3'] = '🜻'#七'
charset['4'] = '🜥'#九'
charset[void] = ' '#'＿''丶'

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
                print( green( charset[char] ), end=' ')
            else:
                print( charset[char], end=' ')
        print()
    print()

if __name__ == '__main__':
    
    stringlist_0 = [
        '1.......0',
        '.6..5.1..',
        '5......64',
        '.215.36.7',
        '4..6.7..5',
        '6.78.204.',
        '73......6',
        '..4.7..3.',
        '2.......1',
    ]
    
    stringlist_1 = [
        '...5..0..',
        '.5860..1.',
        '0.1..3...',
        '5702.8...',
        '.........',
        '...3.1270',
        '...1..6.7',
        '.6..3780.',
        '..2..6...',
    ]

    stringlist_2 = [
        '.4......7',
        '.51..0.3.',
        '.6..78..2',
        '......7.0',
        '.7..4..2.',
        '2.5......',
        '0..31..8.',
        '.3.5..04.',
        '5......7.',
    ]

    stringlist_3 = [
        '.8306....',
        '.........',
        '2...4.5.0',
        '.26....0.',
        '0...7...1',
        '......84.',
        '1.2.0...7',
        '.........',
        '....2418.',
    ]

    def count():
        count.i += 1
    count.i = 0

    def solver(stringlist):
        count()
        print(f'Game {count.i} {'-'*10}\n')
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

