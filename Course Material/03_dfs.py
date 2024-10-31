"""
Depth-First-Search(DFS): DFS is fundamental graph traversal algorithm used to explore all
nodes in a graph by going as deep as possible along one branch before backtracking. It's a
powerful tool for solving various problems in graph and trees due to its systematic approach
to exploring a graph's structure.

The key behavior of DFS is that it visits a node, then recursively (or iteratively) visits
its unvisited neighbors, one by one, until all reachable nodes from that starting node have
been visited.
"""
from collections import deque

def dfs_traversal(graph, start_node):
    traversal = []
    visited = {start_node} # Mark start_node as visited
    mydeque = deque([start_node])

    while mydeque:
        current_node = mydeque.pop()
        # Add node into traversal when it is popped out from deque
        traversal.append(current_node)
        # Reverse order ensures the leftmost neighbor is processed first in DFS
        neighbors = sorted(graph.get(current_node, []), reverse=True)
        for neighbor, _ in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                mydeque.append(neighbor)
    return traversal

def dfs_traversal_recursive(graph):
    pass

def dfs_path(graph, start_node, target_node):
    path = []
    visited = {start_node} # Mark start_node as visited
    mydeque = deque([start_node])

    while mydeque:
        current_node = mydeque.pop()
        path.append(current_node)

        if target_node == current_node: # path is found
            return path
        # Reverse order ensures the leftmost neighbor is processed first in DFS
        neighbors = sorted(graph.get(current_node, []), reverse=True)
        for neighbor, _ in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                mydeque.append(neighbor)
                
    return f"There is no path from {start_node} to {target_node}."

#--------------------------------------------------------------------
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

# print(dfs_traversal(graph=network, start_node='A'))
print(dfs_path(graph=network, start_node='A', target_node='I'))