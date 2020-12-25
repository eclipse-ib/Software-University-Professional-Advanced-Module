def palindrome(text, idx):
    if idx == len(text) // 2:
        return f"{text} is a palindrome"

    if text[idx] != text[len(text)-1-idx]:
        return f"{text} is not a palindrome"
    return palindrome(text, idx + 1)


string = "peter"
index = 0
print(palindrome(string, index))


# #Вариант с използването на слайс:
# def palindrome(word, index):
#     if word == word[::-1]:
#         return f"{word} is a palindrome"
#     return f"{word} is not a palindrome"
#
#
# print(palindrome("abcba", 0))
# print(palindrome("peter", 0))
