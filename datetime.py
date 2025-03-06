'''Teoria ku kniznici datetime'''

import datetime     #importovanie kniznice/modulu datetime

rok = 2025          # rok moze byt aj vo formate 25
mesiac = 3          # mesiac
den = 6             # den

try:
    datetime.datetime(rok, mesiac, den) # funkcia na kontrolu korektneho datumu
    print('spravny datum')
except ValueError:
    raise ValueError('chybny datum')