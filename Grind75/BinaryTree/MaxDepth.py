"""
Given the root of a binary tree, return its maximum depth.
Maximum depth of a tree is the number of steps to reach a leaf node from root.
        3
      /  \
     9     20
          /   \
         15     7
"""

class Node:
    def __init__(self,val=0):
        self.val = val
        self.right = None
        self.left = None

a = Node(3)
b = Node(9)
c = Node(20)
d = Node(15)
e = Node(7)

a.left = b
a.right = c
c.left = d
c.right = e


"""
Iterative BFS: In BFS, we count each levels a tree has to get max depth.
Traverse entire level and then add next level. When we traverse a level, we will increase depth of the tree.
node = 3. add children of 3 to q = [9, 20]
queue has 2 elements: node=9. no children to add
                      node=20. q=[15,7]
queue has 2 elements: node=15. no children to add
                      node=7. no children to add
"""

def maxDepth(root):

    if root == None:
        return 0

    queue = [root]
    level = 0

    while len(queue) > 0:

        for i in queue:
            node = queue.pop()
            if node.left != None:
                queue.append(node.left)

            if node.right != None:
                queue.append(node.right)

        level +=1

    return level

maxDepth(a)

"""
Iterative DFS: We will add root node to stack. Depth = 1. Pop stack
Then add right child and left child: stack = [20,9].
"""

def maxDepthDFS(root):

    if root != None:
        stack = [(root,1)]

    depth = 0

    while len(stack) > 0:
        node,current_depth = stack.pop()
        if node != None:
            depth = max(current_depth,depth)
            stack.append((node.left,current_depth+1))
            stack.append((node.right,current_depth+1))
    return depth

maxDepthDFS(a)
