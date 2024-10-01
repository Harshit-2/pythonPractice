tup = (1, 2, 76, 342, 32, "green", True)
# tup[0] = 90
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])

if 3421 in tup:
    print("Yes 342 is present in this tuple")
tup2 = tup[1:4]
print(tup2)


tuple1 = (1, 2, 2, 3, 5, 4, 6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)

details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details)

country = ("Spain", "Italy", "India",)
#            [0]      [1]      [2]
print(country[0])
print(country[1])
print(country[2])

country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
print(country[-1])  # Similar to print(country[len(country) - 1])
print(country[-3])
print(country[-4])

if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")

if "Russia" in country:
    print("Russia is present.")
else:
    print("Russia is absent.")

animals = ("cat", "dog", "bat", "mouse", "pig",
           "horse", "donkey", "goat", "cow")
print(animals[3:7])  # using positive indexes
print(animals[-7:-2])  # using negative indexes
print(animals[4:])  # using positive indexes
print(animals[-4:])  # using negative indexes
print(animals[:6])  # using positive indexes
print(animals[:-3])  # using negative indexes
print(animals[::2])  # using positive indexes       Used to slice a tuple and returns a new tuple containing every second element of tuple starting from the first element.
print(animals[-8:-1:2])  # using negative indexes
print(animals[1:8:3])
