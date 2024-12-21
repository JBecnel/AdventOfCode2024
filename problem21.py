import sys
import networkx as nx
from enum import Enum
from collections import deque

dBug = True


class Buttons(Enum):
    UP = '^'
    LEFT = '<'
    DOWN = 'v'
    RIGHT = '>'
    ACTIVATE = 'A'

def obtain_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]

    return lines

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+
def key_pad_graph():
    G = nx.DiGraph()
    G.add_edge('A', '0', label=Buttons.LEFT) 
    G.add_edge('A', '3', label=Buttons.UP)
    
    G.add_edge('0','A', label=Buttons.RIGHT) 
    G.add_edge('0', '2', label=Buttons.UP)

    G.add_edge('1', '2', label=Buttons.RIGHT)
    G.add_edge('1', '4', label=Buttons.UP)

    G.add_edge('2', '1', label=Buttons.LEFT)
    G.add_edge('2', '0', label=Buttons.DOWN)
    G.add_edge('2', '3', label=Buttons.RIGHT)
    G.add_edge('2', '5', label=Buttons.UP)

    G.add_edge('3', '2', label=Buttons.LEFT)
    G.add_edge('3', 'A', label=Buttons.DOWN)
    G.add_edge('3', '6', label=Buttons.UP)

    G.add_edge('4', '1', label=Buttons.DOWN)
    G.add_edge('4', '5', label=Buttons.RIGHT)
    G.add_edge('4', '7', label=Buttons.UP)

    G.add_edge('5', '2', label=Buttons.DOWN)
    G.add_edge('5', '4', label=Buttons.LEFT)
    G.add_edge('5', '6', label=Buttons.RIGHT)
    G.add_edge('5', '8', label=Buttons.UP)

    G.add_edge('6', '3', label=Buttons.DOWN)
    G.add_edge('6', '5', label=Buttons.LEFT)
    G.add_edge('6', '9', label=Buttons.UP)

    G.add_edge('7', '4', label=Buttons.DOWN)
    G.add_edge('7', '8', label=Buttons.RIGHT)

    G.add_edge('8', '5', label=Buttons.DOWN)
    G.add_edge('8', '7', label=Buttons.LEFT)
    G.add_edge('8', '9', label=Buttons.RIGHT)

    G.add_edge('9', '6', label=Buttons.DOWN)
    G.add_edge('9', '8', label=Buttons.LEFT)

    return G
    
    
#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+   
def direction_pad_graph():
    G = nx.DiGraph()
    G.add_edge('A', '^', label=Buttons.LEFT)
    G.add_edge('A', '>', label=Buttons.DOWN)
    
    G.add_edge('^', 'A', label=Buttons.RIGHT)
    G.add_edge('^', 'v', label=Buttons.DOWN)

    G.add_edge('<', 'v', label=Buttons.RIGHT)
    
    G.add_edge('v', '>', label=Buttons.RIGHT)
    G.add_edge('v', '<', label=Buttons.LEFT)
    G.add_edge('v', '^', label=Buttons.UP)

    G.add_edge('>', 'v', label=Buttons.LEFT)
    G.add_edge('>', 'A', label=Buttons.UP)

    return G

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+
def get_paths_for_keys(key_graph):
    keys = ['A', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    key_paths = { }
    for k1 in keys:
        for k2 in keys:
            if k1 != k2:
                paths = nx.all_shortest_paths(key_graph, k1, k2)
                path_list = [ ]
                for p in paths:
                    path = p
                    path_str = ""
                    for k in range(len(path)-1):
                        path_str += key_graph[path[k]][path[k+1]]['label'].value
                    path_list.append(path_str)
                key_paths[(k1,k2)] = path_list
                
                
    return key_paths

def get_paths_for_dirs(dir_graph):
    keys = ['A', '>', '^', 'v', '<']
    key_paths = { }
    for k1 in keys:
        for k2 in keys:
            paths = nx.all_shortest_paths(dir_graph, k1, k2)
            path_list = [ ]
            for p in paths:
                path = p
                path_str = ""
                for k in range(len(path)-1):
                    path_str += dir_graph[path[k]][path[k+1]]['label'].value
                path_list.append(path_str)
            key_paths[(k1,k2)] = path_list
            
                
                
    return key_paths



def weight_dict_last(graph):
    weight = { }
    for b1 in Buttons:
        for b2 in Buttons:
            if b1 != b2:
                path = nx.shortest_path(graph, b1.value, b2.value)
                weight[(b1.value, b2.value)] = len(path)
            else:
                weight[(b1.value, b2.value)] = 1

    return weight



def generate_first_strings(code, num_paths):
    code = "A" + code
    all_paths = [ "" ]
    for i in range(len(code)-1):
        key = (code[i], code[i+1])
        all_paths = [ a + b + "A" for a in all_paths for b in num_paths[key]]

    return all_paths

def generate_second_strings(str, dir_paths):
    str = "A" + str
    all_paths = [ "" ]
    for i in range(len(str)-1):
        key = (str[i], str[i+1])
        all_paths = [ a + b + "A" for a in all_paths for b in dir_paths[key]]

    return all_paths

def find_best(second_possible, last_key_pad):
    best = sys.maxsize
    for s in second_possible:
        s = "A" + s
        total = 0
        for i in range(len(s)-1):
            total += last_key_pad[(s[i], s[i+1])]
        if total < best:
            best = total

    return best

def main():
    file_name = "puzzle21_sample.dat"
    file_name = "puzzle21.dat"
    codes = obtain_input(file_name)

    num_pad_G = key_pad_graph()
    dir_pad_G = direction_pad_graph()
    last_key_pad = weight_dict_last(dir_pad_G)
    
    print(last_key_pad)

    num_paths = get_paths_for_keys(num_pad_G)
    #print(num_paths) 


    dir_paths = get_paths_for_dirs(dir_pad_G)
    print(dir_paths)
    
    with open(file_name, 'r') as file:
        numbers = [int(line.strip()[:-1].lstrip('0')) for line in file if line.strip().endswith('A')]
    print(numbers)

    answer  = 0
    for i in range(len(codes)):
        code = codes[i]
        first_possibles = generate_first_strings(code, num_paths)
        #print(first_possibles)

        second_possible = [ ]
        for str in first_possibles:
            second_possible += generate_second_strings(str, dir_paths)

        #print(second_possible)

        length = find_best(second_possible, last_key_pad)
        answer += length *  numbers[i]

    print(answer)

if __name__ == "__main__":
    main()