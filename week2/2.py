
# import os

# # for dirpath,dirnames,files in os.walk(os.getcwd()):
# #     print("Directory path: ",dirpath)
# #     print("Current Directory: ",dirnames)
# #     print("Files : ",files)

# #
# print(os.path.splitext("Mockoon.lnk")[1])

# # Movie example
# os.chdir("c://movies")

# for dirpath,dirnames,files in os.walk(os.getcwd()):
#     for directory in dirnames:
#         if os.path.isdir(directory):
#             continue
#         elif os.path.isfile(directory):
#             extension = os.path.splitext(directory)[1]
#             if extension == '.txt':
#                 print("We found that annoying Readme.txt")
#                 os.rmdir(directory)

count =10
i = 0
while i < count:
    print("hello")
    print(i)
    i+=1
