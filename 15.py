# Exercise 2 => Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. Here is a sample program and documentation link for you:

# import time
# timeStamp = time.strftime('%H:%M:%S')
# print(timeStamp)
# timestamp = time.strftime('Hours: %H')
# print(timestamp)
# timestamp = time.strftime('Minutes: %M')
# print(timestamp)
# timestamp = time.strftime('Seconds: %S')
# print(timestamp)


# https://docs.python.org/3/library/time.html#time.strftime


import time
t = time.strftime('%H:%M:%S') 
hour = int(time.strftime('%H'))
# hour = int(input("Enter hour: "))
# print(hour)

if(hour>=0 and hour<12):
  print("Good Morning!")
elif(hour>=12 and hour<17):
  print("Good Afternoon!")
elif(hour>=17 and hour<0):
  print("Good Night!")
