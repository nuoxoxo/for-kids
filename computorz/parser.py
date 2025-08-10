import collections, re

def parser(line): # line should be an equation like ' *** = *** '
    """
    supposing that our input is correctly-formatted/
        > every term respect a ∗ X^p
        > except 0 on the rhs
    """
    assert line.count('=') == 1

    regex = r'([+-])(\d+(?:\.\d+)?)[*]X\^(\d+)'

    # testing
    sub = re.sub(regex, '', line.strip())
    mid = sub.replace(' ','')
    print(mid.split('='))

    LR = ['+' + _ if _[0] not in '+-' else _ for _ in mid.split('=')]# if _[0] not in '+-' else _ ]
    for lr in LR:print('lr/',lr)
    print('org/', line)
    print('sub/', sub)
    print('mid/', mid)
    for _ in LR: print('side/', _)
    print()

    lhs, rhs = [re.compile(regex).findall( _ ) for _ in LR]
    print('lhs/',lhs)
    print('rhs/',rhs);
    print()

    LHS = collections.defaultdict(float)
    for sig, cofstr, pwr in lhs:
        cof = float(cofstr)
        cof = -cof if sig == '-' else cof
        LHS[ int(pwr) ] += cof

    RHS = collections.defaultdict(float)
    for sig, cofstr, pwr in rhs:
        cof = float(cofstr)
        cof = -cof if sig == '-' else cof
        RHS[ int(pwr) ] += cof

    for k,v in LHS.items(): print('LHS/', k, v)    
    for k,v in RHS.items(): print('RHS/', k, v)    

    print('\n/ends\n')


egs = [
    "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0",
    "5 * X^0 + 4 * X^1 = 4 * X^0",
    "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0",
    "1 * X^0 + 2 * X^1 + 5 * X^2 = 0",
    "42 * X^0 + 21 + 2 * X^1 + 3 * X^2 = 0",
    '136.2 * X^0 - 64.5 * X^1 + 52.9 * X^2 + 5.6 * X^3 = -42.1 * X^0 - 21.4 * X^1 - 77 * X^2 + 1024 * X^3 - 33 * X^0',
    "42 * X^0 + 21 + 2 * X^1 + 3 * X^2 + 0",
]
for eg in egs: parser( eg )
