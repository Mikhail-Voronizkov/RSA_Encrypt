import re
import random
import math


def square_and_multiply(x, k, p=None,assignment=0,comparision=0):
    """
    Square and Multiply Algorithm
    Parameters: positive integer x and integer exponent k,
                optional modulus p
    Returns: x**k or x**k mod p when p is given
    """
    b = bin(k).lstrip('0b')
    r = 1
    assignment += 2
    for i in b:
        comparision += 1
        r = r**2
        assignment += 1
        comparision += 2
        if i == '1':
            r = r * x
            assignment += 1
        if p:
            r %= p
            assignment += 1

    comparision += 1
    return (r,assignment,comparision)

def miller_rabin_primality_test(p, s=5, assignment = 0, comparision = 0):
    comparision += 1
    if p == 2: # 2 is the only prime that is even
        return (True,assignment,comparision)
    comparision += 1
    if not (p & 1): # n is a even number and can't be prime
        return (False,assignment,comparision)

    p1 = p - 1
    u = 0
    r = p1  # p-1 = 2**u * r
    assignment += 3

    while r % 2 == 0:
        comparision += 1
        r >>= 1
        u += 1
        assignment += 2

    comparision += 1

    # at this stage p-1 = 2**u * r  holds
    comparision += 1
    assert p-1 == 2**u * r

    def witness(a, assign, comp):
        """
        Returns: True, if there is a witness that p is not prime.
                False, when p might be prime
        """
        z,a,c = square_and_multiply(a, r, p)
        assign += a
        assign += 1
        comp += c
        comp += 1
        if z == 1:
            return (False,assign,comp)

        for i in range(u):
            comp += 1
            z,a,c = square_and_multiply(a, 2**i * r, p)
            assign += a
            assign += 1
            comp += c
            comp += 1
            if z == p1:
                return (False,assign,comp)

        comp += 1
        return (True,assign,comp)

    
    for j in range(s):
        comparision += 1
        a = random.randrange(2, p-2)
        assignment += 1
        flag, assignment, comparision = witness(a,assignment,comparision)
        comparision += 1
        if flag:
            return (False,assignment,comparision)

    comparision += 1
    return (True,assignment,comparision)

def generate_primes(n=1024, k=1, assign = 0, comp = 0):
    """
    Generates prime numbers with bitlength n.
    Stops after the generation of k prime numbers.

    Caution: The numbers tested for primality start at
    a random place, but the tests are drawn with the integers
    following from the random start.
    """
    comp += 1
    assert k > 0
    comp += 1
    assert n > 0 and n < 4096

    # follows from the prime number theorem
    necessary_steps = math.floor( math.log(2**n) / 2 )
    assign += 1
    # get n random bits as our first number to test for primality
    x = random.getrandbits(n)
    assign += 1

    primes = []

    while k>0:
        comp += 1
        flag, assign, comp = miller_rabin_primality_test(x, s = 16, assignment = assign, comparision = comp)
        comp += 1
        if flag:
            primes.append(x)
            k = k-1
            assign += 1

        
        x = x+1
        assign += 1

    comp += 1

    return (primes,assign,comp)




