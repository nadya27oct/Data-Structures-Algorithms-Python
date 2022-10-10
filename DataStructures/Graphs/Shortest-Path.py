"""
Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B).
The function should return the length of the shortest path between A and B.
Consider the length as the number of edges in the path, not the number of nodes.
If there is no path between A and B, then return -1.

y--x--w
|     |
z-----v
BFS - for shortest path
Start at source w and starting node has dist = 0. Visited = (w). Every time a node visits its neighbors, increment dist
and add neighbor to visited.
Queue = (w,0). Queue[0] = current = (w,0). Add neighbors -> queue = [(x,1),(v,1)]; Visited = (w,x,v)
Queue[0] = current = (x,1). Add neighbors of x: [w,y]. Already visited w. So only add v. queue = [(v,1),(y,1)]; Visited = (w,x,v,y)
Queue[0] = current = (v,1). Add neighbors of v: [z,w]. Already visited w. Only add z. Visited = (w,x,v,y,z). queue[(y,1),(z,2)]
Queue[0] = current = (y,1). Add neighbors of y: [x,z]. Already visited x and z. queue[0]=[(z,2)]. Return dist.
"""

def convert_to_adjacency_list(edges):

    graph = dict()
    for edge in edges:
        [a,b] = edge
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)

        if b not in graph:
            graph[b] = [a]
        else:
            graph[b].append(a)

    return graph # {'y': ['x', 'z'], 'x': ['w', 'y'], 'z': ['y', 'v'], 'w': ['x', 'v'], 'v': ['z', 'w']}

def shortest_path(edges,nodeA, nodeB):

    graph = convert_to_adjacency_list(edges)
    dist = 0
    visited = set(nodeA)
    queue = [[nodeA,dist]]

    while queue:
        cur_node,dist = queue.pop(0)
        if cur_node == nodeB:
            return dist

        for neighbor in graph[cur_node]:
            if neighbor not in visited:
                visited.add(cur_node)
                queue.append([neighbor,dist+1])

    return -1

edges = [['w', 'x'],
         ['x', 'y'],
         ['z', 'y'],
         ['z', 'v'],
         ['w', 'v']]

test1=shortest_path(edges, 'w', 'z') # -> 2
test2=shortest_path(edges, 'z','a')
test3=shortest_path(edges, 'x','y')
