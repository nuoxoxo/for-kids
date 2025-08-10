import collections, re, math, sys
TEST,INFS = True, 1e-12
if not TEST:
    Green,Yello,Mage,Cyan,Rest = '\033[1;32m','\033[1;33m','\033[31m','\033[1;36m','\033[0m'
else:
    Green,Yello,Mage,Cyan,Rest = '','','','',''

def printer(line):
    rf_string, pd_string, res = cutter( line )
    print(f'{Green}{rf_string}{Rest}')
    print(f'{Yello}{pd_string}{Rest}')
    if all(res):
        if isinstance(res[0],complex):
            for _ in res:
                print(f'{Cyan}{str(_).replace("(","").replace(")","").replace("j","i")}{Rest}')
        else:
            for _ in [round(_,7) for _ in res]: print(f'{Cyan}{_}{Rest}')
    elif res[0] != None:
        print(f'{Cyan}{res[0]}{Rest}')
    print()

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
    _solutionis = 'The solution is:'
    _complex = 'Discriminant is strictly negative, the two complex solutions are:'
    _realsln = 'Discriminant is strictly positive, the two solutions are:'

    res_reduced_form = f'Reduced form: {res} = 0'
    res_polydegree = '' if polydegree == 0 else f'Polynomial degree: {polydegree}\n'

    a,b,c = l[2],l[1],l[0]

    if polydegree > 2:
        res_polydegree += _gt2
    elif polydegree == 0: # CONSTANT . FIXME
        if abs(c) < INFS:#l[0] == 0:
            res_polydegree += _anyrealnum
        else:
            res_polydegree += _nosolution
    elif polydegree == 1: # LINEAR . FIXME
        if abs(b) < INFS:
            if abs(c) < INFS:
                res_polydegree += _anyrealnum
            else:
                res_polydegree += _nosolution
        else:
            res_polydegree += _solutionis
            _solutions[0] = round(-c / b,7)
    else: # QUADRATIC . FIXME
        if abs(a) < INFS:
            if abs(b) < INFS:
                if abs(c) < INFS:
                    res_polydegree += _anyrealnum
                else:
                    res_polydegree += _nosolution
            else: # QUADRATIC ---> case/ Linear
                res_polydegree += _solutionis
                _solutions[0] = round(-c/b,7)
        else: # QUADRATIC ---> case/ complex solutions
            D = b*b - 4*a*c
            if D < 0:
                res_polydegree += _complex
                REAL = -b / (2 * a)
                IMG = math.sqrt(-D) / (2 * a)
                _solutions = [complex(REAL, IMG), complex(REAL, - IMG)]
            elif abs(D) < INFS: # QUADRATIC ---> case/ one real root . FIXME
                _solutions[0] = round(-c / b,7)
                res_polydegree += _solutionis
            else: # QUADRATIC ---> case/ 2 real roots
                DSR = math.sqrt(D)
                res_polydegree += _realsln
                _solutions = [round(-b + _,7) / (2 * a) for _ in [DSR, -DSR]]
    return ( res_reduced_form, res_polydegree, _solutions)

def parser(line) -> tuple:
    assert line.count('=') == 1
    regex = r'([+-])(\d+(?:\.\d+)?)[*]X\^(\d+)'
    sub = re.sub(regex, '', line.strip())
    mid = sub.replace(' ','')
    LR = ['+' + _ if _[0] not in '+-' else _ for _ in mid.split('=')]
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

if not TEST:
    if len(sys.argv) != 2:
        print('args/err');sys.exit(1)
    inp = sys.argv[1]
    checkchars = r'[*=+\-X0-9 ]+'
    if not re.fullmatch( checkchars, inp):
        print('inp/illegal chars');sys.exit(1)
    printer( inp )
    #print('test/not\n')
else:
    for i,eg in enumerate(egs):
        printer( eg )
        #print('test/yes')
