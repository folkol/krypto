"""
Caesar "crypto".

 - Assumes a dictionary in '/usr/share/dict/words'.
 - Converts everything to UPPER CASE.

    usage: python3 caesar.py [key]
        - If key is given, encrypt STDIN with the given key.
        - If no key is given, attempt to guess which key was used to encrypt STDIN.
"""
import sys
from collections import namedtuple
from string import ascii_uppercase

Guess = namedtuple('guess', 'key, score')

ALPHABET = list(ascii_uppercase)


def encrypt(msg, key):
    def shift_char(c):
        if c in ALPHABET:
            return ALPHABET[(ALPHABET.index(c) + key) % len(ALPHABET)]
        else:
            return c

    return ''.join(shift_char(c) for c in list(msg))


def decrypt(msg, key):
    return encrypt(msg, -key)


def score(cipher_text, key, words):
    recognized_words = sum(1 for word in decrypt(cipher_text, key).split() if word in words)
    return recognized_words / len(cipher_text.split())


if __name__ == '__main__':
    indata = sys.stdin.read().upper()
    if len(sys.argv) > 1:
        key = int(sys.argv[1])

        cipher = encrypt(indata, key)
        print(cipher)
    else:
        with open('/usr/share/dict/words') as f:
            words = [word.upper().strip() for word in f.readlines()]
        guess = Guess(key=0, score=0)
        for key in range(len(ALPHABET)):
            new_score = score(indata, key, words)
            print(f'Score for {key}: \t{new_score:.2f}')
            if new_score > guess.score:
                guess = Guess(key=key, score=new_score)

        print(f'My guess is that the key was: {guess.key}!')
        print(decrypt(indata, guess.key))
