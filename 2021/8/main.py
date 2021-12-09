from pathlib import Path

n_segments_to_values = {
    1: (),
    2: (1,),
    3: (7,),
    4: (4,),
    5: (2, 3, 5),
    6: (0, 6, 9),
    7: (8,),
}

value_to_segments = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}

def main(file_name):
    with open(Path(__file__).parent / f"{file_name}.txt") as f:
        data = [[["".join(sorted(w)) for w in s.split()] for s in row.split("|")] for row in f.read().splitlines()]

    n_unique_segments = 0

    for patterns, outputs in data:
        for output in outputs:
            if len(n_segments_to_values[len(output)]) == 1:
                n_unique_segments += 1

    print(file_name, "part 1:", n_unique_segments) # test 26

    output_values = []

    for patterns, outputs in data:
        code_to_value = {}

        for code in patterns + outputs:
            if code not in code_to_value:
                values = n_segments_to_values[len(code)]

                if len(values) == 1:
                    code_to_value[code] = values[0]

        false_to_true = dict.fromkeys("abcdefg")

        for code, value in code_to_value.items():
            true_segments = value_to_segments[value]

            for segment in code:
                if false_to_true[segment] is None:
                    false_to_true[segment] = true_segments
                else:
                    false_to_true[segment] = "".join(sorted(set(false_to_true[segment] + true_segments)))

        print(false_to_true)
        exit()

    print(file_name, "part 2:", sum(output_values)) # test 61229

main("test")
main("input")