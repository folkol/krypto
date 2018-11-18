import binascii
import hashlib
from itertools import product

SALT = 'somesalt'.encode()
DIGEST = binascii.unhexlify('51d2c362401171fcd9601097907a3034d73009de4b391581d1ed7b72d810522e')

for year, month, day, sequence_number in product(range(100), range(13), range(32), range(10000)):
    pnr = '{:02d}{:02d}{:02d}-{:04d}'.format(year, month, day, sequence_number)
    if DIGEST == hashlib.sha256(SALT + pnr.encode()).digest():
        print('Found pnr:', pnr)
        break
