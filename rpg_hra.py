import random

class Postava():

    def __init__(self, meno, uroven, zivoty):
        self.set_meno(meno)
        self.set_uroven(uroven)
        self.set_zivoty(zivoty)

    def get_meno(self):
        return self.__meno
    
    def get_uroven(self):
        return self.__uroven

    def get_zivoty(self):
        return self.__zivoty
    
    def set_meno(self, meno):
        if not isinstance(meno, str):
            raise ValueError('meno musi byt slovo')
        if meno == "":
            raise ValueError('Musite zadat meno')
        self.__meno = meno

    def set_uroven(self, uroven):
        if not isinstance(uroven, int):
            raise ValueError('Uroven musi byt cislo')
        if uroven < 1 or uroven > 5:
            raise ValueError('uroven musi byt od 1 do 5')
        self.__uroven = uroven

    def set_zivoty(self, zivoty):
        if not isinstance(zivoty, int):
            raise ValueError('Zivoty musia byt cislo')
        if zivoty < 0 or zivoty > 20:
                raise ValueError('Zivoty musia byt od 0 do 20')
        self.__zivoty = zivoty

    def utok(self):
        return 'Postava útočí'
    

class Bojovnik(Postava):

    def __init__(self, meno, uroven, zivoty, sila):
        super().__init__(meno, uroven, zivoty)
        self.set_sila(sila)

    def set_sila(self, sila):
        if not isinstance(sila, int):
            raise ValueError('Sila musi byt cislo')
        if sila < 1 or sila > 10:
            raise ValueError('sila musi byt v rozsahu od 1 do 10')
        self.sila = sila

    def utok(self):
        nahodny_utok = random.randint(1, self.sila)
        return f'Bojovnik zautocil mečom silou {nahodny_utok}'
    
class Kuzelnik(Bojovnik):

    def __init__(self, meno, uroven, zivoty, sila, mana):
        super().__init__(meno, uroven, zivoty, sila)
        self.set_mana(mana)

    def set_mana(self, mana):
        if mana < 0 or mana > 50:
            raise ValueError('Mana musi byt v rozsahu od 0 do 50')
        self.mana = mana

    def set_sila(self, sila):
        if not isinstance(sila, int):
            raise ValueError('Sila musi byt cislo')
        if sila < 1 or sila > 20:
            raise ValueError('sila musi byt v rozsahu od 1 do 20')
        self.sila = sila 

    def utok(self):
        nahodna_sila = random.randint(1, self.sila)
        pass
    




