import math


class Bod():

    def __init__(self, x, y):
        self.set_x(x)
        self.set_y(y)
    
    def __set_x(self, x):
        if not isinstance(x, (int, float)):
            raise ValueError('chyba nekorektne vstupy')
        self.__x = x

    def __set_y(self, y):
        if not isinstance(y, (int, float)):
            raise ValueError('chyba nekorektne vstupy')
        self.__y = y

    def __get_x(self):
        return self.__x

    def __get_y(self):
        return self.__y
    
    def vzdialenost_od_bodu(self, other):
        if isinstance(other, Bod):
            vzdialenost = math.sqrt((self.__x - other.__x)**2 + (self.__y - other.__y)**2)
            return vzdialenost
        else:
            return 'bod nie je bod'

    def vzdialenost_od_pociatku(self):
        vzdialenost = self.vzdialenost_od_bodu(Bod(0,0))
        return vzdialenost
    
    def __eq__(self, other):
        if isinstance(other, Bod):
            if self.__x == other.__x and self.__y == other.__y:
                return True
            else:
                return False
        else:
            return False
            
    def __str__(self):
        return f'{self.__x} {self.__y}'

    x = property(__get_x, __set_x)
    y = property(__get_y, __set_y)


objekt1 = Bod(2,4)
objekt2 = Bod(3, 6)
#print(objekt1.vzdialenost_od_bodu(objekt2))
#print(objekt1.vzdialenost_od_pociatku())
#print(objekt1 == objekt2)               # porovnanie rovnosti objektov volam metodu eq
#print(objekt1)                              # volam metodu __str__


