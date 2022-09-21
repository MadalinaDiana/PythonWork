# ex 1
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
          'Fiat', 'Trabant', 'Opel']
# for tip in range(0, len(masini)):
#     print(f'Mașina mea preferată este {masini[tip]}')
# print('*' * 80)
# for tip in masini:
#     print(f'Mașina mea preferată este {tip}')
# print('*' * 80)
# tip_masina = 0
# while tip_masina < len(masini):
#     print(f'Mașina mea preferată este {masini[tip_masina]}')
#     tip_masina = tip_masina + 1
# print('*' * 80)
# ex 2
# for tip in range(1, len(masini)-1):
#     masini[tip] = masini[tip].upper()
# else:
#     print(masini)
# print('*' * 80)
# ex 3
# for tip in masini:
#     if tip == 'Mercedes':
#         print('Am găsit mașina dorită de dvs')
#         break
#     else:
#         print(f'Am găsit mașina {tip}. Mai căutam')
# ex 4
# for tip in masini:
#     if tip == 'Lăstun' or tip == 'Trabant':
#         continue
#     print(f'S-ar putea să vă placă mașina {tip}')
# ex 5
# masini_vechi = []
# for tip in masini:
#     if tip == 'Lăstun' or tip == 'Trabant':
#         masini_vechi.append(tip)
#         masini.append('Tesla')
# print(f'Noile modele de masini sunt {masini}')
# print(f'Modelele vechi de masini sunt {masini_vechi}')

# ex 6
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
client_buget = 15000

for masina, valoare in pret_masini.items():
    if valoare <= client_buget:
        print(f'Masina sugerata la bugetul dumneavoastra este {masina} cu valoarea {valoare}')
# Iterează prin listă. aici nu inteleg

# ex 7
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# aparitie_numar = 0
# for numar in numere:
#     if numar == 3:
#         aparitie_numar = aparitie_numar + 1
# print(aparitie_numar)
# ex 8
# suma_numere = 0
# for numar in numere:
#     suma_numere = suma_numere + numar
# print(suma_numere)
# ex 9
# maxim = 0
# for numar in numere:
#     if numar > maxim:
#         maxim = numar
# print(maxim)

for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = -numere[i]
print(numere)