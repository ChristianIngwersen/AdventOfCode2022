## Read challenge input
with open("solutions/03/input.txt") as f:
    data = f.read().splitlines()

# Alphabet values
alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Find common characters
matches = list(
    map(
        lambda x: list(set(x[: len(x) // 2]).intersection(set(x[len(x) // 2 :]))),
        data,
    )
)

values = list(map(lambda x: alphabet.index(x[0]), matches))
print(sum(values))

# Part 2
# Find common characters in 3 lines
data_sets = [[data[i], data[i + 1], data[i + 2]] for i in range(0, len(data), 3)]
matches = list(
    map(
        lambda x: list(set(x[0]).intersection(set(x[1]), set(x[2]))),
        data_sets,
    )
)
values = list(map(lambda x: alphabet.index(x[0]), matches))

print(sum(values))
