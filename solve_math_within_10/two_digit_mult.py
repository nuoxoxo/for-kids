import random, time

white = '\033[0;37m'
green = '\033[32m'
yell = '\033[33m'
cyan = '\033[36m'
noc = '\033[0m'

U = 60 # upper_bound

while True:
    a = random.randint(11, 99)
    b = random.randint(11, 99)
    e = 'x'
    res = 1e9
    if a < b:
        a, b = b, a
    if (e == '/' or e == '÷') and b == 0:
        continue
    # time.sleep(0.9)
    print(yell + str(a), e, b, noc)
    guess = input(white + 'Your answer is: ' + noc)
    if guess == 'exit' or guess == 'end':
        break
    if guess == 'next':
        continue
    if not guess.isdigit():
        continue
    #print()
    if e == '+':
        res = a + b
    elif e == '-':
        res = a - b
    elif e == 'x':
        res = a * b
    elif e == '÷' or e == '/':
        res = a // b
    print(guess)
    if res == int(guess):
        m = a // 10
        n = a % 10
        o = b // 10
        p = b % 10
        print('-')
        print('', m, n, '\n', o, p)
        print('--------')
        print(m*o, n*p)
        print('-')
        print(f'{green} ➜ Correct! {noc} \n')
    else:
        print(f'{cyan} ➜ Wrong! {noc}')
        print(f'{green} ➜ The answer is {res} {noc} \n')

print(white + 'see you next time :)' + noc)
