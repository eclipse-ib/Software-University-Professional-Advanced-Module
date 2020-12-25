def age_assignment(*args, **kwargs):
    all_names = {}
    for arg in args:
        all_names[arg] = kwargs[arg[0]]
    return all_names


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))



# # По-примитивен вариант с for цикъл:
# def age_assignment(*args, **kwargs):
#     all_names = {}
#     for i in args:
#         for key, value in kwargs.items():
#             if i[0] == key:
#                 all_names[i] = value
#     return all_names
#
#
# print(age_assignment("Peter", "George", G=26, P=19))
# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
