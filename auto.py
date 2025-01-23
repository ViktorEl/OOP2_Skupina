
class Auto():

    def __init__(self, znacka, model, rok_vyroby):
        self.znacka = znacka
        self.model = model
        self.rok_vyroby = rok_vyroby

    def vypis_parametre(self):
        print(f'Značka auta:{self.znacka}, model: {self.model}, rok: {self.rok_vyroby}')

    def set_znacka(self, znacka):
        if znacka == "":
            raise ValueError('chyba nezadali ste nič')
        if not isinstance(znacka,str):
            pass




auto1 = Auto('Skoda', 'Fabia', 2020)
auto1.vypis_parametre()