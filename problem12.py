dBug = False

# read the contents of the file line by line
#file_path = 'puzzle10_sample5.dat'
def main():
    file_path = "puzzle12_sample2.dat"
    file_path = 'puzzle12.dat'
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]

    # create the plant and location graphs
    # key is plant, values is a list of locations
    # key is location, values is the plant
    plant_graph, location_graph = create_graphs(lines)
    
    if dBug: 
        print("plant graph")
        print(plant_graph)
        print("location graph")
        print(location_graph)

    # find the price of the fences
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


# This helper functions finds
# a connected plot containing the given
# plant and the given starting location
def fill_plot(plot, plant, location, loc_G, visited):
    plot.append(location)
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

    
    
# Find all plots that contain the given plant
def find_all_plots(plant, locations, loc_G):
    
    plots = []  # lists (of lists) of the various plots containing the given plant
    visited = set()
    
    for location in locations:
        plot = []
        if location not in visited:
            fill_plot(plot, plant, location, loc_G, visited)
            plots.append(plot)

    if dBug:
        print("plants ", plant, "plots ", plots)

    return plots 

# Compute the price of the fence given the information
def compute_price(plant, locations, loc_G):
    
    plots = find_all_plots(plant, locations, loc_G)
    price = 0
    for plot in plots:
        perimeter = 0
        # up down left right directions
        directions = [(0,-1), (0,1), (-1,0), (1,0)]
        for location in plot:
            for dir in directions:
                row = location[0] + dir[0]
                col = location[1] + dir[1]
                
                if (row, col) in loc_G:
                    if loc_G[row, col] != plant:
                        perimeter = perimeter + 1
                else:
                    perimeter = perimeter + 1 
        # len(plot) is the area
        price = price + perimeter * len(plot)
    return price
    

def fence_price(plant_G, loc_G):
    price = 0
    for plant in plant_G:
        price = price + compute_price(plant, plant_G[plant], loc_G) 
    return price

if __name__ == '__main__':
    main()