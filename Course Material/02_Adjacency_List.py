"""
Here I'm just gonna implement Adjacency List for different types of graphs. 
If you don't know about Adjacency List then please check out this link
https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/representing-graphs-in-code/#adjacencylist
"""

# let's name our class 'Mystery'
class Mystery:
    def __init__(self, nodes, directed = True):
        self.nodes = nodes # number of nodes
        self.directed = directed # whether graph is directed or not

        # list for adjacency list
        # dict for storing node-node connection
        self.adj_list = {i: set() for i in range(self.nodes)}


    def add_edge(self, node1, node2, weight = 1):
        self.adj_list[node1].add((node2, weight))

        if not self.directed:
            self.adj_list[node2].add((node1, weight))
    
    # kind of self contained way to represent a graph
    def show_list(self):
        result = [0 for node in range(self.nodes)] # to return

        for node in self.adj_list:
            if len(self.adj_list[node]) != 0:
                result[node] = len(result)
                for i,_ in self.adj_list[node]:
                    result.append(i)
        return result

    def display(self):
        for key in self.adj_list:
            print(f"node {key} : {self.adj_list[key]}")

# Driver code
graph = Mystery(6)

graph.add_edge(0, 1)
graph.add_edge(0, 3)
graph.add_edge(1, 2)

graph.add_edge(2, 3)
graph.add_edge(3, 1)

graph.display()
# print(graph.show_list())

graph.add_edge(0, 4)
graph.add_edge(2, 5)

print(graph.show_list())