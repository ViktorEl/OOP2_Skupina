
class Osoba():

    def __init__(self, meno, vek):
        self.meno = meno
        self.vek = vek

    def predstav_sa(self):
        return f'Volám sa {self.meno} a mám {self.vek} rokov'
        

class Student(Osoba):

    def __init__(self, meno, vek, rocnik):
        super().__init__(meno, vek)
        self.rocnik = rocnik

    def predstav_sa(self):
        return super().predstav_sa() + f' a navstevujem {self.rocnik} rocnik' # polymorfizmus v praxi


class Ucitel(Osoba):

    def __init__(self, meno, vek, predmet):
        super().__init__(meno, vek)
        self.predmet = predmet

    def predstav_sa(self):
        return super().predstav_sa() + f' a učím predmet {self.predmet}'

class Asistent(Student):

    def __init__(self, meno, vek, rocnik, predmet):
        super().__init__(meno, vek, rocnik)
        self.predmet = predmet
    
    def predstav_sa(self):
        return super().predstav_sa() + f' a zaroven vypomaham s predmetom {self.predmet}'



student = Student('Jano', 16, 'prvý')
print(student.predstav_sa())
asistent = Asistent('Jozo', 18, 'treti', 'Matematika')
print(asistent.predstav_sa())
print(dir(asistent))