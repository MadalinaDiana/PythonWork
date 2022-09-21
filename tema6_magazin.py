""" Clasa magazin:
Atribute: produse, suprafata_magazin
Metode: adauga_produse, sterge_produse"""


class Magazin:
    def __init__(self, nume):
        self.nume = nume
        self.fond = 0
        self.depozit = {}
        self.id = 1

    def adauga_produse(self, nume, pret, buc=1, id=None):
        if id in self.depozit:
            self.depozit[id]['Bucati'] += buc
        elif id is None:
            self.depozit[self.id] = {
                'Nume': nume,
                'Bucati': buc,
                'Pret': pret
            }
            self.id += 1

    def sterge_produse(self, id):
        if id in self.depozit:
            del self.depozit[id]
        else:
            print("Acest ID este invalid")

    def vinde(self, id, buc=1):
        if id not in self.depozit:
            print("Acest ID este invalid")
            return

        if self.depozit[id]['Bucati'] < buc:
            print('Acest produs nu mai e in stoc')
            return

        self.depozit[id]['Bucati'] -= buc
        self.fond += self.depozit[id]['Pret']*buc
        print('Fond:', self.fond)

    def update_pret(self, id, pret_nou):
        if id not in self.depozit:
            return
        self.depozit[id]['Pret'] = pret_nou

    def listeaza_id_produse(self):
        print('ID', 'NUME', 'BUCATI', 'PRET')
        for (id, produs) in self.depozit.items():
            print(id, produs['Nume'], produs['Bucati'], produs['Pret'])


m = Magazin('Magazinul Mada')
m.adauga_produse('paine', 3, 10) # se adauga numele, pretul si cantitatea
m.adauga_produse('cartofi', 5, 20)
m.listeaza_id_produse()
m.vinde(1, 10) # la vanzare se alege id-ul produsului, si cantitatea dorita, pretul pe produs va intra la venitul magazinului
m.listeaza_id_produse()
m.vinde(1, 1)
m.adauga_produse('paine', 5, 10, 1) # pentru adaugarea unui produs deja existent, vom folosi id-ul acestui produs
m.listeaza_id_produse()