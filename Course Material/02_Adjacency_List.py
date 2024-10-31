"""
Here I'm just gonna implement Adjacency List for different types of graphs. 
If you don't know about Adjacency List then please check out this link
https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/representing-graphs-in-code/#adjacencylist
"""
class Graph:
    def __init__(self, directed=True):
        self.directed = directed
        self.adj_list = {}

    def add_edge(self, node1, node2, weight=1):
        if node1 in self.adj_list:
            self.adj_list[node1].append((node2, weight))
        else:
            self.adj_list[node1] = [(node2, weight)]

        if not self.directed:
            if node2 in self.adj_list:
                self.adj_list[node2].append((node1, weight))
            else:
                self.adj_list[node2] = [(node1, weight)]
    
    def show(self):
        for key, value in self.adj_list.items():
            print(f"{key} : {value}")

#-----------------------------------------------------------------
g = Graph(directed=True)
g.add_edge('A', 'B', 2)
g.add_edge('A', 'C', 3)
g.add_edge('B', 'C', 1)

g.show()