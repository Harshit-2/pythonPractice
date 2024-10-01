with open('file.txt', 'r') as f:
    f.seek(10)  # Move to the 10th byte in the file
    data = f.read(5)    # Read the next 5 bytes
    print(data)