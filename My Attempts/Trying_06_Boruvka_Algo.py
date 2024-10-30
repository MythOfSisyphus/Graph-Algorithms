def first_step(graph):
    result = {}
    for node in graph:
        min_edge_node, min_edge = None, float('inf')
        neighbors = graph.get(node, [])
        for neighbor, edge_weight in neighbors:
            if edge_weight < min_edge:
                min_edge = edge_weight
                min_edge_node = neighbor
        result[node] = (min_edge_node, min_edge)
    return result

        
network = {
    'A' : [('B', 4), ('C', 7)],
    'B' : [('A', 4), ('C', 11), ('D', 9), ('F', 20)],
    'C' : [('A', 7), ('B', 11), ('F', 1)],
    'D' : [('B', 9), ('E', 2), ('G', 6)],
    'E' : [('D', 2), ('F', 1), ('H', 5), ('G', 10), ('I', 15)],
    'F' : [('C', 1), ('B', 20), ('E', 1), ('H', 3)],
    'G' : [('D', 6), ('I', 5), ('E', 10)],
    'H' : [('E', 5), ('F', 3), ('I', 12)],
    'I' : [('G', 5), ('E', 15), ('H', 12)]
}
print(first_step(graph=network))