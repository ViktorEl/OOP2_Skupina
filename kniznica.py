from kniha2 import Kniha

class Kniznica():

    def __init__(self, nazov):
        self.set_nazov(nazov)
        self.zoznam = []

    def set_nazov(self, nazov):
        if len(self.nazov) > 20:
            raise ValueError('Chyba dlhy nazov')
        else:
            self.nazov = nazov

    def uloz_knihu(self, nazov, suma):
        kniha = Kniha(nazov, suma)
        self.zoznam.append(kniha)

    def vypis_knihy(self):
        for kniha in self.zoznam:
            print(kniha.get_nazov())


betliar = Kniznica('Betliar')
betliar.uloz_knihu('Harry Potter', 15.60)
betliar.uloz_knihu('Zaklinac', 18)



