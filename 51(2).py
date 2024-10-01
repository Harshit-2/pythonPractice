with open('file.txt', 'r') as f:
    data = f.read(10)   # Read the first 10 bytes
    current_position = f.tell() # Save the current position
    f.seek(current_position)    # Seek to the saved position
    print(current_position)