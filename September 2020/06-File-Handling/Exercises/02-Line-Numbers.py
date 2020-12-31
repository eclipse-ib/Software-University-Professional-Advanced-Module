text_file = open("text.txt", "w")
while True:
    line = input()
    if not line:
        break
    # text_file.write(f"{line}\n")
    print(f"{line}", file=text_file)
text_file.close()

with open("text.txt", "r") as text_file:
    text_file_lines = text_file.readlines()
    for index, line in enumerate(text_file_lines):
        letters = 0
        punctuations_marks = ".,-!?';:"
        punctuations_marks_count = 0
        with open("output.txt", "a") as output_file:
            for char in line:
                if char.isalpha():
                    letters += 1
                if char in punctuations_marks:
                    punctuations_marks_count += 1
            new_text_line = f"Line {index+1}: {line.strip()} ({letters})({punctuations_marks_count})"
            print(new_text_line, file=output_file)