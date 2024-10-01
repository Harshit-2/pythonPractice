# WRITING A FILE

f = open('myfile2.md', 'a')
f.write('Hello, world!\n')
f.close()

with open('myfile2.md', 'a') as f:
    f.write("Hey I am inside with\n\t-It does not require a close function")
