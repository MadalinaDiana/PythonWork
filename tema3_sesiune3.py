# ex 1
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)
# -----------------------------------------------------------
# ex 2
print('Nota do apare de: ')
print(note_muzicale.count('do'))
# -----------------------------------------------------------
# ex 3
a = [3, 1, 0, 2]
b = [6, 5, 4]
# prima metoda
c = a + b
print('Rezultatul primei metode')
print(c)
# a doua metoda
a.extend(b)
print('Rezultatul metodei a doua')
print(a)
# -----------------------------------------------------------
# ex 4
c.sort()
print(c)  # la ex 4 Sortează numărul 0 folosind o funcție. nu inteleg aceasta cerinta
c.remove(0)
# -----------------------------------------------------------
# ex 5
if len(c) == 0: #era mai simplu daca puneam doar if element c, asa ca daca are elemente lista returneaza true daca nu, false
    print('Lista este goala ')
else:
    print('Lista contine valori ')
# -----------------------------------------------------------
# ex 6
c.clear() #cu del se sterge cu totul variabila din memorie, cu clear se sterg doar elementele, de obicei
        # garbagecolector sterge automat listele goale din memorie, deci nu ar fi nevoie de del pe element
print(f'Variabila c are acum atribuite: {c} valori')
# -----------------------------------------------------------
# ex 7
if len(c) == 0:
    print('Lista este goala ')
else:
    print('Lista contine valori ')
# -----------------------------------------------------------
# ex 8
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
for i in dict1:
    print(i)
# -----------------------------------------------------------
# # ex 9
prima_nota = list(dict1.items())[0][1]
doua_nota = list(dict1.items())[1][1]
treia_nota = list(dict1.items())[2][1]
print(f'Ana a luat nota: {prima_nota}')
print(f'Gigel a luat nota: {doua_nota}')
print(f'Dorel a luat nota: {treia_nota}')
# -----------------------------------------------------------
# # ex 10
dict1['Dorel'] = 6
print(list(dict1.items())[2][1])
# -----------------------------------------------------------
# # ex 11
del dict1['Gigel']
print('Clasa ramasa dupa plecarea lui Gigel', dict1)
# adaugarea unui nou coleg
dict1['Ionica'] = 9
print(dict1.keys())
# -----------------------------------------------------------
# ex 12
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni') #deoarece este set nu se pot adauga elemente de doua ori
print(zile_sapt)
# -----------------------------------------------------------
# ex 13
if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor din săptămâni.')
else:
    print('Weekend nu este un subset al zilelor din săptămâni.')
# -----------------------------------------------------------
# ex 14
dif = zile_sapt - weekend #se poate folosi difference
print('Diferenta dintre cele doua set-uri, este: ', dif)
# -----------------------------------------------------------
# ex 15
inter = zile_sapt.intersection(weekend) #operator & - intersectie intre seturi
print('Intersectia celor doua set-uri este: ', inter)