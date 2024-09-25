"""
Breadth-First Search Algorithm:
Breadth-First Search (BFS) traverses the graph systematically, level by level, forming a BFS tree along the way.

Implementation - Target Node Search
"""
from queue import Queue

graph = {0: {1, 3, 4}, 1: {0, 2}, 2: {0, 1, 3, 5}, 3: {0, 2, 4, 5},
         4: {0, 3, 5}, 5: {2, 3, 4}}

def bfs(graph, start_node, target_node):
    # set of visited nodes to prevent loops
    visited = set()
    myqueue = Queue()

    # add the start_node to the myqueue and visited
    myqueue.put(start_node)
    visited.add(start_node)

    # start node has not parent
    # because we want to find path from start -> target
    parent = dict()
    parent[start_node] = None

    # path_found has its own significance
    path_found = False

    while not myqueue.empty():
        current_node = myqueue.get()
        if current_node == target_node:
            path_found = True
            break # stopping the loop when our target node found.

        for next in graph[current_node]:
            if next not in visited:
                myqueue.put(next)
                parent[next] = current_node
                visited.add(next)

    # path construction
    path = []
    if path_found:
        path.append(target_node)
        while parent[target_node] is not None:
            path.append(parent[target_node])
            target_node = parent[target_node]
        path.reverse()
    return path

#--------------------------------------------------
route = bfs(graph, 0, 5)
print(route)

"""
Breadth-First Implementation - Graph Traversal
Breadth-First Traversal is a special case of Breadth-First Search that traverses
the whole graph, instead of searching for a target node. 
"""
def bfs_traversal(start_node, graph):
    myqueue = Queue()
    visited = set()

    myqueue.put(start_node)
    visited.add(start_node)

    while not myqueue.empty():
        current_node = myqueue.get()
        print(current_node, end=" ")
        for next_node in graph[current_node]:
            if next_node not in visited:
                myqueue.put(next_node)
                visited.add(next_node)

#----------------------------------------------------------------
bfs_traversal(0, graph)
# g = Graph(12)

# g.addEdge(0, 1)
# g.addEdge(0, 2)

# g.addEdge(1, 3)
# g.addEdge(1, 4)
# g.addEdge(1, 5)

# g.addEdge(2, 6)
# g.addEdge(2, 7)

# g.addEdge(4, 8)

# g.addEdge(6, 9)
# g.addEdge(6, 10)

# g.addEdge(7, 11)

# h = Graph(7)

# h.addEdge(0, 1)
# h.addEdge(0, 2)
# h.addEdge(1, 3)
# h.addEdge(1, 4)
# h.addEdge(2, 5)

# h.display()

# h.addEdge(0, 7)

# h.display()