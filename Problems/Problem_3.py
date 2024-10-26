"""Connected Components
Problem was to find the number of connected components in a graph. So, I thought it would be helpful
if I have a function which takes given graph and a node then tell me all nodes which are in the
component corresponding/involving that node.
Then I used DFS-like approach to solve this problem.
Below is a simple implementation of the appraoch and easy to understand.
"""
from queue import Queue
def corresponding_component_to(graph, node):
    resulting_components = []
    myqueue = Queue()
    myqueue.put(node)
    visited = {node}

    while not myqueue.empty():
        current_node = myqueue.get()
        resulting_components.append(current_node) # store node when it is popped out from queue

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                myqueue.put(neighbor)

    return resulting_components # all nodes in component

"""
Now we can easily get the number of components with the help of above function.
Idea if to make a list of all present nodes in a graph, then get all nodes in
corresponding components of first element of the list which can be done using above
function now we remove all these nodes from the list then apply the same process for
remaining nodes untill the list becomes empty.
"""
def Number_of_Components(graph):
    nodes_given = [node for node in graph] # all nodes
    count = 0 # to keep track of number of components
    while nodes_given:
        current_component = corresponding_component_to(graph, node=nodes_given[0])
        for node in current_component:
            nodes_given.remove(node) # remove all nodes which are in current_component
        count += 1
    return count

#--------------------------------------------------------------------------------------------
G = {
    0 : [1, 2],
    1 : [0, 2],
    2 : [0, 1, 4],
    3 : [5],
    4 : [2],
    5 : [3]
}

H = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D', 'E', 'F'],
    'C' : ['A', 'F'],
    'D' : ['B', 'H'],
    'E' : ['B'],
    'F' : ['B', 'C', 'H'],
    'H' : ['D', 'F'],
    'G' : ['I', 'J'],
    'I' : ['G', 'J'],
    'J' : ['G', 'I', 'K'],
    'K' : ['J', 'L'],
    'L' : ['K']
}

print(corresponding_component_to(H, 'G'))
print(Number_of_Components(H))

# print(corresponding_component_to(G, 1))
# components_in_G = Number_of_Components(G)
# print(components_in_G)