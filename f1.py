file_open = open("file.txt", "r")
file_content = file_open.read()
print(file_content)
file_open.close() # it's a good practice to close a file
