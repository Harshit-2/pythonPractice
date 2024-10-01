for i in range(5):
    print(i, end="  ")
else:
    print('Loop completed')

for i in range(5):
    print(i, end="  ")
    if i == 3:
        break
else:
    print('Loop completed')

print()

j = 0
while j < 7:
    print(j, end="  ")
    j += 1
else:
    print('Loop completed')
