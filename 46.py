import os

if(not os.path.exists("data")):
    os.mkdir("data")    # To create a folder

for i in range(0, 100):
    os.mkdir(f"data/Day{i+1}")
