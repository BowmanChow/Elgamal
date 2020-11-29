from Elgamal import *

secret_key, public_key = Elgamal_gen_key()
print(f'secret_key = {secret_key}')
print(public_key.__dict__)
Plaintext = randint(1, public_key.prime - 1)
print(f'Plaintext = {Plaintext}')

encrypted = Elgamal_encrypt(Plaintext, public_key)
print(f'encrypted = {encrypted}')

Pt_rec = Elgamal_decrypt(encrypted, secret_key, public_key)

print(f'PlainText recieved = {Pt_rec}')
