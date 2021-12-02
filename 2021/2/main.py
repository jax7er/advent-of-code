data = []
with open("input.txt") as f:
    for s in f:
        cmd, value_str = s.strip().split()
        data.append((cmd, int(value_str)))

forward, up, down = "forward up down".split()

horizontal = sum(value for cmd, value in data if cmd == forward)
depth = sum(
    value if cmd == down else -value
    for cmd, value in data if cmd in (down, up)
)

print("part 1:", horizontal * depth)

horizontal = depth = aim = 0

for cmd, value in data:
    if cmd == down:
        aim += value
    elif cmd == up:
        aim -= value
    elif cmd == forward:
        horizontal += value
        depth += aim * value

print("part 2:", horizontal * depth)