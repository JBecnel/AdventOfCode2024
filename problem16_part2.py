dBug = False  # flag to print debug statements 

import sys
from enum import Enum
from collections import deque

class Direction(Enum):
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"

def obtain_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]

    start = [1,1]   # starting location
    end = [10,10]   # ending location
    spots = set()   # set of all wall locations
    

    # using image coordinates (0,0) is top left
    # x moves left and right
    # y moves up and down
    # '#' is a wall, 'O' is a box, '@' is the robot
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] != '#':
                spots.add((x,y))
                if lines[y][x] == "S":
                    start = [x,y]
                if lines[y][x] == "E":
                    end = [x,y]
            

    return start, end, spots


def find_min(dist):
    key = None 
    min = sys.maxsize
    for k, val in dist.items():        
        if (val[0] < min):
            min = val[0]
            key = k
    
    return key

def find_adj_vertex(next,maze):
    x = next[0]
    y = next[1]
    dir = next[2]

    adj = { }
    if dir == Direction.EAST:
        adj[(x,y, Direction.NORTH)] = 1000
        adj[(x,y, Direction.SOUTH)] = 1000
        adj[(x,y, Direction.WEST)] = 2000
        x = x + 1

    elif dir == Direction.WEST:
        adj[(x,y, Direction.NORTH)] = 1000
        adj[(x,y, Direction.SOUTH)] = 1000
        adj[(x,y, Direction.WEST)] = 2000
        x = x - 1
    elif dir == Direction.NORTH:
        adj[(x,y, Direction.WEST)] = 1000
        adj[(x,y, Direction.EAST)] = 1000
        adj[(x,y, Direction.SOUTH)] = 2000
        y = y - 1
    else:  # south
        adj[(x,y, Direction.WEST)] = 1000
        adj[(x,y, Direction.EAST)] = 1000
        adj[(x,y, Direction.NORTH)] = 2000
        y = y + 1

    
    if (x,y) in maze:
        adj[(x,y, dir)] = 1  # only 1 to go in same direction

    return adj

    

def modified_dijkstra(start, end, maze):
    start_vertex = (start[0], start[1], Direction.EAST)

    distance = { }  # start vertex along with distance and prior vertex

    for loc in maze:
        for d in Direction:
            dist = sys.maxsize            
            vertex = (loc[0], loc[1], d)
            distance[vertex] = (dist, None)
    distance[start_vertex] = (0, start_vertex)

    queue = distance.copy()

    tree = []
    for i in range(len(distance)): 
        u = find_min(queue)
       
        tree.append(u)
        adj = find_adj_vertex(u, maze)
        for a, weight in adj.items():
            if weight + distance[u][0] < distance[a][0]:
                distance[a] = (weight + distance[u][0], u)
                queue[a] = (weight + distance[u][0], u)

        queue.pop(u)

    return tree, distance

def depth_first_search_back(dist, end):
    marked = set()
    dfs_rec(dist, end, marked)
    return marked 
   
def dfs_rec(dist, v, marked):
    if dBug: 
        print("visiting", v)
    marked.add(v)
    prev = back_track(dist, v)
    if dBug:
        print("previous", prev)
    for w in prev:
        if w not in marked: 
            dfs_rec(dist, w, marked)
    
    
def back_track(dist, v):
    cost_to_v = dist[v][0]
    
    x = v[0]
    y = v[1]
    dir = v[2]

    adj = { }
    if dir == Direction.EAST:
        adj[(x,y, Direction.NORTH)] = 1000
        adj[(x,y, Direction.SOUTH)] = 1000
        adj[(x,y, Direction.WEST)] = 2000
        x = x - 1

    elif dir == Direction.WEST:
        adj[(x,y, Direction.NORTH)] = 1000
        adj[(x,y, Direction.SOUTH)] = 1000
        adj[(x,y, Direction.WEST)] = 2000
        x = x + 1
    elif dir == Direction.NORTH:
        adj[(x,y, Direction.WEST)] = 1000
        adj[(x,y, Direction.EAST)] = 1000
        adj[(x,y, Direction.SOUTH)] = 2000
        y = y + 1
    else:  # south
        adj[(x,y, Direction.WEST)] = 1000
        adj[(x,y, Direction.EAST)] = 1000
        adj[(x,y, Direction.NORTH)] = 2000
        y = y - 1

    
    if (x,y, dir) in dist:
        adj[(x,y, dir)] = 1  # only 1 to go in same direction

    if dBug:
        print("possible adj: ", adj)
    valid_adj = set()
    for w, cost in adj.items():
        cost_wv = cost
        cost_to_w = dist[w][0]
        if cost_to_v == cost_to_w + cost_wv:
            valid_adj.add(w)

    return valid_adj


def main():
    file_path = "puzzle16_sample.dat"
    file_path = "puzzle16.dat"
    start, end, maze = obtain_input(file_path)

    if dBug:
        print(f"Start {start}")
        print(f"End {end}")
        print(f"Maze {maze}")

    tree, dist = modified_dijkstra(start, end, maze)

    
    min = sys.maxsize
    key = None 
    for d in Direction:
        if dist[(end[0], end[1], d)][0] < min:
            min = dist[(end[0], end[1], d)][0]
            key = (end[0], end[1], d)
    
    print(key)
    print(dist[key])
    
    visited = depth_first_search_back(dist, key)
    
    # remove multi directions
    duplicates_remove = set()
    for v in visited:
        duplicates_remove.add((v[0], v[1]))

    
    print(len(duplicates_remove))
    
    

   



if __name__ == '__main__':
    main()

