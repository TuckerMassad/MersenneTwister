#Author: Tucker Massad
#CSC-483
#Project 2
#demo.py

import mersenne
import crack

def main():
    print("Welcome to Tucker's Project 2 demo!\n Functionalities: \n 1 - PRG \n 2 - Generate test password file \n 3 - encrypt/decrypt \n 4 - Brute Force Password Cracker")
    input = raw_input("Please enter a corresponding number to begin: ")

    if input == "1":
        print("Welcome to Tucker's PRG!")
        desiredSeed = raw_input("To generate a few random numbers, please enter a desired int seed number (digits only): ")
        desiredAmount = int(raw_input("Please enter the amount of random numbers you'd like to generate: "))
        mersenne.setSeed(int(desiredSeed))
        for i in range(desiredAmount):
            number = mersenne.nextInt()
            print("Random number = " + str(number))

        return("Complete!")

    elif input == "2":
        print("Welcome to Tucker's password test file generator!")
        desiredPassword = raw_input("Please enter a desired password for the test file: ")
        crack.createHash(desiredPassword)
        print("Test file written to test_pass.txt !")


    elif input == "3":
        print("Welcome to Tucker's Message Encryption/Decryption Demo!")
        inputKey = raw_input("Please enter a secret key you'd like to encrypt with (can be both numbers & letters): ")
        secretkey = inputKey
        vector = mersenne.createRandomVector()
        encryptedMessage = mersenne.encrypt(secretkey, vector, eavesdrop=False)
        print("Encryption by letter : ", encryptedMessage)
        print("Full encrypted message text = ", ''.join(str(s) for s in encryptedMessage))
        input = raw_input("Would you like to decrypt this message? Enter (Yes/No): ")
        if input == "Yes" or "yes":
            decryptedList = mersenne.decrypt(secretkey, vector, encryptedMessage)
            print("Extracted letters after decryption: " + str(decryptedList))
            print("Full message = " + ''.join(decryptedList))
        else:
            print("Complete!")

    elif input == "4":
        print("Welcome to Tucker's Brute Force Password Cracker! \n")
        input = raw_input("Have you created a test file yet? (Enter Yes/No)")
        if input.lower() == "yes":
            crack.crackPassMethodOne("test_pass.txt")
        else:
            print("Please make a test file and run again!")

    else:
        print("Invalid selection!")




main()