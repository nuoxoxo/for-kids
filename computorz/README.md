# 11
-  [x] needs a better/correct case-logic 
  - `if !a && !b && !c` - coefficients are zeros/ Any real number is a solution.
  - `if !a && !b && c` - nonzero constant/ No solution.
  - `if !a && b` - linear/ `bx + x = 0`
  - `if a` - quadratic
  - [ ]  to re-check | _TODO_

&nbsp;|A|B|C|D||
-|-|-|-|-|-
||
quadratic | !0 |    |    | + | 2 real roots
quadratic | !0 |    |    | 0 | (touches X-axis once) 1 real repeated root 
quadratic | !0 |    |    | - | _2 complex roots_
||
linear    | 0  | !0 |    |   | 1 real root 
||
constant  | 0  | 0  | !0 |   | No solution.
constant  | 0  | 0  | 0  |   |Any real number is a solution.

-  [ ] `math.sqrt` should be `something ** .5`
-  [ ] we don't need regex checkers
-  [ ] look for testcases

# 10 
- [x] prog.: now solves quadratic and linear
  - coefficients a, b, c
    - a,b,c are the only things that determine 1) the nature of the equation 2) the solution(s)
    -  `a,b,c ∈ REAL` needless to say
  -  moved _TODO_:
    -  ~~needs a better/correct case-logic~~
    -  ~~minor | `math.sqrt` is actually `something ** .5`~~
- [x] quote: _Exponents are organized and present._

# 8
- [x] prog.: back to basics
  - [x] case/ linear, nonzero constant (no solution), a=b=c=0 (any real number is a solution) | ~~_TODO_~~
  - case/ quadratic, the nature of roots depends on the Discriminant D
    - D = `b ** 2 - 4 * a * c`
```b
D > 0: 2 distinct real solutions
D = 0: 1 real solution (a repeated root)
D < 0: 2 complex conjugate solutions (no real roots)
```

# 6 
- [x] 初代 parser
```sh
def parser(line): # line should be an equation like ' *** = *** '
    """
    supposing that our input is correctly-formatted/
        > every term respect n ∗ X^p
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
```

# Aug 4 
- [x] samples for parser - For Copy n Paste
```py
egs = [
    "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0",
    # Reduced form: 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0
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
