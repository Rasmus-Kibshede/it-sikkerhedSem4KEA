import random
import os

## non secure random!!!
## key = random.randbytes(16).hex()
## print(key)

## secure way of doing it (psudorandom)
cryptoKey = os.urandom(16).hex()



print(int(cryptoKey, 16))