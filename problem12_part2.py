dBug = True

# read the contents of the file line by line
#file_path = 'puzzle10_sample5.dat'
def main():
    file_path = "puzzle12_sample3.dat"
    #file_path = 'puzzle12.dat'
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

    #return plot 
    

def find_all_plots(plant, locations, loc_G):
    plots = []
    visited = set()
    
    for location in locations:
        plot = []
        if location not in visited:
            fill_plot(plot, plant, location, loc_G, visited)
            plots.append(plot)

    

    return plots 


def compute_price(plant, locations, loc_G):
    
    plots = find_all_plots(plant, locations, loc_G)
    price = 0
    for plot in plots:
        sides = 0
        # left, right, up, down
        directions = [(0,-1), (0,1), (-1,0), (1,0)]
        row_visited = set()
        col_visited = set()
        for location in plot:
            for i in range(len(directions)):
                dir = directions[i]
                row = location[0] + dir[0]
                col = location[1] + dir[1]
                
                if dBug:
                    print("plant ", plant, "location ", location, "r/c", (row, col), "side ", sides)

                if (i >=2):  # up/down
                    if (row, col) in loc_G:
                        if loc_G[row, col] != plant:
                            if row not in row_visited:
                                row_visited.add(row)
                                sides = sides + 1 
                        
                    else:
                        if row not in row_visited:
                            row_visited.add(row)
                            sides = sides + 1 
                else: 
                    if (row, col) in loc_G:
                        if loc_G[row, col] != plant:
                            if col not in col_visited:
                                col_visited.add(col)
                                sides = sides + 1 
                        
                    else:
                        if col not in col_visited:
                            col_visited.add(col)
                            sides = sides + 1 

                if dBug:
                    print("side " , sides)

                    
        if dBug:
          print("plant ", plant, "plots ", plot, "sides ", sides)    
        
        price = price + sides * len(plot)
    return price
    

def fence_price(plant_G, loc_G):
    price = 0
    for plant in plant_G:
        price = price + compute_price(plant, plant_G[plant], loc_G) 
    return price

if __name__ == '__main__':
    main()