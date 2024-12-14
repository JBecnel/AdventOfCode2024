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

    # Parse the input data and store it in list
    # first two numbers are positions
    # second two numbers are velocity
    position = []
    velocity = []
    for i in range(0, len(lines)):
        numbers = re.findall(r"-?\d+", lines[i]) # find all the numbers
        numbers = list(map(int, numbers))  # Convert to integer
        position.append([numbers[0], numbers[1]])
        velocity.append([numbers[2], numbers[3]])
        
    return position, velocity

def move_robots(position, velocity, width, height):

    # move the robots according to each velocity
    position[0] = position[0] + velocity[0]
    position[1] = position[1] + velocity[1]

    # wrap around the to beginning of grid if necessary
    if position[0] >= width:
        position[0] = position[0] % width
    if position[1] >= height:
        position[1] = position[1] % height

    # wrap around the to end of grid if necessary
    if position[0] < 0:
        position[0] = width + position[0]
    if position[1] < 0:
        position[1] = height + position[1]
    

def count_in_quads(positions, quad):
    # count the number of robots in the specified quadrant
    # given the robot positions
    # given the quadrant coordinates
    count = 0
    for p in positions:
        if quad[0][0] <= p[0] <= quad[1][0] and quad[0][1] <= p[1] <= quad[1][1]:
            count += 1
    return count

def main():
    #W = 11
    #H = 7
    W = 101
    H = 103
    NUM_TURNS = 100
    pos, vel = parse_input() 
    
    if dBug:
        print(pos)
        print(vel)


    for i in range(NUM_TURNS):
        for k in range(len(pos)):
            move_robots(pos[k], vel[k], W, H)
        if dBug: 
            print('turn' , i)
            print(pos)
    
    
    if dBug:
        print(pos)

    # quadrants by top left to bottom right
    quads = [ [  (0, 0),  (W //2  - 1, H //2 - 1 ) ],  # top left
              [  ( W//2+1, 0), ( W, H //2-1)  ],  # top right
              [  ( 0, H //2+1),  (W //2-1, H-1)  ],
              [  (W // 2+1, H //2+1), (W-1, H-1)  ] ]
    
    # find the solution by multiplying the number of robots in each quadrant
    total = 1
    for quad in quads:
        total *= count_in_quads(pos, quad)
        
        if dBug:
            print('quad', count_in_quads(pos, quad))
            print(quad)
    
    print(total)
        

    
    
if __name__ == '__main__':
    main()
