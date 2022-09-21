class Masina:

    def __init__(self, numeMasina):
        # atribuite, fileds
        self.numeMasina = numeMasina
        self.anMasina = None
        self.consumMare = False
        self.km = 0
        self.consum = 0


    def set_anMasina(self, an):
        self.anMasina = an

    def set_consumTotal(self, km, consum):
        self.consumMasina = (km*consum)/100

    def afisare_date(self):
        print(f"Numele masinii este {self.numeMasina} din anul {self.anMasina} si are un consum de {self.consumMasina}")
        if self.consumMasina >= 80:
            print("consumul este prea mare")
            self.consumMare = True
        else:
            print("consumul este bun")

