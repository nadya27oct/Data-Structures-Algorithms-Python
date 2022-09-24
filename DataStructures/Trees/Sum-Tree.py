"""
Return sum of binary tree.
            3
           / \
          11   4
         /  \    \
        4    2    1
DFS Recursive:
Base case - Simplest tree is empty tree. Sum is 0.
Call function recursively on left sub tree and right sub tree to get total sum from each tree.
treeSum(3) = root.val + treeSum(left) + treeSum(right)
                3     + treeSum(left) + treeSum(right)
                3  + 17 + 5 = 25

"""

class Node:
    def __init__(self,val=0):
        self.val = val
        self.right = None
        self.left = None

    def treeSum(self,root):

        if root == None:
            return 0

        left_vals = self.treeSum(root.left)
        right_vals = self.treeSum(root.right)
        return root.val + left_vals + right_vals

    def treeSum_breadth_first(self,root):

        if root == None:
            return 0
            
        sum = 0
        queue = [root]

        while queue:
            current = queue.pop(0)
            sum += current.val

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        return sum


a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

tree = Node()
print(tree.treeSum(a))
print(tree.treeSum_breadth_first(a))
