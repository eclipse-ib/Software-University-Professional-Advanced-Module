#Съкратен вариант:
with open("text.txt", "r") as file:
    for idx, line in enumerate(file):
        if idx % 2 == 0:
            for el in "-,.!?":
                line = line.replace(el, "@")
            words = reversed(line.split())
            print(" ".join(words))



# #Мой вариант, в който създавам и записвам информацията чрез пайтън:
# text_file = open("text.txt", "w")
# while True:
#     line = input()
#     if not line:
#         break
#     # text_file.write(f"{line}\n")
#     print(f"{line}", file=text_file)
# text_file.close()
#
# with open("text.txt", "r") as t:
#     text_string = t.read()
#     replace_symbols = ["-", ",", ".", "!", "?"]
#     for symb in replace_symbols:
#         text_string = text_string.replace(symb, "@")
#
# new_txt = open("text.txt", "w")
# for index, text in enumerate(text_string.split("\n")):
#     if index % 2 == 0:
#         print(' '.join(reversed(text.split())), file=new_txt)
# new_txt.close()


