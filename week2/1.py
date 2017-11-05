import os
from datetime import datetime

# get where the code for the os module is
#print(os.__file__)
#get current working directory
print(os.getcwd())

# change to the directory specified
os.chdir("C:\\Users\\Francis\\Desktop")

print(os.getcwd())

#print(os.listdir())

# make a directory
#os.mkdir("fake_dir")
#print(os.listdir())

# make dirs recursively
#os.makedirs("Folder/sub/sub")

# delete a directory
#os.rmdir("fake_dir")
# remove recursively
#os.removedirs("path_to_remove")
#os.rename("file_exists","new_name")

# lookup information about a file
#print(os.stat("Mockoon.lnk"))
# get file size
#size_of_file = os.stat("filename").st_size
stats = os.stat("Mockoon.lnk").st_mtime
print(datetime.fromtimestamp(stats))
