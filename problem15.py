dBug = False  # flag to print debug statements 

def obtain_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]

    robot = [0,0]   # robot location
    boxes = set()   # set of all box locations
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
            elif lines[y][x] == '#':
                walls.add((x,y))
            elif lines[y][x] == 'O':
                boxes.add((x, y))  
            elif lines[y][x] == '@':
                robot[0] = x
                robot[1] = y

    return robot, boxes, walls, moves  

def move_boxes(box_loc, boxes, move, wall_loc):
    # check if there is an opening
    x = box_loc[0]
    y = box_loc[1]
    
    # find how long the row of boxes is
    while ((x,y) in boxes ):
        x = x + move[0]
        y = y + move[1]
    # at this point we arrived (x,y) at something that is not a box
    # if it is a wall, we are stuck
    # if not, we move the boxes 
    if (x,y) in wall_loc:
        return False
    else: # x,y is an empty space
        # move the boxes
        # we can simple move the first box to the last open location
        # it has the same effect as shifting all the poxes
        boxes.add((x,y))
        boxes.remove(box_loc)
        return True
        

def process_move(move, robot, boxes, walls):
    new_x = robot[0] + move[0]
    new_y =  robot[1] + move[1]
    if (new_x, new_y) not in walls:
        if (new_x, new_y) in boxes:
            # check and see the boxes can be moved
            # the method also moves the boxes
            if move_boxes((new_x, new_y), boxes, move, walls):
                # move the robot
                robot[0] = new_x
                robot[1] = new_y
        else: # free space, so just move the robot
            # move the robot
            robot[0] = new_x
            robot[1] = new_y
            
            
def main():
    file_path = "puzzle15_sample1.dat"
    file_path = "puzzle15.dat"
    robot, boxes, walls, moves = obtain_input(file_path)

    # print initial state
    if dBug:
        print(f"Robot: {robot}")
        print(f"Boxes: {boxes}")
        print(f"Walls: {walls}")
        print(f"Moves: {moves}")
    
    # process all the moves
    for move in moves:
        process_move(move, robot, boxes, walls)
        if dBug:
            print(f"Robot: {robot}")
            print(f"Boxes: {boxes}")
            print(f"Move   {move}")

    # compute the score
    score = 0
    for box in boxes:
        score = score + 100*box[1] + box[0] 

    print(score)
    

if __name__ == '__main__':
    main()