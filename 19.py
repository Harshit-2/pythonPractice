for i in range(1, 12):
    if (i == 11):
        print("Loop ko chodkar nikal gaya")
        break
    print("5 X", i, "=", 5 * i)

print()


for i in range(12):
    if (i == 10):
        print("Skip the iteration")
        continue
    print("5 *", i+1, "=", 5 * (i+1))

print()


i = 0
while True:
    print(i, end=", ")
    i = i + 1
    if (i % 12 == 0):
        break
