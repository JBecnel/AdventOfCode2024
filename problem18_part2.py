import re
from enum import Enum
from collections import deque

dBug = False

class Direction(Enum):
    UP = (0,-1)
    LEFT = (-1,0)
    DOWN = (0,1)
    RIGHT = (1,0)

def obtain_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]

    bytes = []   # set of all wall locations
    
    for line in lines:
        nums = re.findall(r"\d+", line)
        bytes.append((int(nums[0]), int(nums[1])))

    return bytes, len(lines)
    

def bfs(bytes, width, height):
    bytes = set(bytes)
    start = (0,0)
    queue = deque()
    queue.append(start)

    
    steps_from_start = { }
    steps_from_start[start] = 0
    while queue:
        v = queue.popleft()
        for d in Direction:            
            new_vertex = (v[0]+d.value[0], v[1]+d.value[1])
            if dBug:
                print("vertex", v, "new vertex: ", new_vertex, " queue ", queue)
            if is_valid(new_vertex, bytes, width, height):
                if not new_vertex in steps_from_start:
                    steps_from_start[new_vertex] = steps_from_start[v] + 1
                    queue.append(new_vertex)
                    if dBug:
                        print()
                        #print("vertex ", new_vertex, "   from v ", v)
                        #print(steps_from_start)
                        #print()
    
    if dBug:
        print(steps_from_start)


    return steps_from_start
    

def is_valid(new_vertex, bytes, width, height):
    with_in_bounds = (0 <= new_vertex[0] < width) and (0 <= new_vertex[1] < height)
    open_spot = not (new_vertex in bytes)
    return with_in_bounds and open_spot



def main():
    file_name = "puzzle18_sample.dat"
    file_name = "puzzle18.dat"
    
    bytes, file_length = obtain_input(file_name)

    WIDTH = 71 #7
    HEIGHT = 71 #7
 
    if dBug:
        s = bfs(bytes[:1024], WIDTH, HEIGHT)
        print(s[(WIDTH-1, HEIGHT-1)])

    if dBug:
        print("bytes " , bytes)
    #perform a bfs
    #WIDTH = 7
    #HEIGHT = 7
    for num_bytes in range(1025, file_length):
        steps_to_nodes = bfs(bytes[:num_bytes], WIDTH, HEIGHT)
        if not (WIDTH-1, HEIGHT-1) in steps_to_nodes:
            if dBug:
                print(bytes[:num_bytes])
            print(num_bytes, bytes[num_bytes-1])
            break

    #print(steps_to_nodes[(WIDTH-1,HEIGHT-1)])

if __name__ == "__main__":
    main()