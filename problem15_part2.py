dBug = False  # flag to print debug statements 

def obtain_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]


    robot = [0,0]   # robot location
    boxes_left_side = set()   # set of all box locations (left side of box, right next is one over in x direction)
    boxes_right_side = set() # set of all box locations (right side of box, left next is
    walls = set()   # set of all wall locations
    moves = []      # list of all moves to make in order

    # using image coordinates (0,0) is top left
    # x moves left and right
    # y moves up and down
    # '^' is up, '>' is right, '<' is left, 'v' is down
    # '#' is a wall, 'O' is a box, '@' is the robot
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == '^':
                moves.append((0,-1))   # x does not change, y goes up
            elif lines[y][x] == '>':
                moves.append((1,0)) 
            elif lines[y][x] == '<':
                moves.append((-1,0)) 
            elif lines[y][x] == 'v':
                moves.append((0,1))
            else:
                widen_x = 2 * x  
                if lines[y][x] == '#':
                    walls.add((widen_x,y))
                    walls.add((widen_x+1,y))
                elif lines[y][x] == 'O':
                    boxes_left_side.add((widen_x, y))  
                    boxes_right_side.add((widen_x+1, y))
                elif lines[y][x] == '@':
                    robot[0] = widen_x
                    robot[1] = y

    return robot, boxes_left_side, boxes_right_side, walls, moves      

    
def move_vertical(robot, boxes, move_y, wall_loc):
    x = robot[0]
    y = robot[1]
    
    new_y = y + move_y 
    
    # wall blocking robot
    if (x,new_y) in wall_loc:
        return False
    # open spot, not wall or box
    elif (x,new_y) not in boxes and (x-1, new_y) not in boxes:
        return True   
    else:  # there is a box in the way
        boxes_to_move = set()
        if (x,new_y) in boxes:
            box_x = x
            box_y = new_y 
        if (x-1, new_y) in boxes:
             box_x = x-1
             box_y = new_y
        # check if there is wall blocking any of the boxes
        can_move = move_boxes((box_x, box_y), boxes, move_y, wall_loc, boxes_to_move)

        # adjust the boxes if possible
        if can_move:
            for box in boxes_to_move:
                boxes.remove(box)
            for box in boxes_to_move:
                boxes.add((box[0], box[1]+move_y))
        return can_move

def move_boxes(box_loc, boxes, move_y, walls, boxes_to_move):
    # cases for move down (robot above left or right)
    #   []    []    []   []      []   []   []
    #  [][]    []  []    []      ..   #.   .#
    
    # location of first box 
    x = box_loc[0]
    y = box_loc[1]
    boxes_to_move.add((x,y))

    # next location 
    next_x = x
    next_y = y+move_y 

    # Case 6 and 7000
    if (next_x, next_y) in walls or (next_x+1, next_y) in walls:
        boxes_to_move = set() # empty the set, we are blocked, no need to move
        return False
    else:
        # one box below Case 4
        if (next_x, next_y) in boxes:
           return move_boxes((next_x, next_y),boxes, move_y, walls, boxes_to_move)
        else:
            # box on the bottom left
            box1 = True 
            box2 = True
            if (next_x-1, next_y) in boxes: 
                box1 = move_boxes((next_x-1, next_y),boxes, move_y, walls, boxes_to_move)
            # box on the bottom right
            if (next_x+1, next_y) in boxes: 
                box2 = move_boxes((next_x+1, next_y),boxes, move_y, walls, boxes_to_move)
            return box1 and box2
        


def move_left(robot, boxes, walls):
    # get position to check
    x = robot[0]-2
    y = robot[1]
    
    # find how long the row of boxes is
    box_set = set()
    while ((x,y) in boxes ):
        box_set.add((x,y))
        x = x - 2  # move left

    # position to the left of all boxes
    x = x + 1

    # at this point we arrived (x,y) at something that is not a box
    # if it is a wall, we are stuck
    # if not, we move the boxes 
    if (x,y) in walls:
        return False
    else: # x,y is an empty space
        # move the boxes over one to the left
        for box in box_set:
            boxes.remove(box)
            boxes.add((box[0]-1, y))
        return True
    
def move_right(robot, boxes, walls):
    # wall to the right, cannot move
    if (robot[0]+1, robot[1]) in walls:
        return False 
    # get position to check for box 
    x = robot[0]+1
    y = robot[1]
    
    # find how long the row of boxes is
    box_set = set()
    while ((x,y) in boxes ):
        box_set.add((x,y))
        x = x + 2  # move right to next possible box

    # position to the right of all boxes is x

    # at this point we arrived (x,y) at something that is not a box
    # if it is a wall, we are stuck
    # if not, we move the boxes 
    if (x,y) in walls:
        return False
    else: # x,y is an empty space
        # move the boxes over one to the right
        for box in box_set:
            boxes.remove(box)
            boxes.add((box[0]+1, y))
        return True

def process_move(move, robot, boxes, walls):
    new_x = robot[0] + move[0]
    new_y =  robot[1] + move[1]
    move_robot = False
    if (new_x, new_y) not in walls:
        # check and see the boxes can be moved
        # the method also moves the boxes
        if move[0] == -1: 
            move_robot = move_left(robot, boxes, walls)
        elif move[0] == 1:
            move_robot = move_right(robot, boxes, walls)
        else:
            move_robot = move_vertical(robot, boxes, move[1], walls)
  
    # move the robot
    if move_robot:
        robot[0] = new_x
        robot[1] = new_y
    
            
            
def main():
    file_path = "puzzle15_sample1.dat"
    file_path = "puzzle15.dat"
    robot, boxes_left, boxes_right,  walls, moves = obtain_input(file_path)

    # print initial state
    if dBug:
        print(f"Robot: {robot}")
        print(f"Boxes Left: {boxes_left}")
        print(f"Boxes Right: {boxes_right}")
        print(f"Walls: {walls}")
        print(f"Moves: {moves}")
        print()
    
    # process all the moves
    for move in moves:
        process_move(move, robot, boxes_left, walls)
        if dBug:
            write_to_file('debug.txt', move, robot, boxes_left, walls)
            
    # compute the score
    score = 0
    for box in boxes_left:
        score = score + 100*box[1] + box[0] 

    print(score)
    
def write_to_file(filename, move, robot, boxes_left, walls):
    with open(filename, 'a') as f:
        print("\n", file=f)
        print(move , file=f)
        print(robot, file=f)
        print("\n", file=f)
        s = ""
        
        WIDTH = 20
        HEIGHT = 10
        skip = False
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if not skip:
                    if (x,y) in walls:
                        s += "#"
                    elif (x,y) in boxes_left:
                        s += "[]"
                        skip =True
                    elif (x,y) == (robot[0], robot[1]):
                        s += "@"
                    else:
                        s+="."
                else:
                    skip = False 
            s += "\n"
        print(s,file=f)
    

if __name__ == '__main__':
    main()