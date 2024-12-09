file_path = 'puzzle9_sample.dat'
file_path = 'puzzle9_sample2.dat'
#file_path = 'puzzle9.dat'

dBug = True  # used to print debugging statemetns

with open(file_path, 'r') as file:
     # Read one line and strip whitespace and newlines
    line = file.readline().strip()

if dBug:
    print(line)

# create a list of pairs with the first number
# is the block size and the second number
# is the free space after this block
# the third boolean is to determine if the block has been moved
# Note: the index is the id in the problem
index = 0
disk_map = []
while (index < len(line) -1):
    block_size = int(line[index])
    free_space = int(line[index+1])
    index = index + 2
    disk_map.append([block_size, free_space, False])

# add the last block
disk_map.append([int(line[len(line)-1]), 0, False])

if dBug:
    print(disk_map)

# find the id of the file that will be moved to the space
# disk_map info given above
# stop - we search from the end of the disk ids to the "stop"
# id; the stop id is where we looking to fill empty space
def move_block(disk_map, free_space, stop):
    # move thru list in reverse
    for id in range(len(disk_map) - 1, stop, -1):
        block_size = disk_map[id][0]
        moved = disk_map[id][2]
        if block_size <= free_space and not moved:            
            disk_map[id][2] = True  # indicate the block has been moved
            return [id, block_size]
    return [-1,0]   # flag for can't find a phone

pos = 0 # position in file
check_sum = 0 # check sum in problem id * file  position
for id in range(len(disk_map)):
    # find the check sum for the block of memory
    block = disk_map[id][0]
    moved = disk_map[id][2]
    if moved: 
        pos = pos + block 
    else: 
        # compute the check sum for the block compenent
        while block > 0:
            check_sum = check_sum + pos*id # check_sum for used space
            if dBug:
                print("id ", id, "pos ", pos, "block ", block,  "check sum ", check_sum)
            pos = pos + 1
            block = block - 1        
        
        # move the file to the free spot and compute the check sum
        free = disk_map[id][1]
        print(disk_map)
        new_block_id = 0
        if disk_map[id][0] == 0:
            print("position ", pos, " nothing ", 0)
            pos = pos + 1

        while free > 0 and new_block_id != -1:
            new_block_id, blocks_used  = move_block(disk_map, free, id)    
            if new_block_id == -1:
                pos = pos + free    
            free = free - blocks_used
            if dBug:
                print("before id ", id, "pos ", pos, "block ", block, "block_used", blocks_used , "free space ", free, "inserted block ", new_block_id, "check sum ", check_sum)
            while blocks_used > 0:
                check_sum = check_sum + pos*new_block_id
                if dBug:
                    print("id ", id, "pos ", pos, "block ", block, "free space ", free, "inserted block ", new_block_id, "check sum ", check_sum)
                pos = pos + 1
                blocks_used = blocks_used - 1

print()
print(check_sum)

# answer to test problem
if dBug:
    #str = "00992111777.44.333555566668888"
    #str = "00992111777.44.3335555......66668888.."
    str = "00992111777.44.333....5555.6666.....8888.."
    #str = "0..111....22222"
    total = 0
    for index in range(len(str)):
        if str[index] != '.':
            total = total + index * int(str[index])
            print(total)
    print(total)








