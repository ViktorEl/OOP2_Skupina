
class Robot():

    def __init__(self, meno, hmotnost): # inicializacna metoda/konštruktor
        self.meno = meno                # inštančná premenná
        self.hmotnost = hmotnost

    def predstav_sa(self):
        print(f'Volám sa {self.meno} a moja hmotnost je {self.hmotnost}')

    def set_meno(self, meno):
        if len(meno) < 4:
            raise ValueError('chyba kratke meno')



objekt1 = Robot('Jozo', 120) # vytvorenie objektu/inštancia 
print(objekt1.meno)          # pristupujem k atributu meno daneho objetku
objekt1.predstav_sa()        # pristupujem k metode, ktorý ma daný objekt k dispozicii

objekt2 = Robot('Mat', 150) # vytvorenie druhého objektu
objekt2.meno = 'Pat'
print(objekt2.meno)
