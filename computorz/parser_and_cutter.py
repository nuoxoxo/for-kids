import collections, re
Green,Yello,Mage,Cyan,Rest = ['\033[1;32m','\033[1;33m','\033[31m','\033[36m','\033[0m']

def cutter(line):
    l,r = parser( line )
    for k,v in r.items(): l[k] -= v
    for k,v in l.items(): l[k] = round(v,7) # to have finite decimal places
    ### for k,v in l.items():# math.isclose(c, 0, abs_tol=1e-12) # removed zeroes?? ### TODO
    for k,v in l.items(): print('flat/',k,v)

    print('/flatten\n')

    # TODO 2 /

    ### 6 * X^0 = 6 * X^0 should be
    ### 0 * X^0 = 0

    res = []
    for k,v in sorted(l.items()):
        if abs(v) > 1e-12: # to have non-0 floats
            w = int(v) if v == int(v) else v
            res.append( f'{ "+" if w > 0 else "-" } { abs(w) } * X^{ k }' )
    res = ' '.join(res)
    if res.startswith('+ '):
        return f'{res[2:]} = 0'
    return f'{res} = 0'

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
    for side in parser(eg):
        for k,v in side.items():print('side/',k,v)

    print('/parsed\n')

    res = cutter( eg )
    print(f'Reduced form: {Green}{res}{Rest}\n')
