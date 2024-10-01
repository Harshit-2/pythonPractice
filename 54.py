a = None    # is will return => True
b = None    # == will return => True

a = (1, 2)  # is will return => True
b = (1, 2)  # == will return => True

a = 3   # is will return => True
b = 3   # == will return => True

a = "Japan"   # is will return => True
b = "Japan"   # == will return => True

a = [5, 2, 8]   # is will return => False
b = [5, 2, 8]   # == will return => True

a = 5   # is will return => False
b = "5" # == will return => False

print(a is b)  # exact location of object in memory
print(a is None)  # exact location of object in memory
print(a == b)  # value


#   ★ Clink: In case of a = 3 b = 3 is returned true because both a and b were pointing to the same location as both are constants and can't be changed, so python created them in the same memory location same goes for a = "Japan" b = "Japan", a = (1, 2) b = (1, 2) & a = None b = None
