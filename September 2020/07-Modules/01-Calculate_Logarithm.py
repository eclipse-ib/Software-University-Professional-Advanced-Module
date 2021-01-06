import math

number = int(input())
logarithm_base = input()
if logarithm_base == "natural":
    print(f"{math.log(number):.2f}")
else:
    print(f"{math.log(number, int(logarithm_base)):.2f}")

