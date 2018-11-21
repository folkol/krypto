import hashlib
from itertools import product

from pandas import date_range

SALT = 'somesalt'.encode()
DIGEST = 'b93d35d303b71ce6b0d27f6b858454de1dd6956b911bbf83c59ab81bd0c70f38'

dates = date_range('1900-01-01', '1999-12-31')
for date, seq in product(dates, range(10000)):
    pnr = date.strftime("%y%m%d-") + format(seq, "04d")
    digest = hashlib.sha256(SALT + pnr.encode()).hexdigest()
    if DIGEST == digest:
        print('Found:', pnr)
