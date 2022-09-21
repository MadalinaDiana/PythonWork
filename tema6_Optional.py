from datetime import date


# ex 1

class Factura:
    seria = 222

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate
        return self.cantitate

    def schimba_pretul(self, pret):
        self.pret_buc = pret
        return self.pret_buc

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume
        return self.nume_produs

    def genereaza_factura(self):
        today = date.today()
        total = self.cantitate * self.pret_buc
        print(self.seria, self.numar)
        print('Data', today)
        print('|'.join(['Produs', 'Cantitate', 'Pret bucata', 'Total']))
        print(self.nume_produs, self.cantitate, self.pret_buc, total, end='|')


# ex 2
class Masina:
    Marca = 'Dacia'
    Viteza_Actuala = 0
    Culoare = 'gri'
    culori_disponibile = {'rosu', 'alb', 'maro', 'mov', 'portocaliu'}
    Inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        print(
            f'Masina cu marca {self.Marca} model {self.model} are viteza maxima {self.viteza_maxima}, culoarea {self.Culoare} are viteza actuala {self.Viteza_Actuala} '
            f'si este inmatriculata {self.Inmatriculata}')

    def inmatriculare(self):
        self.Inmatriculata = True

    def vopseste(self, culoare):
        if culoare in self.culori_disponibile:
            self.Culoare = culoare
        else:
            print(f'Eroare, culoare aleasa nu se afla in lista de culori: {self.culori_disponibile}')

    def accelereaza(self, viteza):
        if viteza < 0:
            print('Eroare, deoarece ati trecut o viteza negativa')
        elif viteza >= self.viteza_maxima:
            self.Viteza_Actuala = self.viteza_maxima
        else:
            self.Viteza_Actuala = viteza

    def franeaza(self, viteza):
        self.Viteza_Actuala = 0


# ex 3
class ToDoList:
    todo = {}

    def adauga_task(self, nume, descriere):
        if nume not in ToDoList.todo:
            ToDoList.todo[nume] = descriere
        else:
            print('Deja exista un task cu acest nume, nu se poate adauga')

    def finalizeaza_task(self, nume):
        if nume in ToDoList.todo.keys():
            del ToDoList.todo[nume]
        else:
            print('Nu avem acest nume trecut in agenda, nu se poate sterge')

    def afiseaza_todo_list(self):
        print(ToDoList.todo.keys())

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task not in ToDoList.todo:
            raspuns = input('Acest task nu este trecut in agenda, doriti sa il trecem?')
            if raspuns == 'nu':
                print('La revedere!')
            elif raspuns == 'da':
                detalii = input('Detalii task: ')
                self.adauga_task(nume_task, detalii)
            else:
                print('Ati introdus un raspuns invalid')
        else:
            print('Acest task este deja salvat')


f = Factura(33, 'Aspirator', 12, 250)
f.genereaza_factura()
print('*' * 80)
f.schimba_cantitatea(10)
f.genereaza_factura()
print('*' * 80)
f.schimba_pretul(200)
f.genereaza_factura()
print('*' * 80)
f.schimba_nume_produs('calcator')
f.genereaza_factura()
print('*' * 80)
m = Masina('Logan', 120)
m.descrie()
m.inmatriculare()
m.vopseste('mov')
m.accelereaza(130)
m.descrie()
m.franeaza(30)
m.descrie()
print('*' * 80)

lista = ToDoList()
lista.adauga_task('alergare', 'ceva')
lista.afiseaza_todo_list()
lista.finalizeaza_task('alergare')
lista.afiseaza_todo_list()
lista.afiseaza_detalii_suplimentare('cina')
lista.afiseaza_todo_list()

