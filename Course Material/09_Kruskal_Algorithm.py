"""
Kruskal's Algorithm for Finding Minimum Spanning Tree
It is based on Union-Find (Disjoint-Set) Data Structure.
"""
def find_parent(parent_node, node):
    if parent_node[node] != node:
        parent_node[node] = find_parent(parent_node, parent_node[node]) # Path Compression
    return parent_node[node]

def connect_components(parent_node, component_size, node1, node2):
    # Find the parent node of node1 and node2
    node1_parent = parent_node[node1]
    node2_parent = parent_node[node2]

    # Attach the smaller tree to larger tree based on component_sizes
    if component_size[node1_parent] > component_size[node2_parent]:
        parent_node[node2_parent] = node1_parent
        component_size[node1_parent] += component_size[node2_parent]
    else:
        parent_node[node1_parent] = node2_parent
        component_size[node2_parent] += component_size[node1_parent]


import heapq
def kruskal_algo(graph):
    parent_node = {node : node for node in graph} # Intialize all nodes as their own parents
    component_size = {node : 0 for node in graph} # As all nodes have no level.
    result = [] # Resulting MST

    myedges = [] # All (edge_weight, node, neighbor) tuples
    for node in graph:
        neighbors = graph.get(node, [])
        for neighbor, edge_weight in neighbors:
            # Sort nodes to ensure the consistent order for all types of identifiers
            edge = (edge_weight,) + tuple(sorted((node, neighbor)))
            # Check if edge is already in the list.
            if edge not in myedges:
                heapq.heappush(myedges, edge)
    while myedges:
        edge_weight, node1, node2 = heapq.heappop(myedges)
        node1_root = find_parent(parent_node, node1)
        node2_root = find_parent(parent_node, node2)

        # if their parent node were same then they are already in the same component. 
        if node1_root != node2_root:
            result.append((node1, node2, edge_weight))
            connect_components(parent_node, component_size, node1, node2) # Now connect their respective components
    return result
#---------------------------------------------------------------
#---------------------------------------------------------------
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
MST = kruskal_algo(graph=network)
print(MST)