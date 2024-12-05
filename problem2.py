


# reads in the numbers as a list of list
def read_number_table(filename):
    table = []
    with open(filename, 'r') as f:
        for line in f:
            row = [int(x) for x in line.split()]
            table.append(row)
    return table


# check if a row is safe according to the problem parameters
def isSafe(row):
    inc = True
    dec = True
    for i in range(len(row)-1):
        # if levels increase by at more than 3, it is unsafe
        if abs(row[i] - row[i+1]) > 3:
            return False
        # if two consecutive go up, it is not decreasing
        if row[i] <= row[i+1]:
            dec = False
        # if two consecutive go down, it is not increasing
        if row[i] >= row[i+1]:
            inc = False

    # it is safe if it's increasing or decreasing
    return inc or dec

##################################
#################################
######        START        ##########

# read the data
#table = read_number_table("puzzle2.dat")
table = read_number_table("puzzle2_prob.dat")
# count the number of rows that are safe according to the problem's parameters
count = 0
for row in table:
    if isSafe(row):
        #print(row)
        count = count + 1

# print out the safe rows
print(count)

        