# Aug 10 
- [x] 初代 parser
```sh
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

    LR = ['+' + _ for _ in mid.split('=') if _[0] != '-' ]
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
    "42 * X^0 + 21 + 2 * X^1 + 3 * X^2 = 0",
]
for eg in egs: parser( eg )
```

# Aug 4 
- [x] samples for parser - For Copy n Paste
```py
egs = [
    "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0",
    # Polynomial degree: 2
    # Discriminant is strictly positive, the two solutions are:
    # 0.905239
    # -0.475131

    "5 * X^0 + 4 * X^1 = 4 * X^0",
    # Reduced form: 1 * X^0 + 4 * X^1 = 0
    # The solution is:
    # -0.25

    "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0",
    # Reduced form: 5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 0
    # Polynomial degree: 3
    # The polynomial degree is strictly greater than 2, I can't solve.

    "6 * X^0 = 6 * X^0",
    # Reduced form: 0 * X^0 = 0
    # Any real number is a solution.

    "10 * X^0 = 15 * X^0",
    # Reduced form: -5 * X^0 = 0
    # No solution.

    "1 * X^0 + 2 * X^1 + 5 * X^2 = 0",
    # Reduced form: 1 * X^0 + 2 * X^1 + 5 * X^2 = 0
    # Polynomial degree: 2
    # Discriminant is strictly negative, the two complex solutions are:
    # -1/5 + 2i/5
    # -1/5 - 2i/5
]
```
