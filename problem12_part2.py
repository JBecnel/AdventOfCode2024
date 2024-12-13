dBug = False

# read the contents of the file line by line
#file_path = 'puzzle10_sample5.dat'
def main():
    file_path = "puzzle12_sample2.dat"
    file_path = 'puzzle12.dat'
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]

    plant_graph, location_graph = create_graphs(lines)
    
    if dBug: 
        print("plant graph")
        print(plant_graph)
        print("location graph")
        print(location_graph)

    print(fence_price(plant_graph, location_graph))

def create_graphs(plot):
    # create the graph using dictionarys
    graph = { }  # key is plant, values is a list of locations
    inverse = { } # key is location, values is the plant
    for r in range(len(plot)):
        for c in range(len(plot[0])):
            location = (r,c)
            plant = plot[r][c]
            if plant in graph:
                graph[plant].append(location)
            else:
                graph[plant] = [(location)]
            inverse[location] = plant

    return graph, inverse


def fill_plot(plot, plant, location, loc_G, visited):
    plot.add(location)
    visited.add(location)

    # up down left right directions
    directions = [(0,-1), (0,1), (-1,0), (1,0)]
    for dir in directions:
        row = location[0] + dir[0]
        col = location[1] + dir[1]
        if (row, col) not in visited:
                if (row, col) in loc_G:
                    if loc_G[row, col] == plant:
                        fill_plot(plot, plant,(row, col), loc_G, visited)

    #return plot 
    
# finds all the seperate plots 
# holding the given plant
# and all the locations the plant occurs
# a list of sets with each set being a separate plot
# is returns
def find_all_plots(plant, locations, loc_G):
    plots = []
    visited = set()
    
    for location in locations:
        plot = set()
        if location not in visited:
            fill_plot(plot, plant, location, loc_G, visited)
            plots.append(plot)

    return plots 

# This method counts the number of fence sides
# we check if each potential square is a new possible
# left, up, down, or right side
def find_sides(plot, plant, loc_G):
    # left, right, up, down
    sides = 0
    for square in plot:
        # left, right, up, down
        up = (square[0] -1, square[1])
        down = (square[0]+1, square[1])
        left = (square[0], square[1]-1)
        right = (square[0], square[1]+1)
        up_left = (square[0]-1, square[1]-1)
        up_right = (square[0]-1, square[1]+1)
        down_left = (square[0]+1, square[1]-1)
        if left not in plot: # potential new left, check above
            if up not in plot: 
                sides = sides + 1
            elif up_left  in plot:
                sides = sides + 1

        if right not in plot: # potential new right, check above
            if up not in plot:
                sides = sides + 1
            elif up_right  in plot:
                sides = sides + 1
        
        if up not in plot: # potential new up, check above and left
            if left not in plot:
                sides = sides + 1
            elif up_left  in plot:
                sides = sides + 1
        
        if down not in plot: # potential new down, check below and right
            if left not in plot:
                sides = sides + 1
            elif down_left in plot:
                sides = sides + 1

    return sides            

def compute_price(plant, locations, loc_G):
    # find all the plots holding the given plant     
    plots = find_all_plots(plant, locations, loc_G)

    if dBug:
        print("plant", plant, "plots", plots)

    price = 0
    for plot in plots:
        # find the number of sides for the given plot
        sides = find_sides(plot, plant, loc_G)

        # increment the fence price
        price = price + sides * len(plot)
    return price
    

def fence_price(plant_G, loc_G):
    price = 0
    for plant in plant_G:
        price = price + compute_price(plant, plant_G[plant], loc_G) 
    return price

if __name__ == '__main__':
    main()