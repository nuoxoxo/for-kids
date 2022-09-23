import random, time

W = '\033[0;37m'
G = '\033[32m'
Y = '\033[33m'
C = '\033[36m'
No = '\033[0m'

def count_correct_both(code, breaker) -> int:
    if len(code) != len(breaker):
        return -1
    res = 0
    for i in range(len(code)):
        if code[i] == breaker[i]:
            res += 1
    return res

def count_correct_color(maker, breaker) -> int:
    if len(maker) != len(breaker):
        return -1
    code = maker.copy()
    for i in range(len(code)):
        if code[i] == breaker[i]:
            code[i] = None
    freq = {}
    for n in code:
        if not n:
            continue
        if n not in freq:
            freq[n] = 1
        else:
            freq[n] += 1
    res = 0
    for n in breaker:
        if n in freq and freq[n] != 0:
            res += 1
            freq[n] -= 1
    return res

def printer(records) -> None:
    print()
    for i in range(len(records) - 1, -1, -1):
        print(records[i])
        i -= 1
    print()

# Game block

while True:
    choices = [1, 2, 3, 4, 5]#, 6, 7, 8]
    codemaker = []
    records = []
    for _ in range(4):
        codemaker.append(str(random.choice(choices)))
    # input(codemaker)
    for _ in range(10):
        record = []
        codebreaker = []
        guess = input("input: ")
        if guess == 'exit':
            print("The code is: ", ''.join(codemaker))
            exit()
        for i in range(4):
            codebreaker.append(guess[i])
        correct_both = count_correct_both(codemaker, codebreaker)
        correct_color = count_correct_color(codemaker, codebreaker)
        record.extend( (guess, correct_both, correct_color) )
        records.append(record)
        if correct_both == len(codemaker):
            print("Correct! The code is: ", ''.join(codemaker))
            exit()
        else:
            printer(records)
            # print("both right:", correct_both, "\tcolor right:", correct_color)
        
