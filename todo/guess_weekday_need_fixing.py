from datetime import date
import random

def i2w(n):
    cases = {
        1: ['Monday', 'lundi'],
        2: ['Tuesday', 'mardi'],
        3: ['Wednesday', 'mercredi'],
        4: ['Thursday', 'jeudi'],
        5: ['Friday', 'vendredi'],
        6: ['Saturday', 'samedi'],
        7: ['Sunday', 'dimanche']
    }
    return cases.get(n, 'N/A')

def sep():
    print('\033[1;33;40m-- \033[1;37;40m')

start_dt = date.today().replace(day=1, month=1, year=1900).toordinal()
end_dt = date.today().replace(day=31, month=12).toordinal()

Right, Wrong, Total = 0, 0, 0
pct = 0

while True:

    #print('')
    pct = Right // Total * 100
    print(f'Right: \033[1;32;40m{Right}\033[1;37;40m | ', end='')
    print(f'Wrong: \033[1;31;40m{Wrong}\033[1;37;40m | ', end='')
    print(f'Total: \033[1;33;40m{Total}\033[1;37;40m | ')
    print(f'Pct.%: \033[1;33;40m{Right // Total * 100}%\033[1;37;40m ')
    print(f'Pct.%: \033[1;33;40m{pct}%\033[1;37;40m ')

    dt = date.fromordinal(random.randint(start_dt, end_dt))
    wd = str(dt.weekday())

    if wd.isdigit():
        ans_real = int(wd) + 1
    else:
        continue

    ans_word = i2w(ans_real)
    ans_user = input(f'{dt}\n')

    if ans_user == 'exit' or ans_user == 'sortie':
        break
    ans_user = int(ans_user)
    Total += 1

    if ans_real == ans_user:
        Right += 1
        print(f'Right! It\'s a {ans_word[0]} ')
        print(f'Correcte! C\'est {ans_word[1]} ')
        sep()
    else:
        Wrong += 1
        print(f'Wrong! The answer is {ans_word[0]} ')
        print(f'Faux! La vraie date c\'est {ans_word[1]} ')
        sep()

