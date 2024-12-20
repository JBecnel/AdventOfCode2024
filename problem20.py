import networkx as nx
from enum import Enum
from collections import deque


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
    # S is start, E is end
    # '#' is a wall, '.' is open
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] != '#':
                path.add((x,y))
                if lines[y][x] == "S":
                    start = [x,y]
                if lines[y][x] == "E":
                    end = [x,y]
            

    return start, end, path

def build_graph(path):
    G = nx.DiGraph()
    for p in path:
        for d in Direction:
            x = p[0] + d[0]
            y = p[1] + d[1]
            G.add_edge(p, (x,y))

    return G


def main():
    file_name = "puzzle20_sample.dat"
    start, end, path = obtain_input(file_name)
    graph = build_graph(path)
    

if __name__ == "__main__":
    main()