

class Obyvatel():

    def __init__(self, meno, vek, pohlavie):
        self.meno = meno
        self.__vek = vek
        self.__pohlavie = pohlavie
    
    def get_vek(self):
        return self.__vek

    def get_pohlavie(self):
        return self.__pohlavie


#obyvatel1 = Obyvatel('Jozo', 18, 'm')
#print(obyvatel1)
