'''Prim's Algorithm
I just want to add my little explanation of this algorithm, but before that watch the
animated gif, then you'll almost understand how this algorithm works.
Because it is for finding Minimum Spanning Tree (MST) so then node we add in our list
can be the neighbor of any of the already existing visited nodes. So in this algo what we
do is we just start with a given node then we visit its neighbors and add them in priority
queue then in the next turn one (weight, node) pair would pop out with minimum weight among
the neighbors of start node and now we visit the neighbors of the current poped node
and add its neighbors and their edge weight then in the next turn we get the node
with minimum weight among the neighbors of start node and previously visited nodes.
And this goes on until we visit all the nodes and priority queue becomes empty.

Now go and understand the code below, I admit the fact that I have only two comments in it
but when you read the code you'll realize that it really doesn't need comments because
names of the variables are totally intuitive.
'''
import heapq

def prims_Algorithm(graph, star_node):
    parent_node = {node : -1 for node in graph}
    in_MST = {node : False for node in graph}

    node_distance = {node : float('inf') for node in graph}
    node_distance[star_node] = 0

    resulting_MST = [star_node]

    myheap = []
    heapq.heappush(myheap, (0, star_node)) # (weight, node) pair

    while myheap:
        current_weight, current_node = heapq.heappop(myheap)
        if in_MST[current_node]: # skip the node if it is already visited
            continue

        in_MST[current_node] = True

        if parent_node[current_node] != -1:
            resulting_MST.append(current_node)

        for neighbor, edge_weight in graph[current_node]:
            if not in_MST[neighbor] and edge_weight < node_distance[neighbor]:
                node_distance[neighbor] = edge_weight
                parent_node[neighbor] = current_node
                heapq.heappush(myheap, (edge_weight, neighbor))

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