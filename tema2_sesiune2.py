""" ex1 : Flow control - if, else
 evalueaza conditii si bifurca codul in functie de rezultat
"""
import random
# ex 2
# x = 3
# if isinstance(x, int) and x >= 0 :
#     print('Nr natural')
# else:
#     print('Nu este nr natural')

# ex 3
#
# x = int(input("Introdu un nr intreg: "))
# if x < 0:
#     print("Nr este negativ")
# elif x > 0:
#     print("Nr este pozitiv")
# else:
#     print("Nr este neutru")

# ex 4
# x = int(input('Introdu un nr intreg: '))
# if -2 < x < 13:
#     print('Nr este in intervalul -2 si 13')
# else:
#     print('Nr nu este in intervalul -2 si 13')

# ex 5
# x = int(input('Scrie un nr intreg: '))
# y = int(input('Scrie un nr intreg: '))
# dif = x - y
# if dif <= 5:
#     print(f'Diferenta este mai mica de 5 si mai exact: {dif} ')
# else:
#     print(f'Diferenta dintre nr nu este mai mica de 5, si mai exact este: {dif} ')

# ex 6
# x = int(input('Introdu un nr intreg: '))
# if not (5 < x < 27):
#     print("nr nu se afla intre 5 si 27")
# else:
#     print("Nr se afla intre 5 si 27")


# ex 7
# x = int(input('Introdu primul nr: '))
# y = int(input('Introdu al doilea nr: '))
# if x == y:
#     print('Nr sunt egale')
# else:
#     print('Nr mai mare este:')
#     print(max(x, y))

# ex 8
# x = 1
# y = 3
# z = 2
# # isoscel
# if x == y == z:
#     print("Triunghi echilateral")
# elif x == y or x == z or y == z:
#     print("Triunghi isoscel")
# else:
#     print("Triunghi oarecare")

# ex 9
# a = input('Scrie o litera: ')
# vocale = ['a', 'e', 'i', 'o', 'u']
# if a in vocale:
#     print('Litera este vocala')
# else:
#     print('Nu este vocala')

# ex 10
# nota = int(input('Introdu nota'))
# if nota >= 9:
#     nota = 'A'
#     print(f'Nota este: {nota}')
# elif nota >= 8:
#     nota = 'B'
#     print(f'Nota este: {nota}')
# elif nota >= 7:
#     nota = 'C'
#     print(f'Nota este: {nota}')
# elif nota >= 6:
#     nota = 'D'
#     print(f'Nota este: {nota}')
# elif nota >= 4:
#     nota = 'E'
#     print(f'Nota este: {nota}')
# else:
#     nota = 'F'
#     print(f'Nota este: {nota}')
# ex 1-tema suplimentara
# x = int(input('Introdu nr: '))
# if len(str(x)) >= 4:
#     print(f'{x} are destule cifre')
# else:
#     print(f'{x} nu are destule cifre')
# ex 2 - tema suplimentara
# x = input('Introdu cifrele')
# if len(x) == 6:
#     print(f'{x} are exact 6 cifre')
# else:
#     print(f'{x} nu are destule cifre')

# ex 3
# x = int(input('Introdu un nr: '))
# if x % 2 == 0:
#     print('Nr este par')
# else:
#     print('Nr este impar')

# ex 4-tema suplimentara
# x = 3
# y = 4
# z = 10
# print(max(x, y, z))

# ex 5
# x = 4
# y = 6
# z = 15
# if x + y < z or x + z < y or y + z < x:
#     print('Triunghi valid')
# else:
#     print('Triunghi invalid')

# ex 6
# prop = 'Coral is either the stupidest animal or the smartest rock'
# x = int(input('Introdu un nr: '))
# print(prop[:-x]) #de la inceput pana la ceva

# ex 7
# prop = 'Coral is either the stupidest animal or the smartest rock'
# print(prop[:5]+prop[-5:])
# ex 8
# prop = 'Coral is either the stupidest animal or the smartest rock'
# cuv_index = prop.find('rock')
# print(cuv_index)
# print(prop[:cuv_index])
# ex 9
# prop = input('Scrie un string: ')
# assert prop[0].lower() == prop[-1].lower()
# ex 10
# sir = '0123456789'
# pare = []
# impare = []
# for i in range(len(sir)):
#     if i % 2 == 0:
#         pare.append(sir[i])
#     else:
#         impare.append(sir[i])
# print(f'Numerele pare sunt: {pare}')
# print(f'Numerele impare sunt: {impare}')
#altfel
# pare = sir[0::2]
# impare = sir[1:len(sir):2]
# ex 11
# importam random
# dice_roll = int(input('Scrie numarul care crezi ca va aparea pe zar: '))
# nr_intamplator = random.randint(0, 6)
# if dice_roll == nr_intamplator:
#     print(f"Ai ghicit. Felicitari! Ai ales {dice_roll} si zarul a fost {nr_intamplator} ")
# elif dice_roll < nr_intamplator:
#     print(f"Ai pierdut. Ai ales un numar mai mic. Ai ales  {dice_roll} si zarul a fost {nr_intamplator} ")
# else:
#     print(f"Ai pierdut. Ai ales un numar mai mare. Ai ales  {dice_roll} si zarul a fost {nr_intamplator} ")
txt ="Ai pierdut. Ai ales un numar mai mare. Ai ales"
print(txt.count("a", "b", "c"))
