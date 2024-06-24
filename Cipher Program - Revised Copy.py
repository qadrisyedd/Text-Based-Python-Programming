'''
Author: Syed Qadri
Date: November 15, 2023
Prgram: Security Pin Cipher
'''

#Import
import random, string, math, time

#Setting up lists (char)
letters=string.ascii_lowercase
letters=list(letters)

#Program Title
print("-------------------")
print("Security Pin Cipher")
print("-------------------")
print("")

#Main
def menu(): #Menu
    print("Please Select One Of The Following Options:")
    print("1 - Encrypt a Message") #Choice 1
    print("2 - Decrypt a Message") #Choice 2
    print("3 - Quit the Program") #Force Quit Prog
    print("")

#Encryption Code; (Choice 1)
def choice1():
    message1=input("Enter a message you would like to encrypt: ")
    global cipher
    cipher=""
    if message1.isascii() and message1.islower():
        pin1()
        pinindex = 0
        index=0
        for letter in message1:
            if letter != " ":
                x = letters.index(letter) + 1
                y = int(pswd[pinindex])
                index= x + y
                if index>26:
                    index=index-26
                pinindex += 1
                if pinindex == 4:
                    pinindex = 0
                cipher+=letters[index - 1]
            else:
                cipher+=" "
        print("Your encrypted code is: "+cipher)
        time.sleep(2)
        print("")
    else:
        print("Invalid message! All characters must be lowercase. No numbers or special characters allowed.")
        time.sleep(1.5)
        print()
        choice1()

#Password for Encrypting Cipher
def pin1():
    global pswd
    pswd = input("Enter a 4-digit Pin: ")
    if pswd.isdigit() and len(pswd)==4:
        print("")
    else:
        print("Invalid Input. Choose a 4-digit PIN.")
        time.sleep(1)
        print("")
        pin1()

#Decryption Code; (Choice 2)
def choice2():
    message2 = input("Enter the message you would like to decrypt: ")
    global uncipher
    uncipher = ""
    if message2.isascii() and message2.islower():
        pin2()
        pinindex1=0
        index1=0
        for letter in message2:
            if letter != " ":
                index1=letters.index(letter)+1 - int(pswd1[pinindex1])
                pinindex1 += 1
                if pinindex1 == 4:
                   pinindex1 = 0
                uncipher += letters[index1 - 1]
            else:
                uncipher+=" "
        print("Your decrypted code is: "+uncipher)
        time.sleep(2)
        print("")
    else:
        print("Invalid message! All characters must be lowercase. No numbers or special characters allowed.")
        time.sleep(1.5)
        print()
        choice2()

#Password for Decrypting Cipher
def pin2():
    global pswd1
    pswd1 = input("Enter your 4-digit Pin: ")
    if pswd1.isdigit() and len(pswd1)==4:
        print("")
    else:
        print("Invalid Input. Enter a 4-digit decription PIN.")
        time.sleep(1)
        print()
        pin2()

#Start Prog Logic
menu()
choice=input("Enter your choice: ")

#Portal(Menu)
while choice!="3":
    #Encryption Connect
    if choice=="1":
        choice1()
    #Decryption Connect
    elif choice=="2":
        choice2()
    #Valid Entery for Choice
    else:
        print("Invalid choice! Enter a number between 1-3")
        time.sleep(1.7)
    print()
    menu()
    choice=input("Enter your choice: ")

#Force Quit Prog
print("")
print("Thanks for using this program. Goodbye!")
print("Created By: Syed Qadri")
time.sleep(3)
quit