import random, time

white = '\033[0;37m'
green = '\033[32m'
yell = '\033[33m'
cyan = '\033[36m'
noc = '\033[0m'

U = 20 # upper_bound

while True:
    a = random.randint(1, U)
    b = random.choice([U % a, U % a - 1])
    #b = random.randint(0, 9)
    s = random.choice(['+', '-'])
    #s = random.choice(['+', '-', 'x', '÷', '/'])
    res = 1e9
    if a < b:
        a, b = b, a
    if (s == '/' or s == '÷') and b == 0:
        continue
    time.sleep(0.9)
    print(yell + str(a), s, b, noc)
    guess = input(white + 'Your answer is: ' + noc)
    if guess == 'exit' or guess == 'end':
        break
    if guess == 'next':
        continue
    if not guess.isdigit():
        continue
    #print()
    if s == '+':
        res = a + b
    elif s == '-':
        res = a - b
    elif s == 'x':
        res = a * b
    elif s == '÷' or s == '/':
        res = a // b
    if res == int(guess):
        print(f'{green} ➜ Correct! {noc}')
    else:
        print(f'{cyan} ➜ Wrong! {noc}')
        print(f'{green} ➜ The answer is {res} {noc}')

print(white + 'see you next time :)' + noc)
