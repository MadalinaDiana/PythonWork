# 1. Funcție care primește o lună din an și returnează câte zile are acea luna
def calendar(luna):
    lista = [1, 3, 5, 7, 8, 10, 12]
    if luna == 2:
        print('Luna Februarie are 28-29 de zile')
    elif luna in lista:
        print('Luna aleasa are 31 de zile')
    else:
        print('Luna aleasa are 30 de zile')

# 2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
# împărțirea a două numere.


def calculator(x, y):
    suma = x + y
    diferenta = x - y
    inmultire = x * y
    impartire = x // y
    return suma, diferenta, inmultire, impartire


'''3. Funcție care primește o lista de cifre (adică doar 0-9)
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră'''

def CountFreq(li):
    freq = {}
    for items in li:
        freq[items] = li.count(items)
    print(freq)


# 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
def maximumnr(y, x, z):
    if z < y > x:
        return f'{y} este cel mai mare nr'
    elif z < x > y:
        return f'{x} este cel mai mare nr'
    else:
        return f'{z} este cel mai mare nr'

# 5. Funcție care să primească un număr și să returneze suma tuturor numerelor
# de la 0 la acel număr


def sumanr(numar):
    suma = 0
    res = sum(range(1, numar + 1))
    return "Suma numerelor pana la ", numar, "numere este: ", res

# calendar(int(input('Introdu numarul lunei dorite: ')))


a, b, c, d = calculator(10, 2)
print('Suma este: ', a)
print('Diferenta este: ', b)
print('Inmultire este: ', c)
print('Impartirea este: ', d)
li = [1, 3, 1, 5, 9, 7, 7, 5, 5]
CountFreq(li)
print(maximumnr(9, 11, 20))
print("Suma este", sumanr(5))