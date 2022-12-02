import re

## Read challenge input
with open("solutions/02/input.txt") as f:
    data = f.read()

## Replace A with 1, B with 2 and C with 3
data = data.replace("A", "1").replace("B", "2").replace("C", "3")

## Replace X with 1, Y with 2 and Z with 3
data = data.replace("X", "1").replace("Y", "2").replace("Z", "3")

## Split lines and get characters
games = [re.findall(r"\w", x) for x in data.splitlines()]

score = 0
for game in games:
    if game[0] == game[1]:
        score += 3
    elif game[0] == "1":
        if game[1] == "2":
            score += 6
    elif game[0] == "2":
        if game[1] == "3":
            score += 6
    elif game[0] == "3":
        if game[1] == "1":
            score += 6
    score += int(game[1])

print(score)


score = 0
for game in games:
    if game[1] == "2":
        score += 3
        score += int(game[0])
    if game[1] == "1":  # Loose
        if game[0] == "1":
            score += 3
        elif game[0] == "2":
            score += 1
        elif game[0] == "3":
            score += 2
    if game[1] == "3":  # Win
        score += 6
        if game[0] == "1":
            score += 2
        elif game[0] == "2":
            score += 3
        elif game[0] == "3":
            score += 1

print(score)


## Nice solution from reddit
f = lambda x: (
    "  BXCYAZAXBYCZCXAYBZ".index(x[0] + x[2]),
    "  BXCXAXAYBYCYCZAZBZ".index(x[0] + x[2]),
)

print(*[sum(x) // 2 for x in zip(*map(f, open("solutions/02/input.txt")))])
