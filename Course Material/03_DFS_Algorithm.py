''' Depth-First Search Algorithm '''

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
    
    # dfs is used to search a node or path in a graph while going along one branch
    def dfs(self, start, target, path=[], visited=set()):
        visited.add(start) # adding start in visited when it is actually visited
        path.append(start) # adding it to the path

        if start == target: # if yes then we've found the path
            return path
        
        for neighbour, _ in self.adj_list[start]:
            if neighbour not in visited: # otherwise we'll be in loop
                result = self.dfs(neighbour, target, path, visited) # going as deep as we can go along one branch
                if result is not None:
                    return result
        path.pop() # when there exist no path
        return None

#----------------------------------------------------------------------------

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