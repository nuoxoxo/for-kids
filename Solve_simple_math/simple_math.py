import random, time

green = '\033[32m'
yell = '\033[33m'
cyan = '\033[36m'
white = '\033[0;37m'
noc = '\033[0m'

Right, Wrong, Total = 0, 0, 0

while True:
    """
    print(f'Right: {green}{Right}{white} | ', end = '')
    print(f'Wrong: {cyan}{Wrong}{white} | ', end = '')
    print(f'Total: {Total} | ', end = '') 
    if Total == 0:
        print(f'Ratio: {Right // 1 * 100}% ')
    else:
        print(f'Ratio: {yell}{round(Right / Total * 100, 2)}{white}% ')
    print()
    """
    # time.sleep(1.2)
    a = random.randint(-1, 12)
    b = random.randint(-1, 12)
    # s = random.choice(['+', '-', 'x', '÷', '/'])
<<<<<<< HEAD
    # s = random.choice(['+', '-'])
    s = random.choice(['x'])
=======
    s = random.choice(['+', '-', '-', '-'])
>>>>>>> 4dbd659d9c0800712a439bb7cb7327ff25c0e365
    res = 1e9
    if a == 0 or b == 0:
        continue
    if a < b:
        a, b = b, a
    if b == 0 and (s == '/' or s == '÷'):
        continue
    #time.sleep(0.9)
    print(yell + str(a), s, b, noc)
    line = input(white + 'Your answer is: ' + noc).strip()
    if line == 'exit' or line == 'end':
        break
    if line == 'next':
        continue
    if not line.isdigit():
        continue
    guess = int(line)
    # print():
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
        Right += 1
    else:
        Wrong += 1
        print(a, b, a*b, guess, int(guess))
        print(f'{cyan} ➜ Wrong! {noc}')
        print(f'{green} ➜ The answer is {res} {noc}')
    # print()
    Total += 1
print(white + 'see you next time :)' + noc)
