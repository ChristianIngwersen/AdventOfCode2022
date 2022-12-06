import re

with open("solutions/06/input.txt") as f:
    data = f.read()

# find the first occurence of four unique characters in a row.
print(re.search(r"(\w)(?!\1)(\w)(?!\1|\2)(\w)(?!\1|\2|\3)(\w)", data).span()[1])

# The same should now be done for 14 characters in a row.
search_string = ""
pattern = "(\w)(?!"
for i in range(2, 15):
    search_string += pattern + "|".join([f"\{j}" for j in range(1, i)]) + ")"
search_string += "(\w)"
print(re.search(search_string, data).span()[1])
