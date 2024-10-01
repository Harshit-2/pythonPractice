import os 
folders = os.listdir("data")

print(os.getcwd())      # To get the current working directory
# os.chdir("/Users")    # To change the current working directory
print(os.getcwd())

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))   # To get the list of files in a folder