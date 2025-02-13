

class Obyvatel():

    def __init__(self, meno, vek, pohlavie):
        self.meno = meno
        self.vek = vek
        self.pohlavie = pohlavie
    
    def __str__(self):
        return f'{self.meno} {self.vek} {self.pohlavie}'



obyvatel1 = Obyvatel('Jozo', 18, 'm')
print(obyvatel1)
