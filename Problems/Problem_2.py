"""Topological Sorting (https://en.wikipedia.org/wiki/Topological_sorting)
So Topological Sorting is done in Directed Acyclic Graph (DAG) and in it node1
is written before node2 if we have node1 -> node2 (directed edge) and we do this
for every pair of nodes in the whole graph.

Here is the code for TS based on Kahn's Algorithm (https://sci-hub.se/10.1145/368996.369025)
He really gave us nice example by saying 'A is dependent on B' if we have A -> B. So it'd be
really helpful to first count the number of dependenies for each node in a graph i.e. how
many edges are directed to each node.

Now after counting the dependencies for each node, we can store the nodes with zero dependencies,
and which can be written directly into topological order. And now we see the iterate through
graph[node] for each node with 0 dependencies. And we also reduce the dependencies of neighbors of
this node by 1 because here what we're basically doing is in each iteration we're reducing the
dependencies of neighbors of node. So if after reducing the dependency, neithbor has zero than add
it to the queue, so that we can free the nodes who are dependent on this node.
And this process goes on until the queue becomes empty.
"""
from collections import deque

def Topological_Sort_Kahn(graph):
    in_degree = {node : 0 for node in graph} # To store dependencies
    # Counting the dependencies for each node
    for node in graph:
        for neighbor, _ in graph[node]:
            in_degree[neighbor] += 1
    # deque with nodes who have zero dependencies
    myqueue = deque([node for node in graph if in_degree[node] == 0])
    topological_order = []

    while myqueue:
        current_node = myqueue.popleft()
        # Add node into topological_order only when it is popped out from the queue,
        # Because node is popped out from the queue only when it has 0 dependencies.
        topological_order.append(current_node)

        neighbors = graph.get(current_node, [])
        for neighbor, _ in neighbors: # Freeing hostages of current_node
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                myqueue.append(neighbor)

    if len(topological_order) == len(in_degree):
        return topological_order
    else:
        return "Graph has a cycle."