# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water. Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.

#                 S W G
# computer =      0 1 2
# player =  S  0  D W L
#           W  1  L D W
#           G  2  W L D


import random


def check(comp, user):
    if comp == user:
        return 0

    if (comp == 0 and user == 1):
        return -1

    if (comp == 1 and user == 2):
        return -1

    if (comp == 2 and user == 0):
        return -1

    if (user > 2):
        return 404

    return 1


comp = random.randint(0, 2)
user = int(input("0 for Snake, 1 for water and 2 for Gun:\n"))

score = check(comp, user)

print("You: ", user)
print("Computer: ", comp)

if (score == 0):
    print("Its a draw")

elif (score == -1):
    print("You Lose")

elif (score == 404):
    print("Enter a number from 0-2")

else:
    print("You Won")



# MY CODE
# import random

# print("-1=> Snake, 0=> Water, 1=> Gun")
# computer = random.randint(-1, 1)
# user = int(input("Enter a number from -1, 0, 1:\n"))
# # print(computer)

# if computer == user:
#     print("Draw")

# elif computer == -1 and user == 0:
#     print("You Loose")

# elif computer == -1 and user == 1:
#     print("You Won")

# elif computer == 0 and user == -1:
#     print("You Won")

# elif computer == 0 and user == 1:
#     print("You Loose")

# elif computer == 1 and user == -1:
#     print("You Loose")

# elif computer == 1 and user == 0:
#     print("You Won")

# else:
#     print("Enter a valid number")
