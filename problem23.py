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

def count_t(cycles):
    count = 0 
    for c in cycles:
        for node in c:
            if node.startswith('t'):
                count += 1
                break
    return count

def main():
    file_path = "puzzle23_sample.dat"
    file_path = "puzzle23.dat"
    graph = construct_graph(file_path)
    
    cycles = nx.simple_cycles(graph, length_bound=3)
    answer = count_t(cycles)
    print(answer)
if __name__ == "__main__":
    main()