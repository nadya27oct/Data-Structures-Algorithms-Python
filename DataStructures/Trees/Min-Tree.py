"""
Find the minimum value of a tree.
            3
           / \
          11   5
         /  \    \
        4    2    8
Recursive: Min(min of left sub tree, min right sub tree, parent node)
Default value for base case = infinity.
min(3,min left=2, min right=5)
left = 11.recursive(11)..no null node.
recursive(4). 4 has null node. return infinity. (4, inf, inf)
recursive(11.right) = recursive(2). 2 has null node on left and right. (2, inf, inf)
now min(11,4,2)
recurisve(5)
recursive(8). 8 has null nodes.(8, inf, inf)
(5, inf, 8)
"""

class Node:

    def __init__(self,val=None):
        self.val = val
        self.left = None
        self.right = None

    def find_min_dfs(self,root):
        smallest = float('inf')
        stack = [root]

        while len(stack) > 0:
            current = stack.pop() # Remove element from top of stack
            if current.val < smallest:
                smallest = current.val

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

        return smallest

    def find_min_bfs(self,root):

        smallest = float('inf')

        queue = [root]

        while queue:
            current = queue.pop(0)
            if current.val < smallest:
                smallest = current.val

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return smallest


    def find_min_recursive_dfs(self,root):

        if root == None:
            return float('inf')
        #print(root.val)
        left = self.find_min_recursive_dfs(root.left)

        right = self.find_min_recursive_dfs(root.right)

        #print(root.val,left,right)
        return min(root.val,left,right)




a = Node(3)
b = Node(11)
c = Node(5)
d = Node(4)
e = Node(2)
f = Node(8)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

tree = Node()
tree.find_min_dfs(a)
tree.find_min_bfs(a)
print(tree.find_min_recursive_dfs(a))
