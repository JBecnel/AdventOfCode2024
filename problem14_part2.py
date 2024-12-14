dBug = False

import numpy as np
import re 
def parse_input():
    # Read the input file
    file_path = "puzzle14_sample.dat"
    file_path = "puzzle14.dat"
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]

    position = []
    velocity = []
    Prize = [ ]
    for i in range(0, len(lines)):
        numbers = re.findall(r"-?\d+", lines[i]) # find all the numbers
        numbers = list(map(int, numbers))  # Convert to integer
        position.append([numbers[0], numbers[1]])
        velocity.append([numbers[2], numbers[3]])
        
    return position, velocity

def move_robots(position, velocity, width, height):


    position[0] = position[0] + velocity[0]
    position[1] = position[1] + velocity[1]

    if position[0] >= width:
        position[0] = position[0] % width
    if position[1] >= height:
        position[1] = position[1] % height

    if position[0] < 0:
        position[0] = width + position[0]
    if position[1] < 0:
        position[1] = height + position[1]
    

def count_in_quads(positions, quad):
    count = 0
    for p in positions:
        if quad[0][0] <= p[0] <= quad[1][0] and quad[0][1] <= p[1] <= quad[1][1]:
            count += 1
    return count

def print_to_file(iteration, positions, width, height):
    pos_set = set()
    for pos in positions:
        pos_set.add((pos[0], pos[1]))
    
    with open('prob14out.txt', 'a') as f:
       print("\n", file=f)
       print(iteration, file=f)
       print("\n", file=f)
       s = ""
       for y in range(height):
            for x in range(width):
               if (x, y) in pos_set:
                    s += "X"
               else:
                    s += "."
            s += "\n"
       print(s,file=f)


def main():
    #W = 11
    #H = 7
    W = 101
    H = 103
    NUM_TURNS = 10000
    pos, vel = parse_input() 
    
    if dBug:
        print(pos)
        print(vel)


    # print the solution to the file and then in the file
    # CTRL + F and find "XXXXX..." the longest  string of X's in the file
    for i in range(NUM_TURNS):
        for k in range(len(pos)):
            move_robots(pos[k], vel[k], W, H)
        print_to_file(i, pos, W, H)
        if dBug: 
            print('turn' , i)
            print(pos)
    
    
if __name__ == '__main__':
    main()
