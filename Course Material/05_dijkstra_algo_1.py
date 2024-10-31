r"""
Dijkstra Algorithm - Theory and Intuition
There is awesome explanation of this algorithm on Computerphile.
So go and search on YT `Computerphile Dijkstra Algorithm`.

In this implementation of DA what we're doing is "we try to find shortest path
for all nodes from any given nodes in a graph, so to do this we keep track of
every node's predecessor."
start_node----------current_node---------random node in graph.

Initially we set the distance of getting to node from start_node as infinity.
Then as we iterate through out priority queue we keep updating it distance and
predecessor when we find the shorter distance than we already have stored.

Consider this graph with adjacency list.
   1-----3          0 : [(1, 1), (2, 2)]
  /|\    |          1 : [(0, 1), (2, 3), (3, 2), (4, 5)]
 / | \   |          2 : [(0, 2), (4, 3), (1, 3)]
0  |  \  |          3 : [(1, 2), (4, 4)]
 \ |   \ |          4 : [(3, 4), (2, 3), (1, 5)]
  \|    \|        
   2-----4

let's try to find shortest path for every node from 0. So in out priority queue we first put
(0, 0) then its neighbors 1 and 2 have their intial distances as infinity and new_dist = 1 and 2
respectively, so we have found the distances shorted than already stored so we will update and
put neighbors in queue, 
queue = [(1, 1), (2, 2)] 
node_distance = {0 : 0, 1 : 1, 2 : 2}
so (1, 1) will be popped out next.

Now node 0 has already its minimum possible distance which is zero so won't get updated, now 2 has
new_dist = 1 + 3 = 4 but which is greater than already stored node_distance[2] = 2 so we won't update.
node 3 and 4, new_dist = 1 + 2 = 3 and 1 + 5 = 6 both are < infinity so update it.
queue = [(2, 2), (3, 3), (6, 4)]
node_distance = {0 : 0, 1 : 1, 2 : 2, 3 : 3, 4 : 6}

Now for current_dist, current_node = (2, 2) its neighbor
node 0 has already shortest possible,
for node 4, new_dist = 2 + 3 = 5 < node_distance[4] = 6 so we'll update it
it means that if we go to node 4 via 2 we'll travel shorter distance than we
go to node 4 via 1.
for node 1, new_dist = 2 + 3 = 5 > 1 so no changes.
queue = [(3, 3), (5, 4) (6, 4)]
node_distance = {0 : 0, 1 : 1, 2 : 2, 3 : 3, 4 : 5}

Now for (3, 3)
for node 1 no changes, for node 4 new_dist = 3 + 4 = 7 > 5 so no changes.

queue = [(5, 4), (6, 4)]
node_distance = {0 : 0, 1 : 1, 2 : 2, 3 : 3, 4 : 5}

Now for (5, 4)
for node 3, new_dist = 5 + 4 = 9 > 3 so no changes,
for node 2, new_dist = 5 + 3 = 8 > 2 so again no changes,
for node 1, new_dist = 5 + 5 = 10 > 1 so again no changes.

queue = [(6, 4)]
node_distance = {0 : 0, 1 : 1, 2 : 2, 3 : 3, 4 : 5}

Now for current_dist, current_node = (6, 4)
same as we did for (5, 4) but this time we will not have to
do all calculation because the condition 
current_dist > node_distance[current_node] will handle it
as 6 > 5 so it won't be contributing it making distances shorter
for its neighbors.

This is the explanation of the below code and predecessor is also
not tough to get, predecessor is just a node which provided us
shortest distance from start_node. And it keeps changing as we
find new shorter distances.
"""

from queue import PriorityQueue

def dijkstra_with_predecessor(graph, start_node):
    # Initialize distances with predecessor
    node_distance = {node : float('inf') for node in graph}
    node_distance[start_node] = 0
    node_predecessor = {node : -1 for node in graph} # predecessor of every node = -1

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
