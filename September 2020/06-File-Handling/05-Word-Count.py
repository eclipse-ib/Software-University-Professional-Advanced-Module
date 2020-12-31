import re

with open("words.txt", "w") as words_file:
    words_file.write(input())

text_file = open("text.txt", "w")
while True:
    line = input().lower()
    if not line:
        break
    text_file.write(f"{line}\n")
text_file.close()


# Counting key words:
key_words = {}

with open("words.txt") as reading_words_file:
    wds = reading_words_file.read().split()

with open("text.txt", "r") as reading_text_file:
    s = reading_text_file.read()

for word in wds:
    matches = re.findall(rf"[\s-]({word.lower()})[\s.,!?]", s.lower(), re.MULTILINE + re.IGNORECASE)
    key_words[word] = len(matches)

# # Вариант 1 с повече писане:
# output_file = open("output.txt", "w")
# for word, counts in sorted(key_words.items(), key=lambda x: -x[1]):
#     output_file.write(f"{word} - {counts}\n")
# output_file.close()

#Оптимизиран Вариант 2:
with open("output.txt", "w") as output_file:
    for word, counts in sorted(key_words.items(), key=lambda x: -x[1]):
        print(f"{word} - {counts}", file=output_file)
