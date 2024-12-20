import networkx as nx
from enum import Enum


dBug = True


class Direction(Enum):
    UP = (0,-1)
    LEFT = (-1,0)
    DOWN = (0,1)
    RIGHT = (1,0)

def obtain_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]

    start = [1,1]   # starting location
    end = [10,10]   # ending location
    path = set()   # set of all wall locations
    walls = set()     

    # using image coordinates (0,0) is top left
    # x moves left and right
    # y moves up and down    
    # '#' is a wall, '.' is open
    for y in range(1, len(lines)-1):
        for x in range(1, len(lines[y])-1):
            if lines[y][x] != '#':
                path.add((x,y))
                if lines[y][x] == "S":
                    start = (x,y)
                if lines[y][x] == "E":
                    end = (x,y)
            else:
                walls.add((x,y))
            

    return start, end, path, walls, len(lines[0]), len(lines)

# build a digraph out the path information
def build_graph(path):
    G = nx.Graph()
    for p in path:
        for d in Direction:
            x = p[0] + d.value[0]
            y = p[1] + d.value[1]
            if (x,y) in path:
                G.add_edge(p, (x,y))
    return G


def find_path(graph, start, end):
    path = [start]
    current = start
    visited = set()
    visited.add(start)
    while not end in visited:
        for d in Direction:
            x = current[0] + d.value[0]
            y = current[1] + d.value[1]
            if (x,y) in graph and not (x,y) in visited:
                path.append((x,y))
                visited.add((x,y))
                current = (x,y)
    return path 

def main():
    #file_name = "puzzle20_sample.dat"
    file_name = "puzzle20.dat"
    start, end, path, walls, width, height = obtain_input(file_name)
    
    # This is overkill, it can easily be figured out b/c there is only one path
    # from start to finish
    # build a graph find the race track start to finish path
    #graph = build_graph(path)    
    #start_finish = nx.shortest_path(graph, start, end)

    start_finish = find_path(path, start, end)
    
    # the length of race_track is the default time it takes
    default_time = len(start_finish)

    pico =  20
  
    # find the time of traversal for each short cut
    short_cut= { }
    for i in range(0, len(start_finish)):
        for j in range(i+1, len(start_finish)):
            p = start_finish[i]
            q = start_finish[j]
            if abs(p[0]-q[0]) + abs(p[1]-q[1]) <= pico:
                traversal_time = i + (default_time - j) + abs(p[0]-q[0]) + abs(p[1]-q[1])
                short_cut[(i,j)] =  default_time - traversal_time

    # find how many times each traversal time occurs
    count = 0
    for key, val in short_cut.items():
        if val >= 100:      
           count = count + 1

    print(count)
    
    
                




    
                    

        
                    
        


if __name__ == "__main__":
    main()