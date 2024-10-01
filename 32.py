cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

cities3 = cities.union(cities2)
print(cities3)

# cities.update(cities2)
# print(cities)

# cities3 = cities.intersection(cities2)
# print(cities3)

# cities.intersection_update(cities2)
# print(cities)

# cities3 = cities.symmetric_difference(cities2)
# print(cities3)

# cities.symmetric_difference_update(cities2)
# print(cities)

# cities3 = cities.difference(cities2)
# print(cities3)

# print(cities.difference(cities2))

# print(cities.isdisjoint(cities2))

# print(cities.issuperset(cities2))

# cities3 = {"Seoul", "Madrid"}

# print(cities.issuperset(cities3))

# cities2 = {"Delhi", "Madrid"}
# print(cities2.issubset(cities))

# cities.add("Helsinki")
# print(cities)

# cities.update(cities2)
# print(cities)

# cities4 = {"Tokyo", "Madrid", "Berlin", "Delhi, Japan"}
# cities4.remove("Tokyo")
# print(cities)

# # cities.remove("Seoul")  # Throws Error
# # print(cities)

# item = cities.pop()
# print(cities)
# print(item)

# cities4 = {"Tokyo", "Madrid", "Berlin", "Delhi, Japan"}
# del cities4  # print(cities) # Throws Error

# cities.clear()
# print(cities)

# info = {"Carla", 19, False, 5.9}
# if "Carla" in info:
#     print("Carla is present.")
# else:
#     print("Carla is absent.")