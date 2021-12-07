def show(diagram):
    print("\n".join("".join(map(str, row)).replace("0", ".") for row in diagram))

with open(f"input.txt") as f:
    data = f.read().strip().splitlines()

lines = [tuple(int(xy) for xy in coords.replace("->", ",").split(",")) for coords in data]
lines_x = [(x1, y1, y2) for x1, y1, x2, y2 in lines if x1 == x2]
lines_y = [(y1, x1, x2) for x1, y1, x2, y2 in lines if y1 == y2]

max_x = max(max((x1, x2)) for x1, _, x2, _ in lines)
max_y = max(max((y1, y2)) for _, y1, _, y2 in lines)
diagram = [[0] * (max_x + 1) for _ in range(max_y + 1)]

for x, *ys in lines_x:
    for y in range(min(ys), max(ys) + 1):
        diagram[y][x] += 1
for y, *xs in lines_y:
    for x in range(min(xs), max(xs) + 1):
        diagram[y][x] += 1

danger = sum(n > 1 for row in diagram for n in row)

print("part 1:", danger)

lines_diag = [(x1, y1, x2, y2) for x1, y1, x2, y2 in lines if abs(x1 - x2) == abs(y1 - y2)]

for x1, y1, x2, y2 in lines_diag:
    x_dir = 1 if x2 > x1 else -1
    y_dir = 1 if y2 > y1 else -1
    xs = range(x1, x2 + x_dir, x_dir)
    ys = range(y1, y2 + y_dir, y_dir)
    for x, y in zip(xs, ys):
        diagram[y][x] += 1

danger = sum(n > 1 for row in diagram for n in row)

print("part 2:", danger)
