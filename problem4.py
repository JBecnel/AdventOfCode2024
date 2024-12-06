# read file line by line into a list
# stripping the newline characters
file_path = 'puzzle4_part1_sample.dat'
file_path = 'puzzle4.dat'
with open(file_path, 'r') as file:
    lines = file.readlines()

# strip newline characters from each line in lines
lines = [line.strip() for line in lines]

# helper method to count occurrences of XMAS
def find_XMAS(lines, row, col):
    max_row = len(lines)-1
    max_col = len(lines[0])-1

    # check right 
    count = 0
    if (lines[row][col:min(max_col, col+4)]) == "XMAS":
        count = count + 1 

    # check left
    if lines[row][max(0,col-3):col] == 'SAM':
        count = count + 1
    
    # check down
    if row + 3 <= max_row:
        if lines[row+1][col] == 'M' and lines[row+2][col] == 'A' and lines[row+3][col] == 'S':
            count = count + 1
    # check up
    if row - 3 >= 0:
        if lines[row -3][col] == 'S' and lines[row-2][col] == 'A' and lines[row-1][col] == 'M':
            count = count + 1
    
    
    # check right down diagonal
    if row + 3 <= max_row and col+3 <= max_col:
        if lines[row+1][col+1] == 'M' and lines[row+2][col+2] == 'A' and lines[row+3][col+3] == 'S':
            count = count + 1
    
    # check left up diagonal
    if row - 3 >= 0 and col - 3 >= 0:
        if lines[row - 1][col - 1] == 'M' and lines[row - 2][col - 2] == 'A' and lines[row - 3][col - 3] == 'S':
            count = count + 1
    
    # check left down diagonal
    if row - 3 >= 0 and col + 3 <= max_col:
        if lines[row - 1][col + 1] == 'M' and lines[row - 2][col + 2] == 'A' and lines[row - 3][col + 3] == 'S':
            count = count + 1
    
    # check right up diagonal
    if row + 3 <= max_row and col - 3 >= 0:
        if lines[row + 1][col - 1] == 'M' and lines[row + 2][col - 2] == 'A' and lines[row+3][col - 3] == 'S':
            count = count + 1
    
    return count
    
##########################################
##########################################
##############   MAIN    #################
########################################## 
count = 0 # count the number of XMAS in all directioins
for r in range(len(lines)):
    for c in range(len(lines[0])):
        if lines[r][c] == 'X':
            count = count + find_XMAS(lines, r,c)

print(count)