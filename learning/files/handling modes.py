# Open a new file named "example.txt" in write mode
# with open("learning/files/handling modes.txt", "w") as file:
#     # Write some text to the file
#     file.write("Hello, world!\n")
#     file.write("This is a text file created using Python.\n")
#     file.write("I hope you find this demo helpful!\n")
    
# Print a message to confirm that the file was created
# print("The file 'example.txt' has been created and written to.")

# with open("learning/files/handling modes.txt", "a+") as f:
#     f.write('2nd iteration\n')
#     f.write('4rd\n')


# filename = 'learning/files/handling modes.txt'
# string_to_delete = '4rd' #deletes all string occurrences 

# # Read the contents of the file into a list
# with open(filename, 'r') as f:
#     lines = f.readlines()

# # Filter out lines containing the string to delete
# new_lines = [line for line in lines if string_to_delete not in line]

# # Write the remaining lines back to the file
# with open(filename, 'w') as f:
#     f.writelines(new_lines)

    

# with open('learning/files/handling modes.txt', 'r+') as file:
#     # read the file content
#     content = file.read()

#     # replace the string
#     new_content = content.replace('3', '2321321') # replaces the individual 3 with the specified, don't matter if it's part of a bigger word like '3rd'

#     # move the file pointer to the beginning of the file (character 0, line 0)
#     file.seek(0)

#     # write the updated content back to the file
#     file.write(new_content)

#     # truncate the file if the new content is shorter than the old content. truncate() is a method of Python file objects that is used to resize the file to a specified size. If the new size is smaller than the current size, then the file is truncated and any data beyond the new size is lost. If the new size is larger than the current size, then the file is extended and the new bytes are set to null bytes.
#     file.truncate()

with open('learning/files/handling modes.txt', 'r') as file:
    content = file.read() # 'abcpskdfpodjfsjfpsdfds'

# convert content to binary
binary_content = ' '.join(format(ord(i), 'b') for i in content)

# write binary content to a new file
with open('learning/files/binary_output.txt', 'w') as file:
    file.write(binary_content)