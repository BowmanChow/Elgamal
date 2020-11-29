from Elgamal import *

group_bit = max_bit_length + 1

encrypt_bit = group_bit + 1


def Elgamal_gen_key_file(secret_key_file: str, public_key_file: str):
    sec, pub = Elgamal_gen_key()
    with open(secret_key_file, 'w')as f:
        print(sec, file=f)
    with open(public_key_file, 'w')as f:
        print(pub.prime, pub.generator, pub.public_key, file=f, sep='\n')


def Elgamal_pub_key_file(pub_key_file: str):
    with open(pub_key_file, 'r') as f:
        data = f.readlines()
    return Elgamal_public_key(int(data[0]), int(data[1]), int(data[2]))


def Elgamal_encrypt_file(text_file: str, pub_key_file: str, enc_file: str):
    with open(text_file, 'r') as f:
        data = f.read()
    data += '1'
    data += '0' * (group_bit - data.__len__() % group_bit)
    data = [data[i:i+group_bit]
            for i in range(0, data.__len__(), group_bit)]
    # print(data)
    data = [int(i, 2) for i in data]
    # print(data)
    pub_key = Elgamal_pub_key_file(pub_key_file)
    # print(pub_key.__dict__)
    encrypted = [Elgamal_encrypt(i, pub_key) for i in data]
    # print(encrypted)
    encrypted_bin = [(bin(i[0])[2:], bin(i[1])[2:]) for i in encrypted]
    encrypted_bin = [('0'*(encrypt_bit - i[0].__len__()) + i[0], '0'*(encrypt_bit - i[1].__len__()) + i[1])
                     for i in encrypted_bin]
    # print(encrypted_bin)
    with open(enc_file, 'w') as f:
        for i in encrypted_bin:
            print(f'{i[0]}  {i[1]}', file=f)


def Elgamal_decrypt_file(enc_file: str, sec_key_file: str, pub_key_file: str, txt_file: str):
    # print('\ndecrypted begin : \n')
    with open(enc_file, 'r') as f:
        data = f.read()
    data = data.split('\n')
    # print(data)
    data = [i.split() for i in data]
    if data[-1] == []:
        data.pop(-1)
    # print(data)
    C = [(int(i[0], 2), int(i[1], 2)) for i in data]
    # print(C)
    with open(sec_key_file, 'r') as f:
        sec_key = int(f.read())
        # print(sec_key)
    pub_key = Elgamal_pub_key_file(pub_key_file)
    # print(pub_key.__dict__)
    decrypted = [Elgamal_decrypt(i, sec_key, pub_key) for i in C]
    # print(decrypted)
    decrypted = [bin(i)[2:] for i in decrypted]
    decrypted = ['0' * (group_bit - i.__len__()) + i for i in decrypted]
    # print(decrypted)
    decrypted = ''.join(decrypted)
    decrypted = decrypted.rstrip('0')
    decrypted = decrypted[:-1]
    with open(txt_file, 'w') as f:
        f.write(decrypted)


# Elgamal_gen_key_file('secrete_key', 'public_key')
# Elgamal_encrypt_file('message_to_send.txt', 'public_key', 'encrypted.txt')
# Elgamal_decrypt_file('encrypted.txt', 'secrete_key',
#                      'public_key', 'message_recieve.txt')
