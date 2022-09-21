import math


# ex 1
class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def aria(self):
        return math.pi * self.raza ** 2

    def descrie_cerc(self):
        print(f'Raza cercului este: {self.raza}, culoarea cercului este {self.culoare}')

    def diametru(self):
        return self.raza * 2

    def circumferinta(self):
        return math.pi * self.diametru()


# ex 2
class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f'Dreptunghiul are {self.lungime} lungime, {self.latime} latime si culoarea {self.culoare}. \n '
              f'Are perimetrul {self.perimetru()}, aria {self.aria()}')

    def aria(self):
        return self.lungime * self.latime

    def perimetru(self):
        return 2 * self.aria()

    def schimba_culoare(self, noua_culoare):
        self.culoare = noua_culoare

# ex 3


class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Numele angajatului este {self.nume_complet()} si are salariul {self.salariu}')

    def nume_complet(self):
        return self.nume + ' ' + self.prenume

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self, procent):
        self.salariu_lunar += self.salariu * (procent/100)
        return self.salariu_lunar


# ex 4


class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} al contului {self.iban} are soldul {self.sold}')
    def debitare_cont(self, suma):
        self.sold += suma
        return self.sold
    def creditare_cont(self, suma):
        self.sold -= suma
        return self.sold


c = Cerc(4, 'galben')
c.descrie_cerc()
print(c.aria(), 'aria cercului')
print(c.diametru(), 'diametrul cercului')
print(c.circumferinta(), 'circumferinta cercului')
print('*'*80)

d = Dreptunghi(13, 11, 'rosu')
d.descrie()
d.aria()
d.perimetru()
d.schimba_culoare('verde')
d.descrie()
print('*'*80)

a = Angajat('Mihai', 'Constantin', 2000)
a.descrie()
print(a.salariu_anual(), 'salariul anual')
a.marire_salariu(15)
a.descrie()
print('*'*80)

s = Cont(1234567, 'Madalina', 600)
s.afisare_sold()
s.debitare_cont(300)
s.afisare_sold()
s.creditare_cont(200)
s.afisare_sold()






