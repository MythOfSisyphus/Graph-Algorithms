r"""Prim's Algorithm
I just want to add my little explanation of this algorithm, but before that watch the
animated gif on Wikipedia, then you'll almost understand how this algorithm works.

Because it is for finding Minimum Spanning Tree (MST) so, node we add in our list can be
the neighbor of any of the already visited nodes. 
(weight, node) pair
So, in this algo what we do is start with a given node then we visit its neighbors and add
them in priority queue then in the next iteration we got the node with minimum edge weight
and we visit its neighbors if it hasn't been visited yet. And while visiting neighbors we
check that whether neighbors has been visited or not, if it hasn't been visited then in this
visit do we have shorter node_distance for that neighbor if yes then we update 
node_distance[neighbor] otherwise jump to next neighbor. This process goes on until the queue
becomes empty.

Example: Here you can set your desired edge weight but for this time let's say edge weights
of (0, 1), (0, 4), (1, 4), (1, 2) and (2, 4) are 1, 2, 3, 4, 2 respectively.
   1-----2-----3
  /|    /|\   /|\
 / |   / | \ / | \
0  |  /  |  \  |  7
 \ | /   | / \ | /
  \|/    |/   \|/
   4-----5-----6
Now we start our MST with node 0, and we put (1, 1) and (2, 4) in our queue so (1, 1) will be popped
up in the next iteration as 1 < 2. And node 1 has edge with nodes 0, 2, 4 but node 0 is already in MST
sp skip that and edge weight of node 4 with node 1 is 3 so again skip that because we have shorter edge
weight already in queue, and add (4, 2).
Now we node 4 will pop out, and node 4 has edge with nodes 0, 1, 2 as nodes 0, 1 are already visited and it
has edge of weight 2 with node 2 so put (2, 2) in queue because we have found shorter edge for node 2. So
this time node 2 will pop out now don't worry that we have (4, 2) in queue so what will happen when it will
get popped. Nothing happened, because when it will be popped, node 2 would have been visited, so by our
condition in_MST loop won't work. As it works for nodes which aren't in MST.
"""
import heapq

def prims_Algorithm(graph, star_node):
    parent_node = {node : -1 for node in graph}
    in_MST = {node : False for node in graph}

    node_distance = {node : float('inf') for node in graph}
    node_distance[star_node] = 0

    resulting_MST = []

    myheap = []
    heapq.heappush(myheap, (0, star_node)) # (weight, node) pair

    while myheap:
        current_weight, current_node = heapq.heappop(myheap)
        if in_MST[current_node]: # skip the node if it is already visited
            continue

        in_MST[current_node] = True # Mark it as visited.

        if parent_node[current_node] != -1:
            resulting_MST.append((parent_node[current_node], current_node, current_weight))

        for neighbor, edge_weight in graph[current_node]:
            # update node_distance and push it into heap iff neighbor is not in MST and shorter distance is found.
            if not in_MST[neighbor] and edge_weight < node_distance[neighbor]:
                node_distance[neighbor] = edge_weight
                parent_node[neighbor] = current_node
                heapq.heappush(myheap, (edge_weight, neighbor))
    # return the MST
    return resulting_MST
#-----------------------------------------------------------------
graph = {
    0 : [(1, 1), (3, 2)],
    1 : [(0, 1), (2, 1), (3, 3), (4, 5), (5, 4)],
    2 : [(1, 1), (5, 5)],
    3 : [(0, 2), (4, 2), (1, 3)],
    4 : [(3, 2), (5, 3), (1, 5)],
    5 : [(2, 5), (1, 4), (4, 3)]
}

graph_2 = {
    0: [(1, 1), (2, 3)],
    1: [(0, 1), (2, 5), (3, 5)],
    2: [(0, 3), (1, 5), (4, 2)],
    3: [(1, 5), (4, 6)],
    4: [(2, 2), (3, 6)]
}

MST = prims_Algorithm(graph_2, 0)
print(MST)