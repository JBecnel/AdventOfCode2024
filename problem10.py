# read the contents of the file line by line
#file_path = 'puzzle10_sample5.dat'
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
def hasPathBetween(v, w, visited, G):
    if v == w:
        return True
    else:
        x = v[0]
        y = v[1]
        visited.add(v)
        neighbors = [(x+1,y),(x-1,y), (x, y+1), (x,y-1)]
        for n in neighbors:
            if n in G and n not in visited:
                if G[n] == G[v]+1:   # can only go up one elevation at a time
                    if hasPathBetween(n, w, visited, G):
                        return True                
        return False


count = 0 # count the number of end points 9, you can get to from the start 0
for start in graph[0]:
    for end in graph[9]:
        if hasPathBetween(start, end, set(), inverse):
            count = count + 1

print(count)



        