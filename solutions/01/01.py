import re

## Read challenge input
with open("solutions/01/input.txt") as f:
    data = f.read()

## split newlines and get ints from strings
numbers = [sum(map(int, re.findall(r"\d+", x))) for x in re.split("\s\s", data)]

# max value
print(max(numbers))

## Part 2
# find the 3 largest numbers in list numbers and sum them
print(sum(sorted(numbers)[-3:]))
