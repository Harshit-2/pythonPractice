i = 0
while (i < 10):
    print(i, end=", ")
    i = i+1
print("\n")

count = 5
while (count > 0):
    print(count)
    count = count - 1

else:
    print("I am inside else")

print()


# Emulate do-while loop in Python

while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if not number > 0:
        break
