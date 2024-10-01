# Write a program to pronounce list of names using win32 API. If you are given a list l as follows:
# l = ["Rahul", "Nishant", "Harry"]


# Your program should pronouce:

# Shoutout to Rahul
# Shoutout to Nishant
# Shoutout to Harry


# Note: If you are not using windows, try to figure out how to do the same thing using some other package

import win32com.client


speaker = win32com.client.Dispatch("SAPI.SpVoice")

list1 = ["Marina", "Arin", "Sneha", "Ananya", "Simran"]

for index, name in enumerate(list1):
    list1[index] = "Shoutout to " + name

print(list1)
speaker.Speak(list1)

# print("Enter the word you want to speak it out by computer")
# s = input()
