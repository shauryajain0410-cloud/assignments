#q1 ---> open function is used to open a file. The different modes of opening a file are "r" as in reading mode , "w" as in writing mode , if the file already exists , it overwrites the whole data , "a" as in appending at the last , "wb" as in storing the values in binary form , "rb" as in reading in binary file
#q2 ---> without using the close function , we cant see the things written in the file , the data would be available after closing the file only
#q3 
f = open("text.txt" , "w")
f.write("I want to become a Data Scientist")
f.close()

f = open("text.txt","r")
f.read()

#q4 ---> read(): Reads the entire file content at once as a single string, readline(): Reads a single line from the file, ending with a newline character (\n), readlines(): Reads all lines in the file and returns them as a list of individual strings.

#q5 ---> we use with statement with open becuase it automatically handles the opening and closing. As soon as the code block ends , the file closes

#q6 ---> write(): inserts a single string into a file, writelines():  inserts an iterable sequence of strings (such as a list) at once

with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Welcome to Python file handling.\n")

    lines_to_add = [
    "This is line number three.\n",
    "This is line number four.\n",
    "This is the final line."]

    with open("example.txt", "a") as file:
      file.writelines(lines_to_add)