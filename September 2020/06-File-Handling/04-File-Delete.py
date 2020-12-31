#Имплементация на долното, но без възможност за хрвърляне на грешка с os.path.exists:
import os

file_path = "my_first_file.txt"
if os.path.exists("my_first_file.txt"):
    os.remove("my_first_file.txt")

# #Вариант с използването на try/except:
# import os
# try:
#     os.remove("my_first_file.txt")
# except FileNotFoundError:
#     print(f"File already deleted!")