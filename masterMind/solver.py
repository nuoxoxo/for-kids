import random

# func

def print_possible(p):
    for i in range(len(p)):
        print(i + 1, ': ', p[i])
    print()

def get_first_call(c, i):
    assert i < len(c) and i + 1 < len(c)
    res = c[i], c[i], c[i], c[i + 1]
    return res

# global

colors = [1,2,3,4,5,6,7,8]
possible = [[] for _ in range(len(colors))]
#print_possible(possible)

first_call_got_something = False
first_call_pointer = -2

SURE = 0
WAIT = 1

# main

while True:
    print_possible(possible)
    feedback = ''
    call = ''
    # make first call
    if not first_call_got_something:
        first_call_pointer += 2
        call = get_first_call(colors, first_call_pointer)
        print(call)
    # get input
    while len(feedback) != 2 or not feedback.isnumeric():
        feedback = input('feedback: ')
    if feedback == 'go':
        exit()
    red = int(feedback[0])
    white = int(feedback[1])
    # check first call
    if not first_call_got_something:
        if red == 0 and white == 0:
            continue
        first_call_got_something = True
    print(feedback)
    # case 1: 00
    # case 2: 01
    # case 3: 02 -> LC is 4, RC is one of 1-3
    # case 4: 11 -> LC is 4
    # case 5: 20 -> 4 is sure, one of 1-3 is sure



""" Deprecated """


"""
# initial guess, which is a 4-repeated digit

# choice_0 = random.randrange(1, 5)#9)
choice_0 = 1
for _ in range(4):
    print(choice_0, end = '')
print()

hints_specific = []
hints_general = []

def print_hints(hints) -> None:
    for _ in hints:
        print('\t', _)

while True:
    feedback = input('feedback: ')
    if feedback == 'exit':
        exit()
    if len(feedback) != 2:
        continue
    RP = feedback[0] # right place
    if RP != '0':
        hints_general.append(RP + ' of those places must be: ' + str(choice_0))
    print_hints(hints_general)
"""
