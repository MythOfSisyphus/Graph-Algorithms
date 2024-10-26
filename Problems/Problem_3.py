"""Connected Components
Problem was to find the number of connected components in a graph. So, I thought it would be helpful
if I have a function which takes given graph and a node then tell me all nodes which are in the
component corresponding/involving that node.
Then I used DFS-like approach to solve this problem.
Below is a simple implementation of the appraoch and easy to understand.
"""
from collections import deque
def get_components(graph, node):
    resulting_components = []
    myqueue = deque([node])
    visited = {node}

    while not myqueue.empty():
        current_node = myqueue.popleft()
        resulting_components.append(current_node) # store node when it is popped out from queue

        neighbors = graph.get(current_node, [])
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                myqueue.append(neighbor)

    return resulting_components # all nodes in component

"""
Now we can easily get the number of components with the help of above function.
Idea if to make a list of all present nodes in a graph, then get all nodes in
corresponding components of first element of the list which can be done using above
function now we remove all these nodes from the list then apply the same process for
remaining nodes untill the list becomes empty.
"""
def number_of_components(graph):
    nodes = set(graph.keys()) # set of nodes
    component_count = 0 # to keep track of number of components
    
    while nodes:
        node = next(iter(nodes)) # get arbitrary node from the set
        component = get_components(graph, node)

        nodes -= set(component) # removes all nodes which are in this component
        component_count += 1

    return component_count

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

print(get_components(H, 'G'))
print(number_of_components(H))