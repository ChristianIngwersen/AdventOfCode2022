import numpy as np


with open("solutions/08/input.txt") as f:
    data = f.read().splitlines()

grid = []
for line in data:
    grid.append([int(x) for x in line])
grid = np.array(grid)


visible = np.zeros_like(grid)
for r in range(grid.shape[0]):
    for c in range(grid.shape[1]):
        visible[r, c] = (
            (grid[:r, c] < grid[r, c]).all()
            or (grid[r + 1 :, c] < grid[r, c]).all()
            or (grid[r, :c] < grid[r, c]).all()
            or (grid[r, c + 1 :] < grid[r, c]).all()
        )


print(visible.sum())

# Scenic view
num_visible = np.zeros((*grid.shape, 4))
for rot in range(4):
    for (r, c), value in np.ndenumerate(grid):
        num = 0
        for cc in range(c - 1, -1, -1):
            num += 1
            if grid[r, cc] >= value:
                break
        num_visible[r, c, rot] = num
    grid, num_visible = np.rot90(grid), np.rot90(num_visible)
print(num_visible.prod(2).max())
