dic = {
    344: "Harry",
    56: "Rajat",
    678: "Harshit",
    567: "Sneha"
}

print(dic[567])

info = {'name': 'Karan', 'age': 19, 'eligible': True}

print(info)

print(info['name'])  # Accessing single values  # This will give error if the key is not present

print(info.get('eligible'))  # Accessing single values  # This will not give error if the key is not present

print(info.values())    # Accessing multiple values

print(info.keys())  # Accessing keys

print(info.items())  # Accessing key-value pairs

for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")

print()

for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")
