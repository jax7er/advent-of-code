from pathlib import Path
from statistics import median

def main(file_name):
    with open(Path(__file__).parent / f"{file_name}.txt") as f:
        data = [int(s) for s in f.read().split(",")]

    def total_fuel(center):
        return sum(abs(n - center) for n in data)

    center = round(median(data))

    print(file_name, "part 1:", total_fuel(center)) # test 37

    def total_fuel(center):
        return round(sum(i * ((i - 1) / 2 + 1) for n in data if (i := abs(n - center))))

    center = min(range(max(data)), key=total_fuel)

    print(file_name, "part 2:", total_fuel(center)) # test 168

main("test")
main("input")