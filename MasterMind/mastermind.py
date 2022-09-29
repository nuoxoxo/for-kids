import random

W = '\033[0;37m'
G = '\033[32m'
Y = '\033[33m'
C = '\033[36m'
No = '\033[0m'

def count_right_place(code, breaker) -> int:
    if len(code) != len(breaker):
        return -1
    res = 0
    for i in range(len(code)):
        if code[i] == breaker[i]:
            res += 1
    return res

def count_right_color(maker, breaker) -> int:
    if len(maker) != len(breaker):
        return -1
    code = maker.copy()
    freq = {}
    for n in code:
        if n:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
    for i in range(len(code)):
        if code[i] == breaker[i]:
            freq[code[i]] -= 1
    # print(freq) # debugger
    res = 0
    for i in range(len(breaker)):
        n = breaker[i]
        if n != code[i] and n in freq and freq[n] != 0:
            freq[n] -= 1
            res += 1
    return res

def printer(records) -> None:
    print()
    for i in range(len(records) - 1, -1, -1):
        print(records[i])
        i -= 1
    print()

# Game block

choices = [1, 2, 3, 4, 5, 6, 7, 8]
codemaker = []
records = []
for _ in range(4):
    codemaker.append(str(random.choice(choices)))
for _ in range(10):
    record = []
    codebreaker = []
    guess = input("input: ")
    if guess == 'exit':
        print("The code is: ", ''.join(codemaker))
        exit()
    for i in range(4):
        codebreaker.append(guess[i])
    right_place = count_right_place(codemaker, codebreaker)
    right_color = count_right_color(codemaker, codebreaker)
    record.extend( (guess, right_place, right_color) )
    records.append(record)
    if right_place == len(codemaker):
        print("Good! The code is: ", ''.join(codemaker))
        exit()
    else:
        printer(records)

