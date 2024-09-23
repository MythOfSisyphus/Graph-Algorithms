"""
Depth-First-Search(DFS): DFS is fundamental graph traversal algorithm used to explore all
nodes in a graph by going as deep as possible along one branch before backtracking. It's a
powerful tool for solving various problems in graph and trees due to its systematic approach
to exploring a graph's structure.

The key behavior of DFS is that it visits a node, then recursively (or iteratively) visits
its unvisited neighbors, one by one, until all reachable nodes from that starting node have
been visited.

Simple and Efficient: DFS is easy to implement and runs in linear time relative to the number
of nodes and edges in the graph. O(n+m)
"""

def dfs(start_index, end_index, graph):
    visited = set() # To track the visited nodes
    stack = [start_index] # start dfs from the start index
    mylist = [] # to store the traversal path

    while stack: # until stack isn't empty
        node = stack.pop() # get the last element in the stack

        if node not in visited:
            visited.add(node)
            mylist.append(node) # add node to the traversal path

            if node == end_index:
                return mylist # return the path if end_index is found
            
            # add unvisited neighbor to the stack
            for neighbor in sorted(graph.get(node, []), reverse=True): # reversed to stimulate the dfs order
                if neighbor not in visited:
                    stack.append(neighbor)

    # returns the full traversal if end_index not found
    return mylist

"""
Now couple of questions come into the mind. Why we're using `sorted(graph.get(node, []), reverse=True)`?
As we know that DFS likes going in the depth along every possible path. So in the graph below 0 has first edge
with 1 so dfs would like to go to fist 0 then 1 then nodes which are connected to 1 i.e. 4 and 5 then nodes
connected to them. And we're using stack.pop() to get the value of `node` when we use pop() method without `reverse=True`
it would give us the element it added most recently in the stack but we want what was added first that's why we're using
`sorted(graph.get(node, []), reverse=True)`.

Why we're not adding `neighbor` in `visited` at the time when we're adding them in `stack`?
It is because `dfs` marks a node `visited` only when the node is actually *visited*. So here we're just
adding node as to-be visited.

Take an graph and go to the code step-by-step, you'll get it.
"""

graph = {0: {1, 2, 3},
           1: {4, 5},
           2: {6, 7},
           3: {8, 9}}

# print(graph.get(10))

# print(dfs(0, 10, graph))