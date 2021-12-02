import numpy as np

with open("input.txt") as f:
    data = np.fromiter(f, dtype=int)

increased = np.diff(data) > 0

print("part 1:", increased.sum())

win = 3

summed = []
for i in range(win, len(data) + 1):
    summed.append(data[i - win:i].sum())

increased = np.diff(summed) > 0

print("part 2:", increased.sum())