"""
Returning shortest path from start node to every node.
There is an awesome explanation of this algorithm on Computerphile so 
go and search on YT `Computerphile Dijkstra Algorithm`.
"""
from queue import PriorityQueue

def paths(graph, start_node):
    # Initialize distances with path
    node_distance = {node : [float('inf'), []] for node in graph}
    node_distance[start_node][0] = 0
    node_distance[start_node][1] = [start_node] # path starts with start_node

    myqueue = PriorityQueue()
    myqueue.put((0, start_node))

    while not myqueue.empty():
        (current_dist, current_node) = myqueue.get()

        if(current_dist > node_distance[current_node][0]):
            continue

        for neighbor, edge_weight in graph[current_node]:
            new_dist = node_distance[current_node][0] + edge_weight

            if new_dist < node_distance[neighbor][0]:
                node_distance[neighbor][0] = new_dist
                # create the new path for neighbor by copying the current_node's path
                node_distance[neighbor][1] = node_distance[current_node][1].copy()
                # append neighbor
                node_distance[neighbor][1].append(neighbor)
                myqueue.put((new_dist, neighbor))

    return node_distance
# --------------------------------------------------------------------------------
# implementation of above function using `heapq` which is more efficient and simpler
import heapq

def paths_second(graph, start_node):
    # Initialize distances with path
    node_distance = {node : [float('inf'), []] for node in graph}
    node_distance[start_node][0] = 0
    node_distance[start_node][1] = [start_node] # path starts with start_node

    # Intialize the heap (min-heap)
    heap = []
    heapq.heappush(heap, (0, start_node))

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        if(current_dist > node_distance[current_node][0]):
            continue

        for neighbor, edge_weight in graph[current_node]:
            new_dist = node_distance[current_node][0] + edge_weight

            if new_dist < node_distance[neighbor][0]:
                node_distance[neighbor][0] = new_dist
                # create the new path for neighbor by copying the current_node's path
                node_distance[neighbor][1] = node_distance[current_node][1].copy()
                # append neighbor
                node_distance[neighbor][1].append(neighbor)
                # push neighbor and its distance into the heap
                heapq.heappush(heap, (new_dist, neighbor))

    return node_distance
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
if __name__ == "__main__": # so that I can use above defined function in other files as well when needed.
    G = {
        0 : [(1, 1), (2, 2)],
        1 : [(3, 1), (2, 3), (5, 4)],
        2 : [(5, 2)],
        3 : [(4, 7), (6, 9)],
        4 : [(7, 8), (5, 5), (6, 2)],
        5 : [(6, 4)],
        6 : [(7, 10)],
        7 : []
    }

    H = {
        0 : [(1, 1), (2, 2)],
        1 : [(0, 1), (2, 5), (3, 7)],
        2 : [(0, 2), (1, 5), (3, 3), (5, 4)],
        3 : [(6, 4), (4, 5), (1, 7), (2, 3)],
        4 : [(7, 3), (5, 1), (3, 5)],
        5 : [(4, 1), (6, 2), (2, 4)],
        6 : [(7, 9), (5, 2), (3, 4)],
        7 : [(4, 3), (6, 9)]
    }

    result = paths_second(G, "Dublin")
    for key, value in result.items():
        print(f"For node {key} : Distance = {value[0]}, path = {value[1]}")