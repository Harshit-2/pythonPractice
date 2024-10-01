def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(round(mean,3))


def isGreater(a, b):
    if (a > b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")


def isLesser(a, b):
    pass


a = 9
b = 8
isGreater(a, b)
calculateGmean(a, b)

c = 8
d = 74
isGreater(c, d)
calculateGmean(c, d)
