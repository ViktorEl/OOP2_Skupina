class Bmi():
    def __init__(self, hmotnost, vyska):
        self.set_hmotnost(hmotnost)
        self.set_vyska(vyska)
  

    def set_hmotnost(self,hmotnost):
        if not isinstance(hmotnost, (int, float)):
            raise TypeError("Hmotnost musí být číslo")
        if hmotnost < 0:
            raise ValueError("Hmotnost musí být kladné číslo")
        else:
            self.__hmotnost = hmotnost


    def set_vyska(self,vyska):
        if not isinstance(vyska, (int, float)):
            raise TypeError("vyskat musí být číslo")
        if vyska <= 0:
            raise ValueError("vyska musí být kladné číslo")
        else:
            self.__vyska = vyska


    def get_hmotnost(self):
        return self.__hmotnost
    
    def get_vyska(self):
        return self.__vyska
    

    def vypocet_bmi(self):
        bmi = self.__hmotnost / (self.__vyska)**2
        return bmi
    

    def kategoria_bmi(self):
        bmi = self.vypocet_bmi()
        if bmi < 18.5:
            return 'uder weight'
        elif bmi > 18.5 and bmi < 24.9:
            return 'normal weight'
        elif bmi > 24.9 and bmi < 29.9:
            return 'overweight'
        elif bmi > 29.9 and bmi < 34.9:
            return 'obese'
        else:
            return 'severely obese'
        
    hmotnost = property(get_hmotnost, set_hmotnost)

    def __str__(self):
        return f'{self.__hmotnost} {self.__vyska}'
    

    def __eq__(self, other):
        if isinstance(other, Bmi):
            if self.__vyska == other.__vyska:
                return True
            else:
                return False
        return False
    

clovek1 = Bmi(70, 1.80)
#clovek2 = Bmi(70, 1.80)
#clovek3 = Bmi(80, 1.30)




#print(clovek1)
        


    