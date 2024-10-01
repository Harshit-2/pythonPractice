with open('sample.txt', 'w') as f:
    f.write('Hello World!')
    f.truncate(5)

with open('sample.txt', 'r') as f:
    print(f.read())
