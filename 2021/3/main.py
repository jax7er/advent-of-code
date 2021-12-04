with open("input.txt") as f:
    data = [s.strip() for s in f]

n_bits = len(data[0])
n_lines = len(data)
most_common_bits = ""
least_common_bits = ""

for bit_i in range(n_bits):
    most_1s = sum(s[bit_i] == "1" for s in data) >= n_lines / 2
    most_common_bits += "1" if most_1s else "0"
    least_common_bits += "0" if most_1s else "1"

gamma = int(most_common_bits, 2)
epsilon = int(least_common_bits, 2)

print("part 1:", gamma * epsilon)

most_common_data = data.copy()
least_common_data = data.copy()
for bit_i in range(n_bits):
    if len(most_common_data) > 1:
        most_common_data = [s for s in most_common_data if s[bit_i] == most_common_bits[bit_i]]
    if len(least_common_data) > 1:
        least_common_data = [s for s in least_common_data if s[bit_i] == least_common_bits[bit_i]]
    
    most_common_bits = ""
    least_common_bits = ""
    for bit_i in range(n_bits):
        oxygen_most_1s = sum(s[bit_i] == "1" for s in most_common_data) >= len(most_common_data) / 2
        scrubber_most_1s = sum(s[bit_i] == "1" for s in least_common_data) >= len(least_common_data) / 2
        most_common_bits += "1" if oxygen_most_1s else "0"
        least_common_bits += "0" if scrubber_most_1s else "1"

oxygen_rating = int(most_common_data[0], 2)
scrubber_rating = int(least_common_data[0], 2)

print("part 2:", oxygen_rating * scrubber_rating)