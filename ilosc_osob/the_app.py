from the_functions import *

while True:
    try:
        a, b = input('wprowadz wymary ').split()
        c = input('ile pięter? ')
        x = ile_osob(float(a), float(b), int(c))
        print('Liczba osób: ', x)
        break
    except ValueError:
        print ('Złe dane, liczba osób: 0')
        print ('jeszcze raz')

srodki = input('Czy są środki? ')
ile_ludzi = ile_ze_srodkami(x, srodki)
print ('W sumie ',ile_ludzi ,' osób')


