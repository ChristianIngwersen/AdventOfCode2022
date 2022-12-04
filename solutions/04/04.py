import re

with open("solutions/04/input.txt") as f:
    data = f.read()

# Split data at , and get the first and last digit in each pair
digits = list(map(int, re.findall(r"\d+", data)))
ranges = list(map(lambda x: range(x[0], x[1] + 1), zip(digits[::2], digits[1::2])))
result = list(
    map(
        lambda x: set(x[0]).issubset(x[1]) or set(x[1]).issubset(x[0]),
        zip(ranges[::2], ranges[1::2]),
    )
)
print(sum(result))

# Part 2
result = list(
    map(
        lambda x: not set(x[0]).isdisjoint(x[1]),
        zip(ranges[::2], ranges[1::2]),
    )
)
print(sum(result))
