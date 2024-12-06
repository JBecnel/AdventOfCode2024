# helper method to count occurrences of XMAS
def find_X(lines, row, col):
    count = 0

    up = row-1
    down = row+1
    left = col - 1 
    right = col + 1
    # m up s down
    if (lines[up][left] == 'M') and (lines[up][right] == 'M') and (lines[down][left] == 'S') and (lines[down][right] == 'S'):
        count = count + 1

    # m down, s up
    if (lines[up][left] == 'S') and (lines[up][right] == 'S') and (lines[down][left] == 'M') and (lines[down][right] == 'M'):
        count = count + 1

    # s left, m right
    if (lines[up][left] == 'S') and (lines[up][right] == 'M') and (lines[down][left] == 'S') and (lines[down][right] == 'M'):
        count = count + 1
    
    # m left, s right
    if (lines[up][left] == 'M') and (lines[up][right] == 'S') and (lines[down][left] == 'M') and (lines[down][right] == 'S'):
        count = count + 1
    
    return count 



    
##########################################
##########################################
##############   MAIN    #################
########################################## 

# read file line by line into a list
# stripping the newline characters
file_path = 'puzzle4_part1_sample.dat'
#file_path = 'puzzle4.dat'
with open(file_path, 'r') as file:
    lines = file.readlines()

# strip newline characters from each line in lines
lines = [line.strip() for line in lines]


count = 0 # count the number of XMAS in all directioins
for r in range(1,len(lines)-1):
    for c in range(1,len(lines[0])-1):
        if lines[r][c] == 'A':
            count = count + find_X(lines, r,c)

print(count)