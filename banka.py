from bankovyucet import BankovyUcet

class Banka():

    def __init__(self, nazov_banky):
        self.nazov_banky = nazov_banky
        self.ucty = []
        self.__interny_ucet = BankovyUcet('interny_ucet')

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

    def najdi_ucet(self, meno):
        for ucet in self.ucty:
            if meno == ucet.get_majitel():
                return ucet
        raise ValueError('chyba ucet neexistuje')

    def vloz_na_ucet(self, meno, suma):
        ucet = self.najdi_ucet(meno)
        ucet.vklad(suma)

    
    def vyber_z_uctu(self, meno, suma):
        ucet = self.najdi_ucet(meno)
        suma_s_poplatkom = suma * 1.01
        poplatok_banke = suma_s_poplatkom - suma
        ucet.vyber(suma_s_poplatkom)
        self.__interny_ucet.vklad(poplatok_banke)


    def vyber_vsetko(self, meno):
        ucet = self.najdi_ucet(meno)
        vydaj_penazi = ucet.get_zostatok() / 1.01
        poplatok_banke = ucet.get_zostatok() - vydaj_penazi
        ucet.vyber(vydaj_penazi)
        self.__interny_ucet.vklad(poplatok_banke)
        ucet.vyber(ucet.get_zostatok())
        



        

banka = Banka('Prima')
banka.zaloz_ucet('Jozo')
banka.zaloz_ucet('Jano')
banka.vloz_na_ucet('Jano', 100)