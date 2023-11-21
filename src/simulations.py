from roobet import *
import hashlib

i = 0
Client = Crash()

while (i<1000000):
    hash = hashlib.sha256(b"H").hexdigest()[:64] # 64-bit, 16 hex chars
    print(hash)
    print(Client.get_multiplier(hash))
    i=i+1


