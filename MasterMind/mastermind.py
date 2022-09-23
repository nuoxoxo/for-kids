import random, time

W = '\033[0;37m'
G = '\033[32m'
Y = '\033[33m'
C = '\033[36m'
RS = '\033[0m' # reset

def count_correct_both(code, breaker):
    if len(code) != len(breaker):
        return -1
    res = 0
    for i in range(len(code)):
        if code[i] == breaker[i]:
            res += 1
    return res

def count_correct_color(maker, breaker):
    if len(maker) != len(breaker):
        return -1
    code = maker.copy()
    for i in range(len(code)): # don't count if well-placed
        if code[i] == breaker[i]:
            code[i] = None
    # print(code)
    freq = {}
    for n in code:
        if not n:
            continue
        if n not in freq: # don't count duplicates
            freq[n] = 1
        else:
            freq[n] += 1
    # print(freq)
    res = 0
    for n in breaker:
        if n in freq and freq[n] != 0:
            res += 1
            freq[n] -= 1
            # print(freq)
    """
    for i in range(len(breaker)):
        for j in range(len(code)):
            if i != j and breaker[i] == code[j] and freq[n] > 0:
                res += 1
                freq[n] -= 1
                print(freq)
    """
    return res

# Game block

while True:
    codemaker = []
    choices = [1, 2, 3, 4, 5]#, 6, 7, 8]
    for _ in range(4):
        codemaker.append(str(random.choice(choices)))
    # input(codemaker)
    for _ in range(10):
        codebreaker = []
        guess = input("input: ")
        if guess == 'exit':
            print("The code is: ", ''.join(codemaker))
            exit()
        for i in range(4):
            codebreaker.append(guess[i])
        correct_both = count_correct_both(codemaker, codebreaker)
        correct_color = count_correct_color(codemaker, codebreaker)
        if correct_both == len(codemaker):
            print("Correct! The code is: ", ''.join(codemaker))
            exit()
        else:
            print("both right:", correct_both, "\tcolor right:", correct_color)
