from extend_euclid import extend_euclid
import numpy as np
import math
from random import *
from prime import *

max_bit_length = 52


def find_generator(Q: int, num: int = 1) -> list:
    # find 2*Q + 1 's
    p = 2 * Q + 1
    generator_list = []
    for i in range(2, p):
        if pow(i, 2, p) != 1 and pow(i, Q, p) != 1:
            generator_list.append(i)
            if generator_list.__len__() >= num:
                break

    return generator_list


def generate_double_prime(low_bound: int, high_bound: int) -> tuple:
    if high_bound < low_bound:
        raise Exception('high_bound should be bigger than low_bound')
    Q = generate_prime(low_bound, high_bound)
    p = 2 * Q + 1
    while(not (is_prime(p) and is_prime(Q))):
        Q = randint(low_bound, high_bound)
        p = 2 * Q + 1
        # print(f'Q = {Q} , p = {p}')
    return Q, p


class Elgamal_public_key:
    def __init__(self, prime, generator, public_key):
        self.prime = prime
        self.generator = generator
        self.public_key = public_key


def Elgamal_gen_key():
    small_prime, big_prime = generate_double_prime(
        2**max_bit_length, 2**(max_bit_length+1))
    # print(small_prime, big_prime)
    generator = find_generator(small_prime)[0]
    # print(f'generator = {generator}')
    secret_key = randint(1, big_prime - 1)
    # print(f'secret_key = {secret_key}')
    public_key = pow(generator, secret_key, big_prime)
    # print(f'pulbic_key = {public_key}')
    return secret_key, Elgamal_public_key(big_prime, generator, public_key)


def Elgamal_encrypt(plain_text: int, public_key: Elgamal_public_key) -> int:
    k = randint(1, public_key.prime - 1)
    Key_tmp = pow(public_key.public_key, k, public_key.prime)
    # print(f'Key_tmp = {Key_tmp}')
    C1 = pow(public_key.generator, k, public_key.prime)
    C2 = Key_tmp * plain_text % public_key.prime
    return C1, C2


def Elgamal_decrypt(encrypted: tuple, secret_key: int, public_key) -> int:
    Key_recieve = pow(encrypted[0], secret_key, public_key.prime)
    # print(f'Key recieved = {Key_recieve}')
    plain_text = encrypted[1] * \
        pow(Key_recieve, public_key.prime-2,
            public_key.prime) % public_key.prime
    return plain_text
