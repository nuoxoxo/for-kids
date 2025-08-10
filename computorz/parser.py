import collections, re

def parser(line):
    line = line.strip().replace(' ','')
    if line[0] != '-':
        line = '+' + line
    regex = r'([+-])(\d+(\.\d+)?)[*]X\^(\d+)'
    remain = re.sub(regex, '', line)
    terms = re.compile(regex).findall(line)
    return (line, terms, remain)

egs = [
    "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0",
    "5 * X^0 + 4 * X^1 = 4 * X^0",
    "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0",
    "1 * X^0 + 2 * X^1 + 5 * X^2 = 0",
    "42 * X^0 + 21 + 2 * X^1 + 3 * X^2 = 0",
    '8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 + 21 = 3 * X^0 + 42'
]

for eg in egs:
    print('\neg/',eg)#,'\n')
    lhs, rhs = [parser(_.strip()) for _ in eg.split('=')]
    for i,p in enumerate([lhs, rhs]):
        if i == 0: print('\nLHS/')
        else: print('\nRHS/')
        line, terms, remain = p
        print('  line  /', line)
        print('  terms /', terms)
        print('  remain/', remain)
        if remain:
            raise ValueError('check your input')
