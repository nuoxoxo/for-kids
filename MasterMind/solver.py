import random

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
    RP = feedback[0] # Right Place
    if RP != '0':
        hints_general.append(RP + ' of those places must be: ' + str(choice_0))
    print_hints(hints_general)
