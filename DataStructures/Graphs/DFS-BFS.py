"""
Implement DFS and BFS algorithm for Graphs.
a->b->d->f
|
c->e
 DFS: Use a stack and start with source node. While stack is not empty,  current node = stack.pop() and add neighbors of that node.
 Process each node when they leave stack.
 Iterate through each neighbor.
 BFS: Initialize queue with source node. While queue is not empty, remove from front of queue.
 queue = ['a'], pop queue. visited = ['a']
 Add neighbors of 'a' to queue = ['c','b']. Remove 1st element from queue. visited = ['a','c']
 Add neighbors of 'c' to queue = ['b','e']. Remove 1st element from queue. visited = ['a','c','b']
 Add neighbors of 'b' to queue = ['e','d']. Remove 1st element from queue. visited = ['a','c','b','e']
 Add neighbors of 'e' to queue but 'e' has no children. Current queue = ['d']. Remove 1st element from queue.
 visited = ['a','c','b','e','d']
 Add neighbors of 'd' to queue = ['f']. Remove 1st element from queue.  visited = ['a','c','b','e','d','f']
"""

def depthFirst(graph,source):

    stack = [source]

    while len(stack)!=0:
        current = stack.pop()
        print(current)

        for neighbor in graph[current]:
            stack.append(neighbor)

def depthFirstRecursive(graph,source):

    print(source)
    for neighbor in graph[source]:
        depthFirstRecursive(graph,neighbor)

def breadthFirst(graph,source):

    queue = [source]
    while len(queue)>0:
        current = queue.pop(0)
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)

graph = {
  'a': ['c', 'b'],
  'b': ['d'],
  'c': ['e'],
  'd': ['f'],
  'e': [],
  'f': []
}

depthFirst(graph,'a') #a,b,d,f,c,e
depthFirstRecursive(graph,'a') #a,c,e,b,d,f
breadthFirst(graph,'a') # a,c,b,e,d,f
