

class Obyvatel():

    def __init__(self, meno, vek, pohlavie):
        self.meno = meno
        self.__vek = vek
        self.__pohlavie = pohlavie
    
    def get_vek(self):
        return self.__vek

    def get_pohlavie(self):
        return self.__pohlavie

    def __eq__(self, other):
        if isinstance(other, Obyvatel):
            if self.meno == other.meno:
                return True
            return False
        return False


obyvatel1 = Obyvatel('Jozo', 18, 'm')
#print(obyvatel1)
obyvatel2 = Obyvatel('Jozo', 50, 'm')
print(obyvatel1 == obyvatel2)       # volam metodu __eq__
