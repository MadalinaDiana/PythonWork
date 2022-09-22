from abc import ABC


class FormaGeometrica(ABC):
    PI = 3.14

    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print('Cel mai probabil am colturi')


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    def aria(self):
        return self.__raza ** 2 * FormaGeometrica.PI

    def descrie(self):
        print(f'Sunt un cerc')

    def get_raza(self):
        print('Luam raza')
        return self.__raza

    def set_latura(self, valoare):
        print(f'Schimbam valoare razei cu {valoare}')
        self.__raza = valoare

    def del_latura(self):
        print('Se sterge raza')
        del self.__raza


class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    def get_latura(self):
        print('Luam latura')
        return self.__latura

    def set_latura(self, valoare):
        print(f'Schimbam valoare laturii cu {valoare}')
        self.__latura = valoare

    def del_latura(self):
        print('Se sterge latura')
        del self.__latura

    def aria(self):
        return self.__latura ** 2

    def descrie(self):
        print(f'Sunt patrat')


c = Cerc(12)
print(c.aria())
c.descrie()

p = Patrat(4)
print(p.aria())
p.descrie()

a = FormaGeometrica()
a.descrie()
try:
    a.aria()
except NotImplementedError:
    print('Forma geometrica este clasa abstracta')









