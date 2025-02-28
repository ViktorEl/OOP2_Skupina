from kniha2 import Kniha

class Kniznica():

    def __init__(self, nazov):
        self.set_nazov(nazov)
        self.zoznam = []

    def set_nazov(self, nazov):
        if len(nazov) > 20:
            raise ValueError('Chyba dlhy nazov')
        else:
            self.nazov = nazov

    def uloz_knihu(self, nazov, suma):
        kniha = Kniha(nazov, suma)
        self.zoznam.append(kniha)

    def vypis_knihy(self):
        for kniha in self.zoznam:
            print(kniha)

    def celkova_hodnota_knih(self):
        spolu_hodnota = 0
        for kniha in self.zoznam:
            suma_knihy = kniha.get_suma()
            spolu_hodnota += suma_knihy
            spolu_hodnota = round(spolu_hodnota, 2)
        return f'{spolu_hodnota}' 


betliar = Kniznica('Betliar')
betliar.uloz_knihu('Harry Potter', 15.63)
betliar.uloz_knihu('Zaklinac', 18.15)
betliar.vypis_knihy()
print(betliar.celkova_hodnota_knih())




