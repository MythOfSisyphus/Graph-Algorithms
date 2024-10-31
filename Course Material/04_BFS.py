"""
Breadth-First - Graph Traversal
Breadth-First traverses the graph systematically, level by level, forming a BFS tree along the way.

Just by using the queue which is based on the principal of FIFO.
And when we do it, it really gives us bfs traversal of the graph.
"""
from queue import Queue

def bfs_traversal(start_node, graph):
    visited = {start_node}
    myqueue = Queue()
    myqueue.put(start_node)

    while not myqueue.empty():
        current_node = myqueue.get()
        print(current_node, end=" ")

        for next_node in graph[current_node]:
            if next_node not in visited:
                myqueue.put(next_node)
                visited.add(next_node)

"""
BFS Traversal can be used to find the path from start_node to target_node.
We can't just keep adding the node in result to find the path as we did in DFS,
it is because BDF is level-by-level traversal whereas when we traverse along DFS
it actually forms a path while traversing. So here we have to mantain the node and
its parent dict. And path found flag to know whether we have target_node in graph
or not.
"""
def bfs(graph, start_node, target_node):
    # set of visited nodes to prevent loops
    # add the start_node to the myqueue and visited
    visited = {start_node}
    myqueue = Queue()
    myqueue.put(start_node)

    # start node has not parent
    # because we want to find path from start -> target
    parent = {start_node : None}

    # path_found flag,
    path_found = False

    while not myqueue.empty():
        current_node = myqueue.get()
        if current_node == target_node:
            path_found = True
            break # stopping the loop when our target node is found.
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                myqueue.put(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current_node
    # path construction
    path = []
    if path_found:
        path.append(target_node)
        while parent[target_node] is not None:
            path.append(parent[target_node])
            target_node = parent[target_node]
    return path[::-1] # reversing the path

#------------------------------------------------------------------------------
graph = {
        0: {1, 3, 4}, 
        1: {0, 2}, 
        2: {0, 1, 3, 5}, 
        3: {0, 2, 4, 5},
        4: {0, 3, 5}, 
        5: {2, 3, 4}
    }

bfs_traversal(0, graph)

route = bfs(graph, 0, 5)
print(route)

