import random

# ex 1
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for numar in alte_numere:
    if numar % 2 == 0:
        numere_pare.append(numar)
    else:
        numere_impare.append(numar)
    if numar > 0:
        numere_pozitive.append(numar)
    else:
        numere_negative.append(numar)
print(f'Numere pare: {numere_pare}')
print(f'Numere impare: {numere_impare}')
print(f'Numere negative: {numere_negative}')
print(f'Numere pozitive: {numere_pozitive}')
# ex 2
for numar_mare in range(len(alte_numere)):
    for numar_mic in range(numar_mare + 1, (len(alte_numere))):
        if alte_numere[numar_mare] > alte_numere[numar_mic]:
            alte_numere[numar_mare], alte_numere[numar_mic] = alte_numere[numar_mic], alte_numere[numar_mare]
print(alte_numere)
# ex 3
# print('*' * 80)
# numar_secret = random.randint(0, 30)
# numar_ghicit = None
# while numar_secret != numar_ghicit:
#     print(numar_secret)
#     numar_ghicit = int(input('Ghiceste un numar de la 1 la 30: '))
#     if numar_ghicit > numar_secret:
#         print('Nr secret e mai mic')
#     elif numar_ghicit < numar_secret:
#         print('Nr secret e mai mare')
# print('Felicitări! Ai ghicit!')

# ex 4
# print('*' * 80)
# numar_ales = int(input('Introdu un numar: '))
# for randuri in range(numar_ales + 1):
#     for coloane in range(randuri):
#         print(randuri, end=' ')
#     print('')  # linie noua

# ex 5
print('*' * 80)
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
for randuri in tastatura_telefon:
    for element in randuri:
        print(f'Cifra curentă este {element}')
