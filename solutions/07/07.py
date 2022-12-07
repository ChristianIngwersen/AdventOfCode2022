from __future__ import annotations
import re
from collections import defaultdict
from dataclasses import dataclass
from typing import List


with open("solutions/07/input.txt") as f:
    data = f.read()


@dataclass
class File:
    size: int
    name: str


@dataclass
class Directory:
    name: str
    parent: Directory
    files: List[File]
    dirs: List[Directory]
    size: int = 0


def add_subdir(d: Directory, name: str) -> Directory:
    subdir = Directory(name + "/", d, [], [])
    d.dirs.append(subdir)
    return subdir


def add_file(d: Directory, size: int, name: str) -> File:
    f = File(size, name)
    d.files.append(f)
    p = d
    while p:
        p.size += f.size
        p = p.parent
    return f


root: Directory = Directory("/", None, [], [])
current: Directory = root
for command in data.split("$")[1:]:
    # Check if command contains ls or cd
    if "ls\n" in command:
        values = re.findall(r"(\d+) (\w+)", command)
        for value in values:
            add_file(current, int(value[0]), value[1])
    elif "cd" in command:
        dir = re.findall(r"cd (\S+)", command)[0]
        if dir == "..":
            current = current.parent
        else:
            current = add_subdir(current, dir)

total_size = 0
dirs = root.dirs[:]
while len(dirs) > 0:
    d = dirs.pop()
    dirs.extend(d.dirs)
    if d.size <= 100000:
        total_size += d.size

print(total_size)

# PArt 2
dirs = root.dirs[:]
total_size = 70000000
unused = total_size - root.size
required_size = 30000000
target_size = required_size - unused
nearest_match = total_size
while len(dirs) > 0:
    d = dirs.pop()
    dirs += d.dirs
    if d.size >= target_size and d.size < nearest_match:
        nearest_match = d.size
print(f"nearest_match: {nearest_match}")
