import statistics
import matplotlib.pyplot as plt 
FILEPATH = " input.txt"
# Open the input file and read the contents
with open(FILEPATH, 'r') as f:
    contents = f.read().strip()

# Convert the contents to a list of integers
bits = [int(c) for c in contents]

# Ignore any leftover bits that don't make a full byte
num_bits = len(bits)
if num_bits % 4 != 0:
    bits = bits[:num_bits - (num_bits % 4)]

# Convert the bits to hex and join them into a string
hex_str = ''.join([hex(int(''.join(map(str, bits[i:i+4])), 2))[2:] for i in range(0, len(bits), 4)])

# Open the output file and write the hex string to it
with open('HexNums.txt', 'w') as f:
    f.write(hex_str)

# Open the file and read the contents
with open('HexNums.txt', 'r') as f:
    hex_str = f.read().strip()

# Count the number of occurrences of each hexadecimal digit
hex_counts = {}
for digit in hex_str:
    hex_counts[digit] = hex_counts.get(digit, 0) + 1

# Calculate the average number of occurrences
avg_count = statistics.mean(hex_counts.values())

# Print the total number of characters read
total_chars = len(hex_str)
print(f'Total characters read: {total_chars}')
print(f'Average occurence of all characters: {avg_count}')
# Print the number of times each character appears and its difference from the average
counts_with_diff = []
for digit in '0123456789abcdef':
    count = hex_counts.get(digit, 0)
    difference = count - avg_count
    counts_with_diff.append((digit, count, difference))

counts_with_diff.sort(key=lambda x: (x[0], -x[1]))

for digit, count, difference in counts_with_diff:
    print(f'{digit}: {count} times')
    print(f'Difference from average: {round(difference*100/total_chars, 6)}%')

# Plot a bar graph of the hexadecimal digit counts
plt.bar([x[0] for x in counts_with_diff], [x[1] for x in counts_with_diff])

# Set the x-axis and y-axis labels
plt.xlabel('Hexadecimal Digit')
plt.ylabel('Count')

# Display the plot
plt.show()
