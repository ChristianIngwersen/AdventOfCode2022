import re
from copy import deepcopy

with open("solutions/05/input.txt") as f:
    data = f.read()

# Initial part
container_data = data.splitlines()[:9]

# Find character indexes in each line in container_data
indexes = list(map(lambda x: re.findall(r".|\s", x), container_data))

container_stacks = [[] for _ in range(9)]
for index, i in enumerate(indexes[-1]):
    if i != " ":
        for j in range(8):
            if indexes[j][index] != " ":
                container_stacks[int(i) - 1].append(indexes[j][index])

# Reverse the stacks
container_stacks = list(map(lambda x: x[::-1], container_stacks))
container_stacks_2 = deepcopy(container_stacks)

# Match three groups of integers in the pattern "move group1 from group2 to group3"
moves = re.findall(r"move (\d+) from (\d+) to (\d+)", data)

for move in moves:
    for _ in range(int(move[0])):
        tmp = container_stacks[int(move[1]) - 1].pop()
        container_stacks[int(move[2]) - 1].append(tmp)
print("".join([container_stacks[i][-1] for i in range(9)]))

# Part 2
for move in moves:
    tmp = container_stacks_2[int(move[1]) - 1][-int(move[0]) :]
    container_stacks_2[int(move[1]) - 1] = container_stacks_2[int(move[1]) - 1][
        : -int(move[0])
    ]
    container_stacks_2[int(move[2]) - 1] += tmp
print("".join([container_stacks_2[i][-1] for i in range(9)]))
