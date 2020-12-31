#Варинат с използването на os.path.exists():
import os.path
print("File found" if os.path.exists("text.txt") else "File not found")


# #Вариант с try/except:
# try:
#     f = open("text.txt")
#     print(f"File found")
# except FileNotFoundError:
#     print(f'File not found')



# #Аматьорски опит:
# f = open("text.txt", "w")
# f.write("This is some random line")
# f.write("This is the second line")
# f.write("And this is the third one")
#
# if f:
#     print('File found')
# else:
#     print('File not found')

