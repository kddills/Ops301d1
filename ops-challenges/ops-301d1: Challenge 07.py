# Script Name:            Ops Challenge 07
# Author:                 Kimberly Dills
# Date of last revision:  9/8/2020
# Description of purpose: To utilize commands that's available in bash using python script file

# Bringing os library

import os

# Declaration of variables:

userInput = input("what directory do you want to go into ? ")

# Putting users imput from the user and display all the files within user's input directory.

def printUsersInput(userinput):
    for (root, dirs, files) in os.walk(userInput):
        print(root)
        intoText(root)
        print(dirs)
        intoText(dirs)
        print(files)
        intoText(files)

# Put all the outputs into the text files
def intoText(texts):
    fileWrite = open("./output.txt" , 'a')
    fileWrite.writelines(texts)
    fileWrite.write("")
    fileWrite.close()

# Main

printUsersInput(userInput)

# End

