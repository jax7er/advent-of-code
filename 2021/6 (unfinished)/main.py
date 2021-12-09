from pathlib import Path
from collections import deque

first_incubation_days = 9
incubation_days = 7

with open(Path(__file__).parent / "test.txt") as f:
    data = [int(s) for s in f.read().split(",")]

def simulate(days):
    fishes = deque(data)
    n_fish = len(fishes)

    while fishes:
        first_child = fishes.pop()

        for day in range(first_child, days, incubation_days):
            fishes.append(day + first_incubation_days)   
            n_fish += 1

        # print(*fishes)
            
    return n_fish

print("part 1:", simulate(80))  # test 5934
print("part 2:", simulate(256)) # test 26984457539

