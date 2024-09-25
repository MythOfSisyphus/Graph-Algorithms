"""
BFS: Please first take quick look at the code below then read the explanation.
Even though it is not an actual bfs, it is inspired/modified code from what I found on stack abuse and I wrote
it to understand it.
Explanation:
Suppose we have graph
    1
   / \
  2   3
  |   |
  4   5
       \
        6
And bfs traverse it level by level (1 -> 2, 3 -> 4, 5 -> 6) so to do that,
we're going to use `Queue` and `set()`.
Here we're storing (node, parent) pair in dict, where key -> node and value -> parent.
"""

from queue import Queue

def bfs(graph, start_node):
    myqueue = Queue() # Queue for bfs
    myqueue.put(start_node)

    visited = {start_node} # to track visited nodes

    parent = {start_node : None} # dict to store parent of each node

    while not myqueue.empty():
        current_node = myqueue.get()

        # Use set() if graph is using set for adj list
        for neighbor in graph.get(current_node, set()):
            if neighbor not in visited:
                parent[neighbor] = current_node
                myqueue.put(neighbor)
                visited.add(neighbor)
    
    return parent # dict of (node, parent)


#---------------------------------
graph = {0 : {1, 2, 3},
         1 : {4, 5},
         2 : {6, 7, 8},
         3 : {9, 10, 11}}

result = bfs(graph, 0)
print(result)

def path_construction(result, start_node, target_node):
    path = []
    while target_node is not None:
        path.append(target_node)
        target_node = result[target_node]
    path.reverse()
    return path

print(path_construction(result, 0, 11))