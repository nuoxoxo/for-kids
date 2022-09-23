import random, time

W = '\033[0;37m'
G = '\033[32m'
Y = '\033[33m'
C = '\033[36m'
RS = '\033[0m' # reset

while True:
    codemaker = []
    choices = [1, 2, 3, 4, 5, 6, 7, 8]
    for _ in range(4):
        codemaker.append(random.choice(choices))
    input(codemaker)
