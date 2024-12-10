# read the contents of the file line by line
file_path = 'puzzle10_sample5.dat'
file_path = "puzzle10.dat"
with open(file_path, 'r') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]


# create the graph using dictionarys
graph = { }   # key is elevation, values is a list of locations
inverse = { } # key is location, values is the elevations
for r in range(len(lines)):
    for c in range(len(lines[0])):
        if lines[r][c] != '.':
            location = (r,c)
            elevation = int(lines[r][c])
            if elevation in graph:
                graph[elevation].append(location)
            else:
                graph[elevation] = [(location)]
            inverse[location] = elevation



# determine if there is a path between the locations v, w 
# in the graph G
# visited keeps track of nodes already visited
def countPathsBetween(v, w, visited, G):
    if v == w:
        return 1
    else:
        x = v[0]
        y = v[1]
        visited.add(v)
        neighbors = [(x+1,y),(x-1,y), (x, y+1), (x,y-1)]
        total_paths = 0 # count the total paths from v to w
        # find the totals number of paths each of v's neighbors to w
        for n in neighbors:
            if n in G and n not in visited:
                if G[n] == G[v]+1:   # can only go up one elevation at a time                
                    # note the copy of the visited set
                    # nodes can be revisited as long as we are on a different path
                    total_paths = total_paths + countPathsBetween(n, w, visited.copy(), G)
                    # note 

        return total_paths



# count the number of paths from elevation 0 to elevation 9
count = 0 
for start in graph[0]:
    for end in graph[9]:
        # set() is a set of visited nodes (currently empty)
        # we use the inverse dictionary ( locations -> elevation)
        count = count + countPathsBetween(start, end, set(), inverse)
            

print(count)       