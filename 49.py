# READING A FILE

# f = open('myfile.txt', 'r')
f = open('myfile.md', 'rb')     # b is written to open the file in binary format
# print(f)
text = f.read()
print(text)
f.close()
