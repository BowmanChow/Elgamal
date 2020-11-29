from random import *
import math

prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449,
              457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013]


def is_prime_fermat(p: int) -> bool:
    if p == 1:
        return False
    elif p <= 0:
        raise Exception("input must be positive")
    if p in prime_list:
        return True
    for a in range(2, 20):
        if a**(p-1) % p != 1:
            return False
    return True


def even_decomposite(q: int) -> tuple:
    # return r, d
    # q = 2^r * d
    if q - math.floor(q) != 0:
        raise Exception('input must be int')
    r = 0
    d = q
    while(True):
        if d % 2 == 1:
            return r, int(d)
        d /= 2
        r += 1


def is_prime_miller_rabin(p: int) -> bool:
    r, d = even_decomposite(p - 1)
    evidents = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    for a in evidents:
        if a >= p:
            break
        is_prime = False
        residue = pow(a, d, p)
        if residue == 1:
            is_prime = True
            break
        for r_k in range(r):
            if residue == p - 1:
                is_prime = True
                break
            else:
                residue = residue**2 % p
        if not is_prime:
            return is_prime
    return True


def is_prime(p: int) -> bool:
    small_prime = [2, 3, 5, 7, 11, 13, 17, 19]
    if p <= 1:
        return False
    elif p <= small_prime[-1]:
        if p in small_prime:
            return True
        else:
            return False
    else:
        for sp in small_prime:
            if p % sp == 0:
                return False
    return is_prime_miller_rabin(p)


# print(find_generator(Q))
# for i in range(1, 10000):
#     if is_prime_miller_rabin(i):
#         print(f"{i} \t {is_prime_miller_rabin(i)}  \t  ", end='')

# print(even_decomposite(28.0))


def generate_prime(low_bound: int, high_bound: int) -> int:
    if high_bound < low_bound:
        raise Exception('high_bound should be bigger than low_bound')
    Q = randint(low_bound, high_bound)
    while(not is_prime(Q)):
        Q = randint(low_bound, high_bound)
        # print(f'{Q}')
    return Q
