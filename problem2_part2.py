#file_to_use = "puzzle2_sample.dat"
file_to_use = "puzzle2_prob.dat"

# reads in the numbers as a list of list
def read_number_table(filename):
    table = []
    with open(filename, 'r') as f:
        for line in f:
            row = [int(x) for x in line.split()]
            table.append(row)
    return table


# row to check
# returns True is the row is safe/false otherwise
def check_safe(row):
    # check if the row is already safe
    if is_safe(row, -1):
        return True
    
    # check if "removing" a number makes the row safe
    for i in range(len(row)):
        if is_safe(row, i):
            return True
        
    # the row is unsafe
    return False 

# check if a row is safe according to the problem parameters
# number to skip while checking if the row is safe
def is_safe(row, skip):
    start = 0
    stop = len(row)-1
    skip_index = -1 # -1 means do not skip any
    if skip == 0:
        start = 1
    elif skip == len(row)-1:
        stop = len(row)-2
    else:
        skip_index = skip 

    inc = True
    dec = True
    for i in range(start, stop):
        current = i
        next = i+1
        if skip_index == current:
            current = i-1
        elif skip_index == next:
            next = i+2
            
        # if levels increase by at more than 3, it is unsafe
        if abs(row[current] - row[next]) > 3:
            return False
        # if two consecutive go up, it is not decreasing
        if row[current] <= row[next]:
            dec = False
        # if two consecutive go down, it is not increasing
        if row[current] >= row[next]:
            inc = False

    # it is safe if it's increasing or decreasing
    return inc or dec

##################################
#################################
######        START        ##########

# read the data
table = read_number_table(file_to_use)
# count the number of rows that are safe according to the problem's parameters
count = 0
for row in table:
    if check_safe(row):
        #print(row)
        count = count + 1

# print out the safe rows
print(count)

        