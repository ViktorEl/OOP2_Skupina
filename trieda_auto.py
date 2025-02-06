class Auto():

    def __init__(self, znacka, spotreba):
        self.__set_znacka(znacka)
        self.__set_spotreba(spotreba)


    def __set_znacka(self, znacka):
        if not isinstance(znacka, str):
            raise TypeError('znacka nesmie byt cislo')
        elif len(znacka) < 2:
            raise ValueError('znacku musi mat voac ako 2 znaky')
        else:
            self.__znacka = znacka

    def __get_znacka(self):
        return self.__znacka
    
    def __set_spotreba(self, spotreba):
        if not isinstance(spotreba, (float, int)):
            raise TypeError('spotreba musi byt cislo')
        elif spotreba < 0:
            raise ValueError('spotreba musi byt kladne cislo')
        else:
            self.__spotreba = spotreba

    def __get_spotreba(self):
        return self.__spotreba

    spotreba = property(__get_spotreba, __set_spotreba)
    znacka = property(__get_znacka)

    def __str__(self):
        return f'{self.__znacka} {self.__spotreba}'
    
    def __eq__(self, other):
        if isinstance(other, Auto):
            if self.__spotreba == other.__spotreba:
                return True
            return False
        return False


auto1 = Auto('skoda', 20)
print(auto1.znacka)

    