from bankovyucet import BankovyUcet

class Banka():

    def __init__(self, nazov_banky):
        self.nazov_banky = nazov_banky
        self.ucty = []

    def zaloz_ucet(self, meno, zostatok=0):
        for ucet in self.ucty:
            meno_klienta =  ucet.get_majitel()
            if meno_klienta == meno:
                raise ValueError('meno klienta už existuje')
        klient = BankovyUcet(meno, zostatok)
        self.ucty.append(klient)

    def zrus_ucet(self, meno):
        existuje_majitel = False
        zostatok_nula = False
        ucet_na_vymazanie = None
        for ucet in self.ucty:
            if meno == ucet.get_majitel():
                existuje_majitel = True
                if ucet.get_zostatok() == 0:
                    zostatok_nula = True
                    ucet_na_vymazanie = ucet
        if existuje_majitel == False:
            raise ValueError('chyba ucet neexistuje')
        elif zostatok_nula == False:
            raise ValueError('Na ucte mate este peniaze')
        self.ucty.remove(ucet_na_vymazanie)
        
        

        



banka = Banka('Prima')
banka.zaloz_ucet('Jozo')
banka.zaloz_ucet('Jano')