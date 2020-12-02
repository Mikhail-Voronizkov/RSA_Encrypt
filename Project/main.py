import re
import random
import math
import RSA
import primes_RNG
import matplotlib.pyplot as plt

def keygen(bitlength = 1024, filename = 'key.txt'):
    keys = RSA.RSA_keygen(bitlength)

    with open(filename, 'w') as file:
        for key in keys:
            file.write(str(key))
            file.write('\n')

    return keys


def readkey(filename):
    key = []
    with open(filename, 'r') as file:
        for line in file:
            key.append(int(line))

    return key


def encrypt(e,n,plainfile,encryptfile):
    plain = open(plainfile,'r')
    output = open(encryptfile,'w')

    try:
        for line in plain:
            encr = RSA.encrypt(e,n,line)
            for char in encr:
                output.write(str(char))
                output.write('\n')

    finally:
        plain.close()
        output.close()


def decrypt(d,n,cipherfile,plainfile):
    cipher = open(cipherfile,'r')
    output = open(plainfile,'w')

    try:
        for line in cipher:
            output.write(RSA.decrypt(d,n,[line]))

    finally:
        cipher.close()
        output.close()


def keygen_test(start,stop,step):
    assignment = 0
    comparision = 0

    assign_list = []
    comp_list = []
    key_len = []

    i = start

    while i <= stop:
        print("i = ", i)
        key_len.append(i)
        key = RSA.RSA_keygen(i,assignment,comparision)
        i += step
        assignment = key[3]
        assignment += 1
        comparision = key[4]

        assign_list.append(assignment)
        comp_list.append(comparision)
        

    return (key_len,assign_list,comp_list)


def keygen_complexity(start,stop,step):

    # y = x^2.8
    x = [i for  i in range(start,stop,step)]
    y = [a**2.8 for a in range(start,stop,step)]


    key_length,assignment,comparision = keygen_test(start,stop,step)

    # Save result
    with open('result.txt', 'w') as resultfile:
        resultfile.write('key_length,assignment,comparision\n')
    
        i = len(key_length)
        k = 0
        while k < i:
            resultfile.write(str(key_length[k]))
            resultfile.write(',')
            resultfile.write(str(assignment[k]))
            resultfile.write(',')
            resultfile.write(str(comparision[k]))
            resultfile.write('\n')
            k += 1

    # Draw plot
    plt.plot(key_length,assignment,label = "assignment")
    plt.plot(key_length,comparision,label = "comparison")
    plt.plot(x,y,label = "y = x^2.8")
    plt.xlabel("key length")
    plt.legend()
    plt.show()


# Program
def main():
    # Generate key and save it
    keygen(2048,'key.txt')

    e,n,d = readkey('key.txt')
    encrypt(e,n,'test.txt','encr.txt')
    decrypt(d,n,'encr.txt','decr.txt')
    


#main()

keygen_complexity(32,2048,32)