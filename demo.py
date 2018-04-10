#Author: Tucker Massad
#CSC-483
#Project 2
#demo.py

import mersenne

def main():
    print("Welcome to Tucker's Project 2 demo!\n Functionalities: \n 1 - PRG \n 2 - encrypt/decrypt \n 3 - eavesdrop")
    input = raw_input("Please enter a corresponding number to begin: ")
    if input == "1":
        print("Welcome to Tucker's PRG!")
        desiredSeed = raw_input("To generate a few random numbers, please enter a desired int seed number: ")
        desiredAmount = int(raw_input("Please enter the amount of random numbers you'd like to generate: "))
        mersenne.setSeed(int(desiredSeed))
        for i in range(desiredAmount):
            number = mersenne.nextInt()
            print("Random number = ", number)

        return("Complete!")

    elif input == "2":
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
            print("Extracted letters after decryption", decryptedList)
            print("Full message = ", ''.join(decryptedList))
        else:
            print("Complete!")

    elif input == "3":
        print("Welcome to Tucker's Eavesdropper Demo!")
        inputKey = raw_input("Please enter a message you'd like to attempt to encrypt and attempt to find without the use of a secret key: ")
        secretkey = "doesn't matter"
        vector = mersenne.createRandomVector()
        encryptedMessage = mersenne.encrypt(secretkey, vector, eavesdrop=True)
        mersenne.eavesdrop(vector, encryptedMessage)
    else:
        print("Invalid selection!")




print(main())