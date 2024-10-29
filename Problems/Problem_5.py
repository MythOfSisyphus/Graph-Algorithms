"""
Problem: Determine whether a given graph is Bipartite Graph or not.

A graph G=(N, E) is called a bipartite graph if its nodes N can be
partitioned into two subsets N1 and N2 such that each edge of G connects
a node of N1 to a node N2. It is denoted by Kmn, where m and n are the
numbers of nodes in N1 and N2 respectively.

See image here (https://www.researchgate.net/figure/Complete-bipartite-graph_fig2_338987850)

Explanation: #TODO
"""
from queue import Queue
def isBipartite(graph, start_node):
    subgraph_1 = {start_node} # let start_node be in first subgraph
    subgraph_2 = set()
    visited = {start_node} # Mark start_node as visited
    myqueue = Queue()
    myqueue.put((start_node, 1)) # (node, subgraph number) tuple
    while not myqueue.empty():
        current_node, current_subgraph = myqueue.get()

        neighbors = graph.get(current_node, [])
        for neighbor, _ in neighbors:
            # if there is edge between nodes of subgraph_1 then break
            if current_subgraph == 1 and neighbor in subgraph_1:
                return False
            # if there is edge between nodes of subgraph_2 then break
            if current_subgraph == 2 and neighbor in subgraph_2:
                return False
            if neighbor not in visited:
                visited.add(neighbor)
                if current_subgraph == 1: # if current node is in subgraph_1 then
                    subgraph_2.add(neighbor) # add neighbors in subgraph_2
                    myqueue.put((neighbor, 2))
                else: # if current node is in subgraph_2 then
                    subgraph_1.add(neighbor) # add neighbors in subgraph_1
                    myqueue.put((neighbor, 1))
    return True
#-----------------------------------------------------------------------------------

def isBipartite_optimized(graph, start_node):
    color = {start_node : 1} # 1 for 1 subgraph, 2 for other.
    myqueue = Queue()
    myqueue.put(start_node)

    while not myqueue.empty():
        current_node = myqueue.get()
        current_color = color[current_node]

        neighbors = graph.get(current_node, [])
        for neighbor, _ in neighbors:
            # If the neighbor has the same color, then graph isn't Bipartite
            if neighbor in color:
                if color[neighbor] == current_color:
                    return False
            else:
                # Color the neighbor with opposite color
                color[neighbor] = 3 - current_color
                myqueue.put(neighbor)
    return True

G = {
    'A' : {('C', 1), ('E', 1)},
    'B' : {('C', 1), ('D', 1), ('E', 1)},
    'C' : {('A', 1), ('B', 1), ('D', 1)},
    'D' : {('B', 1)},
    'E' : {('A', 1), ('B', 1)}
}

H = {
    0 : {(1, 1)},
    1 : {(0, 1), (2, 1)},
    2 : {(1, 1)}
}

result = isBipartite(graph=H, start_node=0)
print(result)