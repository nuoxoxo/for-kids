from datetime import date
import random

def get_doomsday(n) -> int:
    if 1899 < n < 2000:
        dday = 3
        n -= 1900
    elif 1999 < n < 2100:
        dday = 4
        n -= 2000
    div4 = n // 4
    #print(dday, n, div4) # debugger
    return (dday + n + div4) % 7

def unit_test() -> None:
    print(f'Doomsday 1929 is {get_doomsday(1929)} (should be 4)')
    print(f'Doomsday 1969 is {get_doomsday(1969)} (should be 5)')
    print(f'Doomsday 1994 is {get_doomsday(1994)} (should be 1)')

def sep():
    print('\n\033[1;33;40m- \033[1;37;40m')

start_dt = date.today().replace(day=1, month=1, year=1900).toordinal()
end_dt = date.today().replace(day=31, month=12).toordinal()

Right, Wrong, Total = 0, 0, 0
Green = '\033[1;32;40m'
Yello = '\033[1;33;40m'
White = '\033[1;37;40m'
Red = '\033[1;31;40m'

#unit_test()

while True:
    print('')
    print(f'Right: {Green}{Right}{White} | ', end='')
    print(f'Wrong: {Red}{Wrong}{White} | ', end='')
    print(f'Total: {Yello}{Total}{White} \n') 

    dt = date.fromordinal(random.randint(start_dt, end_dt))
    yr = dt.year
    ans_real = get_doomsday(yr)
    ans_user = input(f'{yr}\n')

    if ans_user == 'exit' or ans_user == 'sortie':
        break

    ans_user = int(ans_user)
    Total += 1
    if ans_real == ans_user:
        Right += 1
        print(f'➜ {Red}Right!{White} Doomsday {yr} is {ans_real} ')
        sep()
    else:
        Wrong += 1
        print(f'➜ {Red}Wrong!{White} Doomsday {yr} is {ans_real} ')
        sep()
