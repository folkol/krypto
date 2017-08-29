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

ALPHABET = list(ascii_uppercase)

Guess = namedtuple('guess', 'key, score')


def encrypt(plaintext, key=1):
    """Encrypts the given plaintext message using a Caesar Cipher."""

    def shift_char(char):
        try:
            return ALPHABET[(ALPHABET.index(char) + key) % len(ALPHABET)]
        except ValueError:
            return char

    return ''.join(shift_char(char) for char in list(plaintext))


def decrypt(ciphertext, key):
    """Decrypts the Caesar Ciphertext using the given key."""
    return encrypt(ciphertext, -key)


def score(ciphertext, key, dictionary):
    """Scores the given key using dictionary lookup of the decrypted words."""
    words = decrypt(ciphertext, key).split()
    real_words = [word for word in words if word in dictionary]
    return len(real_words) / len(words)


if __name__ == '__main__':
    indata = sys.stdin.read().upper()
    if len(sys.argv) > 1:
        key = int(sys.argv[1])

        ciphertext = encrypt(indata, key)
        print(ciphertext)
    else:
        with open('/usr/share/dict/words') as f:
            dictionary = [word.upper().strip() for word in f.readlines()]

        guess = Guess(key=0, score=0)
        for key in range(len(ALPHABET)):
            new_score = score(indata, key, dictionary)
            print(f'Score for {key}: \t{new_score:.2f}')
            if new_score > guess.score:
                guess = Guess(key=key, score=new_score)

        print(f'My guess is that the key was: {guess.key}!')
        print(decrypt(indata, guess.key))
