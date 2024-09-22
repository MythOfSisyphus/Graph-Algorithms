class Graph:
    # Constructor
    def __init__(self, num_of_nodes, directed=True):
        self.num_of_nodes = num_of_nodes
        self.directed = directed

        # Adjacency Matrix is a way to represent a graph
        # a zero matrix of order nodes x nodes
        self.adjacency_matrix = [[0 for columns in range(self.num_of_nodes)] 
                                   for rows in range(self.num_of_nodes)]

    # Add edge to a graph
    def add_edge(self, node1, node2, weight = 1):
        self.adjacency_matrix[node1][node2] = weight

        # if the graph is undirected
        if not self.directed:
            self.adjacency_matrix[node2][node1] = weight

    # printing Adjacency Matrix
    def show_adj_matrix(self):
        for row in self.adjacency_matrix:
            for column in row:
                print(column, end=" ")
            print()


# # initializing an empty graph with 5 nodes
# g = Graph(5)

# # graph g with default weight 1
# g.add_edge(0, 1)
# g.add_edge(0, 3)
# g.add_edge(1, 2)
# g.add_edge(1, 4)
# g.add_edge(2, 0)
# g.add_edge(3, 4)
# g.add_edge(4, 2)

# g.show_adj_matrix()

# ------------------------------------
g2 = Graph(5)

g2.add_edge(0, 1, 1)
g2.add_edge(0, 3, 3)
g2.add_edge(0, 2, 2)
g2.add_edge(1, 2, 3)
g2.add_edge(1, 3, 4)
g2.add_edge(2, 4, 6)
g2.add_edge(3, 4, 7)
g2.add_edge(4, 0, 4)
g2.add_edge(4, 1, 5)
g2.add_edge(4, 3, 7)

g2.show_adj_matrix()