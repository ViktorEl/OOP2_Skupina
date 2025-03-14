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
        
    def prevod(self, odosielatel, prijemca, suma):
        ucet_odosielatela = self.najdi_ucet(odosielatel)
        ucet_prijemca = self.najdi_ucet(prijemca)
        suma_s_poplatkom = suma * 1.01
        poplatok_banke = suma_s_poplatkom - suma
        zostatok_odosielatel = ucet_odosielatela.get_zostatok()
        if zostatok_odosielatel < suma_s_poplatkom:
            raise ValueError('chyba nemate dostatok penazi na ucte')
        ucet_odosielatela.vyber(suma_s_poplatkom)
        ucet_prijemca.vklad(suma)
        self.__interny_ucet.vklad(poplatok_banke)

    def __str__(self):
        vsetky_ucty = ''
        for ucet in self.ucty:
            vsetky_ucty += str(ucet) + '\n'
        return vsetky_ucty

    def uloz(self, nazov_suboru):
        with open(nazov_suboru, 'w', encoding='utf-8') as f:
            f.write(str(self))
    
    def nacitaj(self, nazov_suboru):
        with open(nazov_suboru, 'r', encoding='utf-8') as f:
            nacitany = f.read()
            return nacitany

    def hodnota_banky(self):
        spolu_hodnota = 0
        for ucet in self.ucty:
            suma = ucet.get_zostatok()
            spolu_hodnota += suma
        spolu_hodnota += self.__interny_ucet.get_zostatok()
        return spolu_hodnota

banka = Banka('Prima')
banka.zaloz_ucet('Jozo')
banka.zaloz_ucet('Jano')
banka.vloz_na_ucet('Jano', 100)
#banka.uloz('ucty.txt')
#print(banka.nacitaj('ucty.txt'))
banka.prevod('Jano', 'Jozo', 50)
print(banka.hodnota_banky())
