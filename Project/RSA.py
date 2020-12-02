import primes_RNG
import math
import random
import sys

sys.setrecursionlimit(5000)


def egcd(a, b):
    """
    Euclid's extended algorithm for finding the multiplicative inverse of two numbers
    """
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    """
    Return inverse moudle
    """
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m




def RSA_keygen(n=1024,assignment = 0,comparision = 0):
 
    # step 1: Generate 2 random primes p & q
    #print("> Generate p")
    pcount = primes_RNG.generate_primes(n=n, k=1, assign = assignment, comp = comparision)
    p = pcount[0][0]
    
    assignment = pcount[1]
    assignment += 1
    comparision = pcount[2]

    #print("> Generate q")
    qcount = primes_RNG.generate_primes(n=n, k=1, assign = assignment, comp = comparision)
    q = qcount[0][0]

    
    assignment = qcount[1]
    assignment += 1
    comparision = qcount[2]

    # step 2: Find public key n
    n = p * q
    assignment += 1


    # step 3
    phi_n = (p - 1) * (q - 1)
    assignment += 1

    # step 4 and step 5: Find private key d
    while True:
        comparision += 1 # True compare
        e = random.randrange(1, phi_n-1)
        assignment += 1
        comparision += 1 # if compare
        if math.gcd(e, phi_n) == 1:
            # step 5
            gcd, s, t = egcd(phi_n, e)
            assignment += 3
            comparision += 1 # if compare
            if gcd == (s*phi_n + t*e):
                d = t % phi_n
                assignment += 1
                break
    comparision += 1 # True compare
    return (e, n, d, assignment, comparision)


def encrypt(e,n, plaintext):
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    #cipher = [(ord(char) ** e) % n for char in plaintext]
    cipher =[primes_RNG.square_and_multiply(ord(char),e,n) for char in plaintext]

    
    #Return the array of bytes
    return cipher



def decrypt(d,n, ciphertext):
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    #plain = [chr((ord(char) ** d) % n) for char in ciphertext]

    plain = [chr(primes_RNG.square_and_multiply(int(char),d,n)) for char in ciphertext]

    #Return the array of bytes as a string
    return ''.join(plain)
