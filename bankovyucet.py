
class BankovyUcet():

    def __init__(self ,majitel, zostatok=0):
        self.__set_majitel(majitel)
        self.zostatok = zostatok


    def __set_majitel(self , majitel):
        if majitel == "":
            raise ValueError('majitel nemoze byt prazdny')
        if not isinstance(majitel , str):
            raise ValueError('majitel neni string')
        self.__majitel = majitel

    def get_majitel(self):
        return self.__majitel

    def get_zostatok(self):
        return self.zostatok

    def vklad(self , vklad):
        self.zostatok = self.zostatok + vklad


    def vyber(self , vyber):
        if vyber > self.zostatok:
            raise ValueError('prečo bereš viac ako maš')
        else:
            self.zostatok = self.zostatok - vyber


    def __str__(self):
        return f'{self.__majitel} {self.zostatok}'



ucet1 = BankovyUcet('Jozo')
print(ucet1)



        