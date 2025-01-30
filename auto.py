
class Auto():

    def __init__(self, znacka, model, rok_vyroby):
        self.set_znacka(znacka)
        self.model = model
        self.rok_vyroby = rok_vyroby

    def vypis_parametre(self):
        print(f'Značka auta:{self.__znacka}, model: {self.model}, rok: {self.rok_vyroby}')

    def set_znacka(self, znacka):
        if znacka == "":
            raise ValueError('chyba nezadali ste nič')
        if not isinstance(znacka,str):
            raise ValueError('chyba znacka musi byť reťazec')
        else:
            self.__znacka = znacka

    
    def get_znacka(self):
        return self.__znacka
    
    znacka = property(get_znacka, set_znacka)

    def __str__(self):      # magicka metoda ktora vrati vsetky atributy objektu
        return f'{self.__znacka} {self.model} {self.rok_vyroby}'


    def __eq__(self, other):
        if isinstance(other, Auto):
            pass
        





auto1 = Auto('Skoda', 'Fabia', 2020)
auto2 = Auto('Skoda', 'Octavia', 2022)
zoznam = [1, 2, 3]
#print(dir(auto1))      # vypise vsetky dostupne metody a atributy pre dany objekt


