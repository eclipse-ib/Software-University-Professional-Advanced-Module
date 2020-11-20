n = int(input())

students = {}

for i in range(n):
    student = input().split()
    name = student[0]
    grade = float(student[1])

    if name not in students:
        students[name] = [grade]

    else:
        students[name].append(grade)

for name, values in students.items():
    average = sum(values) / len(values)
    print(f"{name} -> ", end='')
    for i in values:
        print(f"{i:.2f} ", end='')
    print(f"(avg: {average:.2f})")
