import networkx as nx

def construct_graph(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    lines = [line.strip() for line in lines]
    graph = nx.Graph()
    for line in lines:
        edge = line.split('-')
        graph.add_edge(edge[0], edge[1])
        
    return graph

def password(clique):
    sorted_clique = sorted(clique)
    str = ""
    for c in sorted_clique:
        str = str + "," +  c
    return str

def main():
    #file_path = "puzzle23_sample.dat"
    file_path = "puzzle23.dat"
    graph = construct_graph(file_path)
    clique = max(nx.find_cliques(graph), key=len)  
    
    answer = password(clique)
    print(answer)
if __name__ == "__main__":
    main()