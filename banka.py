from bankovyucet import BankovyUcet

class Banka():

    def __init__(self, nazov_banky):
        self.nazov_banky = nazov_banky
        self.ucty = []


    def zaloz_ucet(self, meno, zostatok=0):
        for ucet in self.ucty:
            pass
        klient = BankovyUcet(meno, zostatok)
        self.ucty.append(klient)
