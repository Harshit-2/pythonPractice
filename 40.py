# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode


import random
import string

operation = input("Enter operation (encode/decode): ")
if (operation == "encode"):

    string1 = input("Enter string to encode: ")
    if len(string1) < 3:
        print(string1[::-1])    # to reverse a string

    else:
        string2 = string1[1:len(string1)]+string1[0]    # To slice the first letter and attch it to the end

        rand1 = (random.choice(string.ascii_letters))
        rand2 = (random.choice(string.ascii_letters))
        rand3 = (random.choice(string.ascii_letters))
        rand4 = (random.choice(string.ascii_letters))
        rand5 = (random.choice(string.ascii_letters))
        rand6 = (random.choice(string.ascii_letters))

        final = rand1 + rand2 + rand3 + string2 + rand4 + rand5 + rand6    # To add random characters to the main string
        print(final)

elif (operation == "decode"):

    string3 = input("Enter string to decode: ")     # Enter a decoded string
    
    if len(string3) <= 8:
        print(string3[::-1])    # to reverse a string

    else:
        string4 = string3[3:len(string3)-3]       # remove first 3 and last 3 characters
        store = string4[0:len(string4)-1]     # store it in a variable
        fLetter = string4[len(string4)-1:len(string4)]        # store the first character
        print(fLetter+store)      # concat

else:
    print("Enter a valid operation")
