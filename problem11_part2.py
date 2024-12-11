dBug = False  # flag for debugging prints
BLINKS = 75   # constant for the number of blinks

# This function removes leading 0's from a string
def clean(str):
    index = 0
    while str[index] == '0' and index < len(str)-1:
        index = index + 1

    return str[index:len(str)]


# This blink function returns the number of stones
# created after blinking the number of times 
# given by the blink_count.
# The number returned is stored in a Memory Function
# to speed up future retrieval as this problem has
# many overlapping subproblems.
def blink(stone, blink_count, MF):
    # if no blinks occur then we just have the original stone (1 stone)
    if blink_count == 0:
        return 1
    
    # if we already solved this problem, return the result
    if (stone, blink_count) in MF:
       return MF[(stone, blink_count)]
        
    count = 1
    # find the string version of the stone and it's length
    stone_str = str(stone) 
    num_length = len(stone_str)
    # these rules are specified by the problem
    # in each the recursive call will have one fewer blinks
    if stone == 0:
        count = blink(1, blink_count-1, MF)
    elif num_length % 2 == 0:
        half_len = len(stone_str) // 2
        stone2 = int(clean(stone_str[half_len:num_length]))
        stone1 = int(stone_str[0:half_len])
        count = blink(stone1, blink_count-1, MF ) + blink(stone2, blink_count - 1, MF)
    else:
        count = blink(stone * 2024, blink_count-1, MF)
            
    # store the result for future use
    MF[(stone, blink_count)] = count
     
    return MF[(stone, blink_count)]



def process_stones(stones):
    # process each of the original
    # stones, counting how many stones they create
    count = 0
    memory_function = {}
    for stone in stones:
        if dBug:
            print('stones: ', stone)
        count  = count + blink(stone, BLINKS, memory_function)

    return count


# start of program
def main():
    
    filename = 'puzzle11_sample.dat'
    with open(filename, 'r') as f:
        for line in f:
            row = [int(x) for x in line.split()]
            if dBug:
                print("init row", row)
            print('total', process_stones(row))
    if dBug:
        print(dict)    

if __name__ == '__main__':
    main()
