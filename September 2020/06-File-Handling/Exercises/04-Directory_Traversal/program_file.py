import os
import shutil

path = input()

dict_files = {}

for root, dirs, files in os.walk(path):
    if root.count(os.path.sep) > 1:
        continue
    print(files)
    for file in files:
        file_name, file_ext = file.split(".")
        if file_ext not in dict_files:
            dict_files[file_ext] = []
        dict_files[file_ext]. append(file)
print(dict_files)

sorted_dict = sorted(dict_files.items(), key=lambda f: (f[0], f[1]))
print(sorted_dict)
with open("report.txt", "w") as final_file:
    for key, values in sorted_dict:
        final_file.write(f".{key}\n")
        for value in values:
            if value == "program_file.py":
                continue
            final_file.write(f"- - - {value}\n")