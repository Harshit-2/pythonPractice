def avg1(a, b):
    '''Required arguments: a, b'''
    return (a + b) / 2

def avg2(a=2, b=4):
    '''Default arguments: a, b'''
    return (a + b) / 2

def avg3(a, b=4):
    '''Keyword arguments: a, b'''
    return (a + b) / 2

def avg4(*nums):
    '''Variable length arguments'''
    print(type(nums))
    sum = 0
    for i in nums:
        sum = sum + i
    return sum / len(nums)

print(avg1(8, 4), avg1.__doc__)
print(avg2(), avg2.__doc__)
print(avg3(b=2, a=5), avg3.__doc__)
print(avg4(2, 4, 6, 8), avg4.__doc__)
