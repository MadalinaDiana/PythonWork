# variabila este zona din memoria unui calculator care contine date, o cutiuta in care se pot pune valori
# ex 2----------------------------------
fruct = "mere"
nr = 0
kg = 0
pret = 0.0
cumpara = False
for nr in range(0, 11, 1):
    kg = kg + 1
    pret = pret + 3
    nr = nr + 1
    if nr < 10:
        cumpara = False
    else:
        cumpara = True
# ex 5 cu printarea----------------------------------
print(f'S-au cumparat, {cumpara}, {nr}  {fruct} cu kilogramre {kg} si a costat {pret}  lei')
# ex 3----------------------------------
print(type(pret))
# ex 4----------------------------------
pret = round(pret)
print(type(pret))
print(pret)
# # ex 6----------------------------------
# numele = input("Scrie numele tau: ")
# prenume = input("Scrie prenumele tau: ")
# print(len(numele) + len(prenume))
# # ex 7----------------------------------
# lungimea = int(input("Introdu lungimea dreptunghiului: "))
# latimea = int(input("Introdu latimea dreptunghiului: "))
# aria = latimea * lungimea
# print(f'Aria dreptunghiului este: {aria}')
# ex 8----------------------------------
# propozitia = 'Coral is either the stupidest animal or the smartest rock'
# de_gasit = " the "
# print(propozitia.count(de_gasit))

# ex 9 - de gasit the substring----------------------------------
# subs_prop = 'Coral is either the stupidest animal or the smartest rock'
# de_gasitsubs = "the"
# print(propozitia.count(de_gasitsubs))
#  ex 10 - eroare deoarece nu avem numere in str----------------------------------
# assert subs_prop.isdigit(), 'Acest string nu contine doar numere' # isnumeric returneaza true chiar daca avem fractii sau nr romane
# assert subs_prop.isnumeric(), 'Acest string contine doar numere'
# ex 1----------------------------------
# impar = input("Introdu o propozitie impara: ")
# print(impar[(len(impar)//2)])
# ex 2----------------------------------

# def is_palindrome(s):
#     string = s
#     if (string == string[::1]):
#         print("Sirul este palindrom")
#         return True
#     else:
#         print("Sirul nu este palindrom")
#         return False
# assert is_palindrome('noon')
# ex 3----------------------------------
# a, b = input('Scrie doua cuvinte').split(' '); print(a,'\n',  b)
# ex 4----------------------------------
# prop = input("Introdu propozitia dorita: ")
# caracter = prop[0]
# cuvant_nou = prop[0] + prop[1:-1].replace(caracter, caracter.upper()) + prop[-1]
# print(cuvant_nou)
#
# # ex 5----------------------------------
# user = input("Introdu user-ul: ")
# parola = input("Introdu parola: ")
# print(f"Parola pt {user} este {'*'*len(parola)} si are {len(parola)} caractere.")
