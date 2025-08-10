import collections, re, math
Green,Yello,Mage,Cyan,Rest = ['\033[1;32m','\033[1;33m','\033[31m','\033[36m','\033[0m']

def cutter(line) -> tuple:
    l,r = parser( line )
    for k,v in r.items(): l[k] -= v
    for k,v in l.items(): l[k] = round(v,7)
    polydegree = sorted(l.keys(), reverse=True)[0]
    assert polydegree > -1

    res = []
    for k,v in sorted(l.items()):
        w = int(v) if v == int(v) else v
        sign = '-' if w < 0 else '+'
        res.append( f'{sign} {abs(w)} * X^{k}' )
    res = ' '.join(res)
    if res.startswith('+ '):
        res = res[2:]
    elif res.startswith('- '):
        res = '-' + res[2:]

    _solutions = [None, None]
    _gt2 = 'The polynomial degree is strictly greater than 2, I can\'t solve.'
    _anyrealnum = 'Any real number is a solution.'
    _nosolution = 'No solution.'
    _2slns = 'Discriminant is strictly ..., the two|one solution|s are:\n.../1\n.../2'
    #_solvable = True ### XXX

    res_reduced_form = f'Reduced form: {res} = 0'
    res_polydegree = '' if polydegree == 0 else f'Polynomial degree: {polydegree}\n'
    if polydegree > 2:
        res_polydegree += _gt2
        #_solvable = False ### XXX
    elif polydegree == 0:
        #_solvable = False ### XXX
        if l[0] == 0:
            res_polydegree += _anyrealnum
        else:
            res_polydegree += _nosolution
    elif polydegree == 1: # linear
        print(f'{Yello}L I N E A R{Rest} !!!')
        _solutions[0] = round(-c / b,7)
    else:
        res_polydegree += _2slns ### TODO : might have only 1 soln
        a,b,c = l[2],l[1],l[0]
        D = b*b - 4*a*c
        if D < 0:
            print( f'Discriminant is strictly {Yello}negative{Rest}, \
the {Yello}two{Rest} complex solutions are:' )
        elif a != 0:
            DSR = math.sqrt(D)
            _solutions = [round(-b + _,7) / (2 * a) for _ in [DSR, -DSR]]
            print(f'a > 0 :: solutions/{Yello}', _solutions, Rest)

    return ( res_reduced_form, res_polydegree, )#_solutions)

def parser(line) -> tuple:
    assert line.count('=') == 1
    regex = r'([+-])(\d+(?:\.\d+)?)[*]X\^(\d+)'
    sub = re.sub(regex, '', line.strip())
    mid = sub.replace(' ','')
    LR = ['+' + _ if _[0] not in '+-' else _ for _ in mid.split('=')]# if _[0] not in '+-' else _ ]
    lhs, rhs = [re.compile(regex).findall( _ ) for _ in LR]
    LHS = collections.defaultdict(float)
    RHS = collections.defaultdict(float)
    for sig, cofstr, pwr in lhs:
        cof = float(cofstr)
        cof = -cof if sig == '-' else cof
        LHS[ int(pwr) ] += cof
    for sig, cofstr, pwr in rhs:
        cof = float(cofstr)
        cof = -cof if sig == '-' else cof
        RHS[ int(pwr) ] += cof
    return ( LHS, RHS )


# driver/test

egs = [
    "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0",
    "5 * X^0 + 4 * X^1 = 4 * X^0",
    "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0",
    "6 * X^0 = 6 * X^0",
    "10 * X^0 = 15 * X^0",
    # FIXME - above: added tests
    "1 * X^0 + 2 * X^1 + 5 * X^2 = 0",
    "42 * X^0 + 21 + 2 * X^1 + 3 * X^2 = 0",
    '136.2 * X^0 - 64.5 * X^1 + 52.9 * X^2 + 5.6 * X^3 = -42.1 * X^0 - 21.4 * X^1 - 77 * X^2 + 1024 * X^3 - 33 * X^0',
    "42 * X^0 + 21 + 2 * X^1 + 3 * X^2 + 0", # testing wrong input
]
for eg in egs:
    print(eg)
    l,r = parser( eg )
    #for side in parser(eg):
        #for k,v in side.items():print('side/',k,v)
    #print('/parsed\n')
    rf_string,pd_string = cutter( eg )
    redform = 'Reduced form: '
    padding =  redform + Yello
    print(f'{Green}{rf_string}{Rest}')

    DBG = rf_string[14:]
    def printpadding(s):print(f'{padding}{s}{Rest}')
    match eg:
        case "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0":
            printpadding('4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0')#+Rest)
            assert DBG == '4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0'
        case "5 * X^0 + 4 * X^1 = 4 * X^0":
            printpadding('1 * X^0 + 4 * X^1 = 0')#+Rest)
            assert DBG == '1 * X^0 + 4 * X^1 = 0'
        case "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0":
            printpadding('5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 0')#+Rest)
            assert DBG == '5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 0'
        case "6 * X^0 = 6 * X^0":
            printpadding('0 * X^0 = 0')#+Rest)
            assert DBG == '0 * X^0 = 0'
        case "10 * X^0 = 15 * X^0":
            printpadding('-5 * X^0 = 0')#+Rest)
            assert DBG == '-5 * X^0 = 0'
        case "1 * X^0 + 2 * X^1 + 5 * X^2 = 0":
            printpadding('1 * X^0 + 2 * X^1 + 5 * X^2 = 0')#)+Rest)
            assert DBG == '1 * X^0 + 2 * X^1 + 5 * X^2 = 0'

    if pd_string:
        print(pd_string)
    print()
