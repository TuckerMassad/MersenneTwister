#Author: Tucker Massad
#CSC-483
#Project 2
#crack.py

import sys
import hashlib, binascii, os
import itertools
import binascii
import time
import string
import re

#Line 1: Crack approach (1,2,3,4)
#Line 2: Known letters (if any)
#Line 3: Salt (hex)
#Line 4: Hashed password (hex)


symbols = "!@#$%^&*()-+_=`~|/?><.,"
possibleLetters = string.ascii_letters + string.digits + symbols

#starter code given by Matt to create a hash
def createHash():
    f = open("test_pass.txt","w")
    password = "fish"
    salt = os.urandom(16)
    hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    f.write("2\n")
    f.write("fish\n")
    f.write(binascii.hexlify(salt).decode('utf-8') + "\n")
    f.write(binascii.hexlify(hash).decode('utf-8') + "\n")
    print("DONE!")


#function to check if an input hash code is the same as creating a hash with the provided pw + salt
def checkHash():
    f = open("test_pass.txt", "r")
    allLines = []
    password = "fish"
    for line in f:
        allLines.append(line)
    salt = allLines[2]
    realHash = allLines[3]
    toCheck = hashlib.pbkdf2_hac('sha256', password.encode('utf-8'), salt, 100000)
    toCheckStr = binascii.hexlify(toCheck).decode()



#compare if a hash is the same as input hash
#@param filename: name of text file with password information to crack
def crackPassMethodOne(filename):
    with open(str(filename), "r") as f:
        allLines = f.read().splitlines()
    attempt = 0
    startTime = time.time()
    realpass = allLines[1].strip()
    salt = allLines[2].strip()
    salt = binascii.unhexlify(salt)
    realHash = allLines[3]
    realHash = str(realHash)
    possiblePws = itertools.product(possibleLetters, repeat = len(realpass))
    print("Please wait while your password is cracked...")
    for pw in possiblePws:
        attempt+=1
        currpw = ''.join(pw).strip()
        currhash = hashlib.pbkdf2_hmac('sha256', currpw.encode('utf-8'), salt, 100000)
        currhashStr = binascii.hexlify(currhash).decode('utf-8')
        print("current attempt: ", currpw)
        print("current hash: ", currhashStr)
        print("real hash: ", realHash)
        if currhashStr == realHash:
            endTime = time.time() - startTime
            return("SUCCESS! Password equals: ", currpw, "Found in ", attempt, " attempts. Running time = ", endTime , " seconds.")
    return("Password not found.")


#compare if a dictionary word hash is the same as input hash
#@param filename: name of text file with password information to crack
def crackPassMethodTwo(filename):
    with open(str(filename), "r") as f:
        allLines = f.read().splitlines()
    with open("/usr/share/dict/words") as d:
        allDicWords = d.read().decode('utf-8').splitlines()
    attempt = 0
    startTime = time.time()
    #realpass = allLines[1].strip()
    salt = allLines[2].strip()
    salt = binascii.unhexlify(salt)
    realHash = allLines[3]
    realHash = str(realHash)
    print("Please wait while your password is cracked...")
    for word in allDicWords:
        attempt+=1
        currpw = word
        currhash = hashlib.pbkdf2_hmac('sha256', currpw.encode('utf-8'), salt, 100000)
        currhashStr = binascii.hexlify(currhash).decode('utf-8')
        print("current attempt: ", currpw)
        print("current hash: ", currhashStr)
        print("real hash: ", realHash)
        if currhashStr == realHash:
            endTime = time.time() - startTime
            return("SUCCESS! Password equals: ", currpw, "Found in ", attempt, " attempts. Running time = ", endTime , " seconds")
    return("Password not found.")


#compare if a password with some known letters is the same as input hash
#@param filename: name of text file with password information to crack
def crackPassMethodThree(filename):
    with open(str(filename), "r") as f:
        allLines = f.read().splitlines()
    attempt = 0
    startTime = time.time()
    realpass = str(allLines[1].strip())
    possiblePws = itertools.product(possibleLetters, repeat = len(realpass))
    salt = allLines[2].strip()
    salt = binascii.unhexlify(salt)
    realHash = allLines[3]
    realHash = str(realHash)
    for char in string.punctuation:
        realpass = realpass.replace(char, ' ')
    knownLetters = []
    realpass = realpass.replace(" ", "")
    for char in realpass:
        if char != " ":
            knownLetters.append(char)
    print("Please wait while your password is cracked...")
    for pw in possiblePws:
        attempt+=1
        if checkContainsLetters(knownLetters, pw) == True:
            currpw = ''.join(pw).strip()
            currhash = hashlib.pbkdf2_hmac('sha256', currpw.encode('utf-8'), salt, 100000)
            currhashStr = binascii.hexlify(currhash).decode('utf-8')
            print("current attempt: ", currpw)
            print("current hash: ", currhashStr)
            print("real hash: ", realHash)
            if currhashStr == realHash:
                endTime = time.time() - startTime
                return("SUCCESS! Password equals: ", currpw, "Found in ", attempt, " attempts. Running time = ", int(endTime) , "seconds.")
    return("Password not found.")


#helper function to check if a word contains all possible letters)
#@param letters: list of known letters of password
#@param word: string to check if contains all letters in list
def checkContainsLetters(letters, word):
    for letter in letters:
        #print("checking if letter ", letter , " is in ", word)
        if letter not in word:
            return False
    return True

#main method
def main():
    print("Welcome to Tucker's password cracker!\n")
    fileInput = raw_input("Please enter the filename of the file you'd like to crack (please include '.txt' at the end): ")
    with open(str(fileInput), "r") as f:
        allLines = f.read().splitlines()
    if(allLines[0] == str(1)):
        print(crackPassMethodOne(fileInput))
    elif(allLines[0] == str(2)):
        print(crackPassMethodTwo(fileInput))
    elif(allLines[0] == str(3)):
        print(crackPassMethodThree(fileInput))
    else:
        print("Invalid testfile format!")


#print(checkContainsLetters(["o", "p", "k"], "angaroop"))
#createHash()
print(main())

#print(crackPassMethodThree("test_pass.txt"))
#print(crackMethodOne("k@sh"))


#print passwordfile


