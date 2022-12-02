import hashlib

secret = 'iwrupvqb'

nonce = 0

while not hashlib.md5((secret+str(nonce)).encode()).hexdigest()[0:5] == "00000":
    nonce += 1

print("Task 1: %s" %(nonce))

while not hashlib.md5((secret+str(nonce)).encode()).hexdigest()[0:6] == "000000":
    nonce += 1

print("Task 2: %s" %(nonce))
