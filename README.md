# Fun with Caesar Cipher

```
usage: python3 caesar.py [key]
	- If key is given, encrypt STDIN with the given key.
	- If no key is given, attempt to guess which key was used to encrypt STDIN.
```

## Encrypt

```
$ echo "THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG'S BACK 1234567890" | python3 caesar.py 7
AOL XBPJR IYVDU MVE QBTWLK VCLY AOL SHGF KVN'Z IHJR 1234567890
```

## Decrypt

```
$ echo "AOL XBPJR IYVDU MVE QBTWLK VCLY AOL SHGF KVN'Z IHJR 1234567890" | python3 caesar.py
Score for 0: 	0.00
Score for 1: 	0.00
Score for 2: 	0.00
Score for 3: 	0.00
Score for 4: 	0.09
Score for 5: 	0.00
Score for 6: 	0.00
Score for 7: 	0.73
Score for 8: 	0.00
Score for 9: 	0.00
Score for 10: 	0.00
Score for 11: 	0.09
Score for 12: 	0.00
Score for 13: 	0.00
Score for 14: 	0.18
Score for 15: 	0.00
Score for 16: 	0.00
Score for 17: 	0.00
Score for 18: 	0.00
Score for 19: 	0.00
Score for 20: 	0.18
Score for 21: 	0.09
Score for 22: 	0.00
Score for 23: 	0.00
Score for 24: 	0.00
Score for 25: 	0.00
My guess is that the key was: 7!
THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG'S BACK 1234567890
```
