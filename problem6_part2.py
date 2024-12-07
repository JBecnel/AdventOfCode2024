
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

carrot_r, carrot_c = find_carrot(grid) # starting position of the carrot



# enumerable for different directions:
# up, right, down, left
directions = [(-1,0), (0,1), (1,0), (0,-1)]

# max row and max column
max_row = len(grid) - 1
max_col = len(grid[0]) -1
count = 0  # count of the number loops

#############################################################
# find the path from problem 1
#############################################################
original_path = set()
r = carrot_r
c = carrot_c 
direction = 0
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
        original_path.add((r,c)) # add the location to the path set
    # move to next location to check
    r = r + dr
    c = c + dc
   
print(len(original_path))

##########################################################
# put the obstruction on places along the path
# and determine if you run into a cycle
##########################################################
##########################################################

# for each possible destination along the original path
for location in original_path:
    row = location[0]
    col = location[1]        
    if grid[row][col] == ".": # each '.' is a potential place for an obstruction
        # reset the path
        path_set = set()
        # reset starting location and direction
        r = carrot_r
        c = carrot_c
        direction = 0
        dr, dc = directions[direction]
        # while we are on the grid
        while (r <= max_row) and (r >= 0) and (c <= max_col) and (c >= 0):
            # check if we've reached a tree or the obstruction location
            if grid[r][c] == '#' or (r == row and c == col): 
                # retreat to previous location and turn
                r = r - dr 
                c = c - dc
                direction = (direction + 1) % 4
                dr, dc = directions[direction]
            else:
                # if we arrive a path location and are facing the same direction
                if (r,c,direction) in path_set:
                    count = count + 1
                    #print(r,c,direction)
                    # exit the while loop
                    r = -1
                    c = -1
                    
                else:
                    path_set.add((r,c, direction))
                # go to next grid point in this direction
                r = r + dr
                c = c + dc
        # end while
        
   
# move in the current direction
print(count)
