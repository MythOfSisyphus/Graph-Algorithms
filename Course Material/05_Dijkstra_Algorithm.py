"""Dijkstra Algorithm - Theory and Intuition"""

from queue import PriorityQueue

def dijkstra_with_predecessor(graph, start_node):
    # Initialize distances with predecessor
    node_distance = {node : float('inf') for node in graph}
    node_distance[start_node] = 0
    node_predecessor = {node : -1 for node in graph} # precurrsor of every node = -1

    # Initialize priority queue with the start node
    myqueue = PriorityQueue() # (distane, node) tuple
    myqueue.put((0, start_node))

    # Process the priority queue
    while not myqueue.empty():
        (current_dist, current_node) = myqueue.get()

        # skip processing if we already have better distance
        if(current_dist > node_distance[current_node]):
            continue
        
        # explore the neighbors of current node
        for neighbor, edge_weight in graph[current_node]:
            new_dist = current_dist + edge_weight

            # if the shorter path is found, update distance and predecessor
            if(new_dist < node_distance[neighbor]):
                node_distance[neighbor] = new_dist
                node_predecessor[neighbor] = current_node
                myqueue.put((new_dist, neighbor))

    return node_predecessor
#--------------------------------------------------------------

def path_reconstruction(graph, start_node, target_node):
    path = [] # path to be returned
    predecessor_list = dijkstra_with_predecessor(graph, start_node)

    # check if node is reachable
    if predecessor_list[target_node] == -1 and target_node != start_node:
        return "No path exists from {} to {}.".format(start_node, target_node)

    # Backtrack from target_node to start_nod using predecessor_list
    while target_node != -1:
        path.append(target_node)
        target_node = predecessor_list[target_node]

    path.reverse() # reverse the path to get the correct order
    return path

#--------------------------------------------------------------
graph = {
    1: [(2, 3), (5, 2), (7, 1)],  # Changed to lists
    2: [(3, 4), (4, 7)],
    5: [(4, 6), (6, 3)],
    7: [(6, 1)],
    4: [(3, 5)],
    3: [],  # Ensure all nodes are present in the graph
    6: []
}

result = dijkstra_with_predecessor(graph, 1)
print(result)

resulatant_path = path_reconstruction(graph, 1, 4)
print(resulatant_path)

# for node in graph[0]:
#     print(node)