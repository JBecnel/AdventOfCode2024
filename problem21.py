import sys
import networkx as nx
from enum import Enum
from collections import deque

# failed attempt


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
    
#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+   

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+
def get_paths_for_keys():
    keys = [     'A',    '0', '1',     '2',   '3',   '4', '5',     '6',   '7', '8', '9']
    locations = [(2,3), (1,3), (0,2), (1,2), (2,2), (0,1), (1,1), (2,1), (0,0), (1,0), (2,0)]
    key_path = { }
    for i in range(len(keys)):
        for j in range(len(keys)):
            key1 = keys[i]
            key2 = keys[j]
            if (i == j):
                key_path[(key1,key2)] = "A"
            else:
                str = ""
                # key2 - key1 
                hor = locations[j][0]- locations[i][0]
                ver = locations[j][1] - locations[i][1]
                # go left, then up/down, then right except if you are going to hit blank
                
                # get left 
                if hor < 0:
                    str = "<" * abs(hor)
                if ver < 0:
                    str += "^" * abs(ver)
                else:
                    str += "v" * ver
                    
                if hor > 0:
                    str += ">" * hor
                
                key_path[(key1,key2)] = str + "A"
                
    # fix the incorrect ones
    key_path[('A', '1')] = "^<<A"
    key_path[('A', '4')] = "^^<<A"
    key_path[('A', '7')] = "^^^<<A"
    key_path[('1', 'A')] = ">>vA"
    key_path[('4', 'A')] = ">>vvA"
    key_path[('7', 'A')] = ">>vvvA"
    
    key_path[('0', '1')] = "^<A"
    key_path[('0', '4')] = "^^<A"
    key_path[('0', '7')] = "^^^<A"
    key_path[('1', '0')] = ">vA"
    key_path[('4', '0')] = ">vvA"
    key_path[('7', '0')] = ">vvvA"
    
    
    return key_path


# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

                    
  #  379A: <v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+   
def get_paths_for_dirs():
    keys = ['A', '>', '^', 'v', '<']
    locations = [(2,0), (2,1), (1,0), (1,1), (0,1)]
    
    # go left, then up/dow, then rigth (unless a blank)
    key_path = { }
    for i in range(len(keys)):
        for j in range(len(keys)):
            key1 = keys[i]
            key2 = keys[j]
            if (i == j):
                key_path[(key1,key2)] = "A"
            else:
                str = ""
                # key2 - key1 
                hor = locations[j][0]- locations[i][0]
                ver = locations[j][1] - locations[i][1]
                # go left, then up/down, then right except if you are going to hit blank
                
                # get left 
                if hor < 0:
                    str += "<" * abs(hor)
                if ver < 0:
                    str += "^" * abs(ver)
                else:
                    str += "v" * ver    
                if hor > 0:
                    str += ">" * hor
                 
                key_path[(key1,key2)] = str + "A"
                
    # fix the two incorrect ones
    key_path[('A', '<')] = "v<<A"
    key_path[('^', '<')] = "v<A"
    key_path[('<', 'A')] = ">>^A"
    key_path[('<', '^')] = ">^A"
    return key_path
                
    
#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+   
# <vA<AA>>^A vAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
# v<<A >>^A<A>AvA<^AA>A<vAAA>^A
# A<A^A>^^AvvvA                
   


def parse_code(code,num_paths):
    code = "A" + code
    str = ""
    for i in range(len(code)-1):
        key1 = code[i]
        key2 = code[i+1]
        str += num_paths[(key1,key2)]
        
    return str 

def get_dir_path_length(dir_paths):
    length = { }
    for key in dir_paths:
        path = dir_paths[key]
        length[key] = len(path)
    return length

def reverse(dir_length, dir_paths):
    new_lengths = { }
    for key in dir_length:
        path =  dir_paths[key]
        sum = 0
        for i in range(len(path)-1):
            key1 = path[i]
            key2 = path[i+1]
            sum =  sum + dir_length[(key1,key2)]
        if key[0] != key[1]:
            new_lengths[key] = sum
        else:
            new_lengths[key] = 1
    return new_lengths

def code_length(dir_length, code):
    sum = 0
    code = "A" + code
    for i in range(len(code)-1):
        key1 = code[i]
        key2 = code[i+1]
        sum =  sum + dir_length[(key1,key2)]
    return sum

def main():
    file_name = "puzzle21_sample.dat"
    file_name = "puzzle21.dat"
    codes = obtain_input(file_name)

    
    num_paths = get_paths_for_keys()
    #print(num_paths)
    print()
    dir_paths = get_paths_for_dirs()
    
    # create start path length
    dir_length = get_dir_path_length(dir_paths)
    print(dir_paths)
    print()
    print(dir_length) 

    for i in range(2):
        dir_length = reverse(dir_length, dir_paths)
        print(dir_length)
        print()
        
    print()
    lengths = [ ]
    for code in codes:
        #print(code)
        start = parse_code(code,  num_paths)
        print(start)
        length = code_length(dir_length, start)
        #for i in range(25):
            #print(start)
            #start = parse_code(start, dir_paths)
        #print(start)
        lengths.append(length)
        print(length)
   
    
    with open(file_name, 'r') as file:
        numbers = [int(line.strip()[:-1].lstrip('0')) for line in file if line.strip().endswith('A')]
    print(numbers)

    answer  = 0
    for i in range(len(codes)):
        answer += lengths[i] * numbers[i]

    print(answer)

if __name__ == "__main__":
    main()