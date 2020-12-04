def matrix(numbers):
    print(f"Positive: {', '.join([str(positive) for positive in numbers if positive >= 0])}"),
    print(f"Negative: {', '.join([str(negative) for negative in numbers if negative < 0])}"),
    print(f"Even: {', '.join([str(even) for even in numbers if even % 2 == 0])}"),
    print(f"Odd: {', '.join([str(odd) for odd in numbers if odd % 2 != 0])}")


numbers = [int(_) for _ in input().split(", ")]

matrix(numbers)