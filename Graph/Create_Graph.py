# graph is non linear data structure in which nodes are connected to each other through the edges.
# They can be represented in 3 ways - edge list, adjacency list and adjacency matrix.

class Graph:
    def __init__(self):
        self.num_of_nodes = 0
        self.adjacency_list = {}

    def insert_node(self, data):
        if data not in self.adjacency_list:
            self.adjacency_list[data] = []
            self.num_of_nodes += 1
            return self

    def insert_edge(self, vertex1, vertex2):
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return self
        return "The edge is already existed."

    def show_connection(self):
        for node in self.adjacency_list:
            print(f'{node} -----> {" ".join(map(str, self.adjacency_list[node]))}')

my_graph = Graph()
my_graph.insert_node(1)
my_graph.insert_node(2)
my_graph.insert_node(3)
my_graph.insert_edge(2, 3)
my_graph.insert_edge(1, 3)
my_graph.insert_edge(3, 2)
my_graph.show_connection()



