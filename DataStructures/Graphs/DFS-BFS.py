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
 Add neighbors of 'a' to queue = ['c','b']. Pop queue. visited = ['a','b']
 Add neighbors of 'b' to queue = ['c','d']
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
depthFirstRecursive(graph,'a') #a,b,d,f,c,e
breadthFirst(graph,'a') # a,c,b,e,d,f
