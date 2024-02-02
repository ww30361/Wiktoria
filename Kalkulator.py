import sys



print('Witaj w kalkulatorze')



a = int(input('Podaj pierwszą liczbę: '))

b = int(input('Podaj drugą liczbę: '))



operacja = int(input('Wybierz rodzaj operacji: 1 - Dodawanie, 2 - Odejmowanie, 3 - Mnożenie, 4 - Dzielenie: '))



if (operacja == 1):

    wynik = a + b

elif (operacja == 2):

    wynik = a - b

elif (operacja == 3):

    wynik = a * b

elif (operacja == 4):

    if (b == 0):

        print('Nie wolno dzielić przez zero')

        sys.exit()

    wynik = a / b

else:

    print('Zły wybór')

    sys.exit()



print('Wynik działania:',  wynik)

