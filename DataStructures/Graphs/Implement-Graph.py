"""
Graphs are data structures that contain nodes/vertices and edges/lines that connect those nodes.
Edge List - An array that states connections.
Implement an Undirected Unweighted Graph using adjacency list. In Adjacency List - index is a node. Value is the node's neighbors.
Undirected - bidirectional
Unweighted - all edges have unit of 1 or all edges have constant weight.
Graph can be found here - https://visualgo.net/en/graphds
"""

class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacency_list = dict()

    def add_vertex(self,node):
        self.adjacency_list[node] = [] # When we enter a new node, it will not have any connections initially. Adding key to dictionary.
        self.number_of_nodes += 1

    def add_edge(self,node1,node2): # This is an undirected, so both nodes need to be connected with each other.
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)

    def show_connections(self):
        for node in self.adjacency_list:
            print(node,'-->',self.adjacency_list[node])


myGraph = Graph()
myGraph.add_vertex('0')
myGraph.add_vertex('1')
myGraph.add_vertex('2')
myGraph.add_vertex('3')
myGraph.add_vertex('4')
myGraph.add_vertex('5')
myGraph.add_vertex('6')
myGraph.add_edge('3', '1')
myGraph.add_edge('3', '4')
myGraph.add_edge('4', '2')
myGraph.add_edge('4', '5')
myGraph.add_edge('1', '2')
myGraph.add_edge('1', '0')
myGraph.add_edge('0', '2')
myGraph.add_edge('6', '5')
myGraph.show_connections()
# ('1', '-->', ['3', '2', '0'])
# ('0', '-->', ['1', '2'])
# ('3', '-->', ['1', '4'])
# ('2', '-->', ['4', '1', '0'])
# ('5', '-->', ['4', '6'])
# ('4', '-->', ['3', '2', '5'])
# ('6', '-->', ['5'])
