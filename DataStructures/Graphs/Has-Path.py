"""
Return a boolean (True or False) whether a path exists between two nodes.
f->g->h
| /
i<--j
 \
  k
Write a function, has_path, that takes in a dictionary representing the adjacency list of a
directed acyclic graph and two nodes (src, dst). The function should return a boolean
indicating whether or not there exists a directed path between the source and destination nodes.

Convert
e = # of edges
Time complexity = O(e)
Space complexity = O(n)
"""
graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

def has_path(graph,source,destination):

    if source == destination:
        return True

    for neighbor in graph[source]:
        if has_path(graph,neighbor,destination) == True:
            return True
    return False


has_path(graph, 'f', 'k') # True
has_path(graph, 'f', 'j') # True


def BFS_has_path(graph,source,destination):
    queue = [source]

    while queue:
        current = queue.pop(0)
        if current == destination:
            return True

        for neighbor in graph[current]:
            queue.append(neighbor)

    return False

BFS_has_path(graph,'f','k')
BFS_has_path(graph,'f','j')

"""
Undirected Path:
Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B).
The function should return a boolean indicating whether or not there exists a path between node_A and node_B.

Need to avoid cycles in graph. Otherwise, there is maximum recursion.
Pass visited as a function input. If a node has been visited, no need to traverse through the node.
"""

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

def buildGraph(edges):

    graphs = dict()

    for edge in edges:
        (a,b) = edge
        if a in graphs:
            graphs[a].append(b)
        else:
            graphs[a] = [b]
        if b in graphs:
            graphs[b].append(a)
        else:
            graphs[b] = [a]

    return graphs
#graphs ={'i':['j','k'],
#         'j':['i'],
#         'k':['i','m','l'],
#         'm':['k'],
#         'l':['k'],
#         'o':['n'],
#         'n':['o']}

def undirected_path(edges,nodeA, nodeB):

    graph = buildGraph(edges)
    visited = set()

    return hasPath(graph,nodeA,nodeB,visited)

def hasPath(graph,source,destination,visited):

    if source in visited:
        return False

    if source == destination:
        return True
    visited.add(source)

    for neighbor in graph[source]:
        if hasPath(graph,neighbor,destination,visited) == True:
            return True

    return False

print(undirected_path(edges, 'm', 'j')) 
print(undirected_path(edges, 'k', 'o'))
