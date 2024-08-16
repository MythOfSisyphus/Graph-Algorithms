'''
Depth-First Search Algorithm

Now I'm gonna try myself to write a code for DFS but I don't know
what should I use to Implement Graph I mean whether should I use
Adjacency Matrix or List? I'm trying with Adjacency List first let's
see what happens...
'''

class Graph:
    def __init__(self, nodes, directed = True):
        self.nodes = nodes 
        self.directed = directed

        self.adj_list = {i : set() for i in range(self.nodes)} 
    
    def addEdge(self, node1, node2, weight = 1):
        self.adj_list[node1].add((node2, weight))

        if not self.directed:
            self.adj_list[node2].add((node1, weight))

    def display(self):
        for key in self.adj_list:
            print(f"node {key} : {self.adj_list[key]}")

    # It is efficient algorithm for
    def DFS(self, node, visited = None):
        if visited is None:
            visited = set()
        
        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neightbour, _ in self.adj_list[node]:
                self.DFS(neightbour, visited)
    
    """
    dfs can be used for searching node,
    the following code is on stack abuse's website so for explanation go there
    """
    def dfs(self, start, target, path=[], visited=set()):
        visited.add(start)
        path.append(start)

        if start == target:
            return path
        
        for neighbour, _ in self.adj_list[start]:
            if neighbour not in visited:
                result = self.dfs(neighbour, target, path, visited)
                if result is not None:
                    return result
        path.pop()
        return None


# g = Graph(8) # a graph with 7 nodes

# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(0, 3)

# g.addEdge(1, 4)
# g.addEdge(1, 5)

# g.addEdge(3, 6)
# g.addEdge(3, 7)

# g.display()
# g.DFS(0)

h = Graph(5, False)

h.addEdge(0, 1)
h.addEdge(0, 2)
h.addEdge(1, 3)
h.addEdge(2, 3)
h.addEdge(3, 4)

h.display()
print(h.dfs(1, 2))