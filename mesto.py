from obyvatel import Obyvatel

class MestoObyvatelia():

    def __init__(self, mesto):
        self.mesto = mesto
        self.obyvatelia = []

    def uloz_obyvatela(self, meno, vek, pohlavie):
        obyvatel = Obyvatel(meno, vek, pohlavie)
        self.obyvatelia.append(obyvatel)

    def pocet_obyvatelov_podla_veku(self, vek):
        pocitadlo = 0
        for obyvatel in self.obyvatelia:
            if vek == obyvatel.get_vek():
                pocitadlo += 1
        return pocitadlo

    def pocet_podla_pohlavia(self, pohlavie):
        pocitadlo = 0
        for obyvatel in self.obyvatelia:
            if pohlavie == obyvatel.get_pohlavie():
                pocitadlo += 1
        return pocitadlo




roznava = MestoObyvatelia('roznava')
roznava.uloz_obyvatela('Jozo', 40, 'm')
roznava.uloz_obyvatela('Lucia', 27, 'z')
roznava.uloz_obyvatela('Milan', 27, 'm')
print(roznava.pocet_obyvatelov_podla_veku(27))
print(roznava.pocet_podla_pohlavia('m'))







