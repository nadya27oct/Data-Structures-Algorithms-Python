"""
Write a function, connected_components_count, that takes in the adjacency list of an undirected graph.
The function should return the number of connected components within the graph.
"""

def connected_components_count(graph):

    count = 0
    visited = set()

    for node in graph:
        if explore_nodes(graph,node,visited) == True:
            count +=1
    return count

def explore_nodes(graph,node,visited):

    if node in visited:
        return False

    visited.add(node)

    for neighbor in graph[node]:
        explore_nodes(graph,neighbor,visited)

    return True

connected_components_count({0: [8, 1, 5],1: [0], 5: [0, 8], 8: [0, 5], 2: [3, 4], 3: [2, 4], 4: [3, 2]}) # 2
connected_components_count({ 3: [], 4: [6], 6: [4, 5, 7, 8], 8: [6], 7: [6], 5: [6], 1: [2], 2: [1] }) # 3

"""
Write a function, largest_component, that takes in the adjacency list of an undirected graph.
The function should return the size of the largest connected component in the graph.

Iterative code to travel/hop different components. Then a DFS to find the # of nodes in an island/component.
Time complexity = O(e) where e=number of edges
Space complexity = O(n) as we save all nodes in a visited set.
"""

def largest_component(graph):

    largest = 0
    visited = set()
    for node in graph:
        largest = max(count_nodes(graph,node,visited),largest)

    return largest

def count_nodes(graph,node,visited):

    if node in visited: # If this condition is not true, then its a new node so we can set count = 1 and add to visited.
        return 0

    visited.add(node)
    count = 1

    for neighbor in graph[node]:
        count += count_nodes(graph,neighbor,visited)

    return count

test_0 = largest_component({ 0: [8, 1, 5], 1: [0], 5: [0, 8], 8: [0, 5], 2: [3, 4], 3: [2, 4], 4: [3, 2]}) # -> 4
test_1 = largest_component({1: [2], 2: [1,8], 6: [7], 9: [8], 7: [6, 8], 8: [9, 7, 2]}) # -> 6

# count_nodes(graph,node=1); count = 1; neighbor[1]=[2]
# count_nodes(graph,node=2); count = 2; neighbor[2]=[1,8]
# count_nodes(graph,node=1); 0; count = 2
# count_nodes(graph,node=8); count =3; neighbor[8] = [9,7,2]
# count_nodes(graph,node=9); count = 4; neighbor[8] -> 0; count = 4
# count_nodes(graph,node=7); count = 5; neighbor[7] = [6,8]
# count_nodes(graph,node=6); count = 6; neighbor[6] = 7 -> 0; count = 6
# count_nodes(graph,node=2) --> 0; count = 7
