file_path = 'puzzle9_sample.dat'
file_path = 'puzzle9_sample2.dat'
file_path = 'puzzle9.dat'

dBug = False  # used to print debugging statemetns

with open(file_path, 'r') as file:
     # Read one line and strip whitespace and newlines
    line = file.readline().strip()

if dBug:
    print(line)

# create a list of pairs with the first number
# is the block size and the second number
# is the free space after this block
# Note: the index is the id in the problem
index = 0
disk_map = []
while (index < len(line) -1):
    block_size = int(line[index])
    free_space = int(line[index+1])
    index = index + 2
    disk_map.append([block_size, free_space])

# add the last block
disk_map.append([int(line[len(line)-1]), 0])

if dBug:
    print(disk_map)

# find the id of the file that will be moved to the space
# disk_map info given above
# stop - we search from the end of the disk ids to the "stop"
# id; the stop id is where we looking to fill empty space
def move_block(disk_map, stop):
    # move thru list in reverse
    for id in range(len(disk_map) - 1, stop, -1):
        block_size = disk_map[id][0]
        if block_size > 0:
            disk_map[id][0] = disk_map[id][0] - 1
            return id
    return 0

pos = 0 # position in file
check_sum = 0 # check sum in problem id * file  position
for id in range(len(disk_map)):
    # find the check sum for the block of memory
    block = disk_map[id][0]
    while block > 0:
        check_sum = check_sum + pos*id # check_sum for used space
        if dBug:
            print("id ", id, "pos ", pos, "block ", block,  "check sum ", check_sum)
        pos = pos + 1
        block = block - 1        
        
    # move the file to the free spot and compute the check sum
    free = disk_map[id][1]
    while free > 0:
        new_block = move_block(disk_map, id)        
        check_sum = check_sum + pos*new_block
        if dBug:
            print("id ", id, "pos ", pos, "block ", block, "free space ", free, "inserted block ", new_block, "check sum ", check_sum)
        free = free - 1
        pos = pos + 1

print()
print(check_sum)

# answer to test problem
if dBug:
    str = "022111222"
    total = 0
    for index in range(len(str)):
        total = total + index * int(str[index])
        print(total)
    print(total)








