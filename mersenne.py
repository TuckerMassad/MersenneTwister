#Author: Tucker Massad
#CSC-483
#Project 2
#mersenne.py

import sys
import hashlib, binascii, os
import itertools
import string
import datetime
import binascii
import time
import string
import re
import random
import os, binascii
from binascii import hexlify, unhexlify


N = 624
M = 397
A = 0x9908b0df
UpperBound = 0x80000000
LowerBound = 0x7fffffff
m = list(range(0, N))
mi = N

#symbols = "!`.,"
possibleLetters = string.ascii_letters# + string.digits# + symbols

#set the seed #
def setSeed(seed):
    global mi
    m[0] = seed & 0xffffff
    for i in range(1, len(m)):
        m[i] = (69069 * m[i-1] & 0xffffff)
    mi = N


#generate a random int
def nextInt():
    global mi
    if mi >= N:
        for k in range(0, N-1):
            y = (m[k] & UpperBound) | (m[(k+1) % N] & LowerBound)
            m[k] = m[(k + M) % N] ^ (y >> 1)
            if y % 2 == 1:
                m[k] = m[k] ^ A
        mi = 0
    y = m[mi]
    mi += 1
    y = y ^ (y >> 11)
    y = y ^ ((y << 7) & 0x9d2c5680)
    y = y ^ ((y << 15) & 0xfc60000)
    y = y ^ (y >> 18)
    return(y)


#create random vector # to seed PRG
def createRandomVector():
    randomVect = hex(int(random.random() * 1000))
    return randomVect



#encrypt a message given a key and vector
def encrypt(key, vector, eavesdrop):

    #print("Secret Key : ", key)
    #print("Vector : ", vector)
    if eavesdrop == False:
        ciphertext = raw_input("Please enter the message you'd like to encrypt: ")
    else:
        ciphertext = raw_input("Encrypting and eavesdropping beginning!")

    returntext = []

    keyHexxed = binascii.hexlify(key)
    vectorHexxed = binascii.hexlify(vector)

    seedSetter = int(keyHexxed, 16) ^ int(vectorHexxed, 16)


    setSeed(seedSetter)


    for letter in ciphertext:
        letter = int(hexlify(letter), 16)
        newNum = nextInt()
        #print(newNum)
        returntext.append(letter^newNum)


    return returntext


#decrypt a message given a key, vector, and ciphortext
def decrypt(key, vector, ciphertext):

    keyHexxed = binascii.hexlify(key)
    vectorHexxed = binascii.hexlify(vector)

    seedSetter = int(keyHexxed, 16) ^ int(vectorHexxed, 16)

    setSeed(seedSetter)

    finalReturn = []

    for letter in ciphertext:
        newNum = nextInt()
        print("Decrypting letter " + str(letter) + "with current seed " + str(newNum))
        letter = letter ^ newNum
        finalReturn.append(unhexlify(format(letter, '02x')))


    return finalReturn


#attempt to obtain a message given a vector and ciphertext
def eavesdrop(vector, ciphertext):

    vectorHexxed = binascii.hexlify(vector)

    with open("/usr/share/dict/words") as d:
        allDicWords = d.read().decode('utf-8').splitlines()

    longestPoss = 0

    while longestPoss < 10:
        possibleKeys = itertools.product(possibleLetters, repeat=longestPoss)
        for key in possibleKeys:
            print("current key: ", ''.join(key))
            if ''.join(key) in allDicWords:
                for letter in key:
                    print("Letter = ", letter)
                    decryptedWord = decrypt(letter, vector, ciphertext)
                    #print decryptedWord
                    #print("SUCCESSFUL WORD FIND!")

        longestPoss+=1







# secretkey = "it"
# vector = createRandomVector()
# #
# #
# encryptedmessage = encrypt(secretkey, vector, eavesdrop=False)
# print("Encrypted message = ", encryptedmessage)
# decryptedmessage = decrypt(secretkey, vector, encryptedmessage)
# print("Decrypted message = ", ''.join(decryptedmessage))
#
# eavesdrop(vector, encryptedmessage)




#eavesdrop(vector, "test")



# setSeed(100)
# print(nextInt())
# setSeed(100)
# print(nextInt())

#print(decrypt(secretkey, vector, str(encryptedmessage)))