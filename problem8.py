# read the file and create a dictionary with
# - keys being the letter read and 
# - values the row and column where the letter occurred
char_positions = { }
file_path = 'puzzle8_sample3.dat'
#file_path = "puzzle8.dat"
with open(file_path, 'r') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]


num_rows = len(lines)
num_cols = len(lines[0])

for row in range(num_rows):
    for col in range(num_cols):
        char = lines[row][col]
        if char != '.':
            if char in char_positions:
                char_positions[char].append((row, col))
            else:
                char_positions[char] = [(row, col)]

print(char_positions)

# traverse the dictionary
locations = set()
for char, positions in char_positions.items():
    for m in range(0, len(positions)):
        for n in range(m+1, len(positions)): 
            row1, col1 = positions[m]
            row2, col2 = positions[n]
            row_diff = row1-row2 
            col_diff = col1-col2
        
            location1 = (row2-row_diff, col2-col_diff)
            location2 = (row1 + row_diff, col1 + col_diff)

            if (location1[0] >= 0 and location1[0] < num_rows and location1[1] >= 0 and location1[1] < num_cols):
                locations.add(location1)
        
            if (location2[0] >= 0 and location2[0] < num_rows and location2[1] >= 0 and location2[1] < num_cols):
                locations.add(location2)

print(locations)
print(len(locations))
            