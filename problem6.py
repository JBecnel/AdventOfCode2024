
# find the position of the carrot ('^') in the grid
def find_carrot(grid):
    # find location of ^ in grid
    for r in range(len(grid)):
        col = grid[r].find('^')
        if (col != -1):
            return r, col
        
# read file line by line into a list
# stripping the newline characters
file_path = 'puzzle6_sample.dat'
file_path = 'puzzle6.dat'
with open(file_path, 'r') as file:
    grid = file.readlines()

# strip newline characters from each line in grid
grid = [line.strip() for line in grid]

r, c = find_carrot(grid) # starting positon of the carrot

# enumerable to control direction of move
direction = 0
# up, right, down, left
directions = [(-1,0), (0,1), (1,0), (0,-1)]
path_set = set()

max_row = len(grid) - 1
max_col = len(grid[0]) -1
dr, dc = directions[direction]
while (r <= max_row) and (r >= 0) and (c <= max_col) and (c >= 0):
    # check if we've reached a tree or a carrot
    if grid[r][c] == '#':
        direction = (direction + 1) % 4
        # retreat to previous location
        r = r - dr 
        c = c - dc
        dr, dc = directions[direction]
    else:
        path_set.add((r,c)) # add the location to the path set
    # move to next location to check
    r = r + dr
    c = c + dc
   
# move in the current direction
print(len(path_set))