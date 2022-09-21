import math


# ex 1.Funcție care să calculeze și să returneze suma a două numere
def suma(a, b):
    return a + b


# ex 2 Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

def tipnumar(a):
    if a % 2 == 0: #mai optim este sa facem direct return, deoarece ne spune daca condifia este adevarata sau nu
        #return a % 2 == 0
        return True
    else:
        return False


# ex 3 Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)

def calc_nume(nume, prenume, nume_mijlociu=""):
    a = len(nume)
    # b = len(prenume)
    # c = len(nume_mijlociu)
    # return a + b + c
    return len(nume) + len(prenume) + len(nume_mijlociu)


# ex 4 Funcție care returnează aria dreptunghiului
def aria_dreptunghi(lungime, latime):
    return lungime * latime


# ex 5 Funcție care returnează aria cercului
def aria_cerc(raza):
    return math.pi * raza ** 2


# ex 6 Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și Talse dacă nu găsește.
def find_char(prop, x):
    if x in prop:
        return True
    else:
        return False


# ex 7 Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y
def typeofchar(propozitie_tip):
    char_upper = 0
    char_lower = 0
    for i in propozitie_tip:
        if i.isupper():
            char_upper = char_upper + 1
        else:
            char_lower = char_lower + 1
    print(f'Numarul total de caractere upper este: {char_upper}')
    print(f'Numarul total de caractere lower este: {char_lower}')

# ex 8 Funcție care primește o LISTA de numere și returnează o LISTA doar cu
# numerele pozitive
def lista_nr(lista):
    lista_pozitive = []
    for i in lista:
        if i > 0:
            lista_pozitive.append(i)
    return f'Lista de numere pozitive este: {lista_pozitive}'

# ex 9 Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.
def comparare_nr(a, b):
    if a > b:
        print(f'Primul număr {a} este mai mare decat al doilea nr {b}')
    elif a < b:
        print(f'Al doilea nr {b} este mai mare decat primul nr {a}')
    else:
        print('Numerele sunt egale.')

# ex 10 Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False
def set_numar(a, set):
    if a in set:
        print(f'nu am adaugat numărul {a} în set. Acesta există deja')
        return False
    else:
        set.add(a)
        print(f'am adaugat numărul {a} în set.')
        return True

# print(suma(int(input('Introdu primul numar: ')), int(input('Introdu al doilea numar: '))))
print(tipnumar(7))
print(calc_nume('Laszlo', 'Madalina', 'Diana'))
print(f'Aria dreptunghiului este:{aria_dreptunghi(5, 8)}')
print(f'Aria cercului este: {aria_cerc(8)}')
print(find_char('Ana are mere', 'b'))
typeofchar('Ursul mergea prin padure Linistit')
print(lista_nr([1, 3, 5, -4, -8]))
# comparare_nr(int(input('Introdu primul nr: ')), int(input('Introdu al doilea nr: ')))
print(set_numar(3, {3, 6, 8, 6}))
