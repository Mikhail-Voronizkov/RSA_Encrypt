import re
import random
import math
import RSA
import primes_RNG
import matplotlib.pyplot as plt

def keygen(bitlength = 1024, filename = 'key.txt'):
    keys = RSA.RSA_keygen(bitlength)

    with open(filename, 'w') as file:
        #for key in keys:
            #file.write(str(key))
            #file.write('\n')

        file.write(str(keys[0]))
        file.write('\n')
        file.write(str(keys[1]))
        file.write('\n')
        file.write(str(keys[2]))

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
        # Program
        for line in plain:
            encr = RSA.encrypt(e,n,line)
            for char in encr:
                output.write(str(char))
                output.write('\n')

        # For testing complexity
        #assignment = 0
        #comparision = 0
        #for line in plain:
            #encr,assign,comp = RSA.encrypt(e,n,line)
            #assignment += assign
            #comparision += comp
            #for char in encr:
                #output.write(str(char))
                #output.write('\n')

    finally:
        plain.close()
        output.close()
        #return (assignment,comparision)


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


def encrypt_test(plainfile,destfile):
    """
    Key file: 
        e = first line
        n = second line
        d = third line
    Key file name: key_<bit length>.txt
    """
    with open('encrypt_result.txt', 'w') as resultfile:
        resultfile.write('key_length,assignment,comparision\n')


    assign_list = []
    comp_list = []
    key_len = []

    name = 'key'
    filename = ''
    for i in range(32,2049,32):
        key_len.append(i)
        print('i =', i)
        filename += name + '_' + str(i) + '.txt'
        # encrypt
        e,n,d = readkey(filename)
        assignment,comparision = encrypt(e,n,plainfile,destfile)
        assign_list.append(assignment)
        comp_list.append(comparision)   

        filename = ''

    return (key_len,assign_list,comp_list)


def encrypt_complexity(plainfile,destfile):
    # y = x^2
    x = [i for  i in range(32,2049,32)]
    y = [a**2 for a in range(32,2049,32)]


    key_length,assignment,comparision = encrypt_test(plainfile,destfile)

    # Save result
    with open('encrypt_result.txt', 'w') as resultfile:
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
    #plt.plot(x,y,label = "y = x^2")
    plt.xlabel("Number of character")
    plt.legend()
    plt.show()

# Program
def main():
    # Generate key and save it
    #keygen(1024,'key.txt')

    e,n,d = readkey('key_1.txt')
    encrypt(e,n,'plain_100.txt','encr.txt')
    decrypt(d,n,'encr.txt','decr.txt')
    


main()

#keygen_complexity(32,2048,32)
#encrypt_complexity('plain_100.txt','encrypt.txt')