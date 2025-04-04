
class Robot():

    def __init__(self, meno, hmotnost): # inicializacna metoda/konštruktor
        self.__set_meno(meno)
        self.hmotnost = hmotnost

    def predstav_sa(self):
        return f'Volám sa {self.__meno} a moja hmotnost je {self.hmotnost}'

    def __set_meno(self, meno):
        if len(meno) < 4:
            raise ValueError('chyba kratke meno')
        else:
            self.__meno = meno


    def __get_meno(self):
        return self.__meno

    meno = property(__get_meno, __set_meno)


objekt1 = Robot('Jozo', 120)
#objekt1.meno = 'Jo'                 # atribut vytvorený cez property/ v tomto pripade nevieme vytvorit nekorektný objekt
#print(objekt1.meno)                  # pristupujem cez atribut meno, ktorý je vytvorený cez property 
#objekt1.meno = 'Jozinko'
#print(objekt1.predstav_sa())