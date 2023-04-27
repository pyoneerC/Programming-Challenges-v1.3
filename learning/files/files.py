# from os.path import exists, join, basename
# from shutil import move

# source = 'C:\\Users\\User\\Desktop\\prog chall py\\extras\\text.txt'
# destination = 'C:\\User\\User\\Desktop\\folde'

# try:
#     if exists(join(destination, basename(source))):
#         print('File already exists in that location!')
#     else:
#         move(source, join(destination, basename(source)))
#         print('File was moved successfully!')

# except FileNotFoundError:
#     print('File does not exist')

# except PermissionError:
#     print('You do not have the permissions to access this folder')

# except Exception as e:
#     print(f"An error occurred: {e}")

# basename(source) will return the base name of the file in the source variable, which in this case is 'text.txt'.

# text = 'abcdefg'

# with open ('C:\\Users\\User\\Desktop\\prog chall py\\extras\\text.txt', 'a') as file:
#     file.write(text)

# r ---> read
# w ---> write (overwrite previous state)
# a ---> append in new line without overwriting

import os
import shutil

path = 'C:\\Users\\User\\Desktop\\prog chall py\\extras\\test.txt'

try:
    os.remove(path)      #delete a file
    #os.rmdir(path)      #delete an empty directory
    #shutil.rmtree(path) #delete a directory containing files

except FileNotFoundError:
    print("That file was not found")

except PermissionError:
    print("You do not have permission to delete that")

except OSError:
    print("You cannot delete that using that function")

else:
    print(f'{path} was deleted')