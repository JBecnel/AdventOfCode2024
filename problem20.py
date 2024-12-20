import networkx as nx
from enum import Enum
from collections import deque

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
    

    # using image coordinates (0,0) is top left
    # x moves left and right
    # y moves up and down    
    # '#' is a wall, '.' is open
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] != '#':
                path.add((x,y))
                if lines[y][x] == "S":
                    start = [x,y]
                if lines[y][x] == "E":
                    end = [x,y]
            

    return start, end, path, len(lines[0]), len(lines)

# build a digraph out the path information
def build_graph(path):
    G = nx.DiGraph()
    for p in path:
        for d in Direction:
            x = p[0] + d.value[0]
            y = p[1] + d.value[1]
            if (x,y) in path:
                G.add_edge(p, (x,y))
                G.add_edge((x,y), p)

    return G


def main():
    file_name = "puzzle20_sample.dat"
    #file_name = "puzzle20.dat"
    start, end, path, width, height = obtain_input(file_name)
    graph = build_graph(path)
    result = nx.shortest_path(graph, (start[0], start[1]), (end[0], end[1]))
    
    default_time = len(result)

    if dBug:
        print(result)
        print(default_time)
        print("start ", start, "end ", end, " width ", width, " height ", height) 
        print(graph.number_of_nodes())
        print(graph.number_of_edges())
        print(graph[(1,1)], graph[(2,1)])
        #graph.add_edge((7,1), (8,1))
        #graph.add_edge((8,1), (9,1))
        #result = nx.shortest_path(graph, (start[0], start[1]), (end[0], end[1]))
        print()


    time_saved = { }
    for y in range(1, height-1):
        for x in range(1, width-1):
    #for y in range(1,3):
     #   for x in range(7,10):
            if not (x,y) in graph:  # if we find a wall
                # attempt to jump over it (if possbile)
                for d in Direction:
                    v = (x-d.value[0], y - d.value[1])
                    u = (x+d.value[0], y + d.value[1])
                    if u in graph and v in graph:
                        graph.add_edge(u,v) # jump over the wall
                        
                        # find the shortest path from start to end
                        new_result = nx.shortest_path(graph, (start[0], start[1]), (end[0], end[1]))                        
                        
                        # track all improvemetns over a 100
                        improvement = default_time - len(new_result) - 1   # -1 for "skipped" wall space
                        if improvement < 0:
                            improvement = 0
                        elif improvement >= 100:
                            if improvement in time_saved:
                                time_saved[improvement] = time_saved[improvement] + 1
                            else:
                                time_saved[improvement] = 1                
                        graph.remove_edge(u,v)
                        
    if dBug:
        print(dict(sorted(time_saved.items())))

    count = 0
    for key, val in time_saved.items():
        count = count + val

    print(count)
        


if __name__ == "__main__":
    main()