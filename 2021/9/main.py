from pathlib import Path
from functools import reduce
from operator import mul

def get_adjacent(x, y):
    return ((x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y))

def main(file_name):
    with open(Path(__file__).parent / f"{file_name}.txt") as f:
        data = [row.strip() for row in f]

    heightmap = [[int(s) for s in row] for row in data]
    n_y = len(heightmap)
    n_x = len(heightmap[0])

    low_locs = []
    for y, row in enumerate(heightmap):
        for x, h in enumerate(row):
            check_locs = [(x, y) for x, y in get_adjacent(x, y) if (0 <= x < n_x) and (0 <= y < n_y)]
            other_hs = [heightmap[check_y][check_x] for check_x, check_y in check_locs]
            if h < min(other_hs):
                low_locs.append((x, y))

    risk = sum(heightmap[y][x] + 1 for x, y in low_locs)

    print(file_name, "part 1:", risk) # test 15

    checked_locs = []
    basins = []

    for y, row in enumerate(heightmap):
        for x, h in enumerate(row):
            if (x, y) in checked_locs:
                continue

            checked_locs.append((x, y))

            if h < 9:
                basin = {(x, y)}
                check_locs = [
                    (x, y) for x, y in get_adjacent(x, y)
                    if (x, y) not in basin and (0 <= x < n_x) and (0 <= y < n_y)
                ]
                
                while check_locs:
                    check_x, check_y = check_locs.pop()
                    check_h = heightmap[check_y][check_x]
                    checked_locs.append((check_x, check_y))
                    
                    if check_h < 9:
                        basin.add((check_x, check_y))
                        check_locs.extend(
                            (x_, y_) for x_, y_ in get_adjacent(check_x, check_y)
                            if (x_, y_) not in basin and (x_, y_) not in checked_locs and (0 <= x_ < n_x) and (0 <= y_ < n_y)
                        )

                basins.append(basin)

    biggest_3_lens = [len(b) for b in sorted(basins, key=len)[-3:]]
    product = reduce(mul, biggest_3_lens)

    print(file_name, "part 2:", product) # test 1134

    # for basin in basins:
    #     diagram = [["."] * n_x for _ in range(n_y)]
    #     for x, y in basin:
    #         diagram[y][x] = str(heightmap[y][x])
    #     print("\n".join("".join(row) for row in diagram))
    #     print("")

main("test")
main("input")