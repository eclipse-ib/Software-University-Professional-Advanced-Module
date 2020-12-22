numbers = [int(i) for i in input().split()]
negative = sum(filter(lambda x: x < 0, numbers))
positive = sum(filter(lambda x: x >= 0, numbers))
print(f"{negative}\n{positive}")

if abs(negative) > positive:
    print(f"The negatives are stronger than the positives")
else:
    print(f"The positives are stronger than the negatives")