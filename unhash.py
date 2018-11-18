import hashlib
import sys
from itertools import product

SALT = 'somesalt'.encode()
start = int(sys.argv[1])
end = int(sys.argv[2])
digest = sys.argv[3]

for year, month, day, seq in product(range(start, end), range(13), range(32), range(10000)):
    pnr = f'{year:02d}{month:02d}{day:02d}-{seq:04d}'
    if digest == hashlib.sha256(SALT + pnr.encode()).hexdigest():
        print(f'SHA256({digest}) = {pnr}')
        break
