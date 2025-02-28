

class Kniha():

    def __init__(self, nazov, suma):
        self.__nazov = nazov
        self.set_suma(suma)
        
    def set_nazov(self, nazov):
        if not isinstance(nazov, str):
            raise ValueError('chyba nazov musi byť slovo')


    def __set_suma(self, suma):
        if not isinstance(suma, (int, float)):
            raise ValueError('chyba musite zadat cislo')
        self.__suma = suma

    def __get_suma(self):
        return self.__suma

    def get_nazov(self):
        return self.__nazov


    suma = property(__get_suma, __set_suma)

    def __str__(self):
        return f'{self.__nazov} {self.__suma}'
    
    def __eq__(self, other):
        if isinstance(other, Kniha):
            if self.__suma == other.__suma:
                return True
            return False
        return False



objekt = Kniha('Harry', 15)


