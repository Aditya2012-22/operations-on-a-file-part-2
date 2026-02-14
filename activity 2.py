# new_file = open('New_File.txt', 'x')
# new_file.close()

import os
print("Checking if my_file exists or not")
if os.path.exists("New_File.txt"):
    os.remove("New_File.txt")
else:
    print("This file does not exist")
    