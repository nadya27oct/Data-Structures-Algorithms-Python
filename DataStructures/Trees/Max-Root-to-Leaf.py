"""
Find max path sum from root to any leaf path.
        3
      /   \
    11      4
   /  \    /  \
  2    8   10   7
16    22   17    14

We want to end in leaf node. A node with no children. Base case. Leaf node -> returns leaf val
If we input a node with no children, then sum of that leaf node is n.
A tree with only 1 node (value =42), then max path sum = 42.
What happens when we have a leaf with no left or right node?
They should not contribute any value to path sum.
Another base case: when root node is null -> returns 0 (or negative infinity)
Think of base case as their own inputs.
What is the max path sum from each sub tree? bigger of two children contributes to max path.
The decision we make at each node (based on left and right child) should carry on to parent node.
call function on 3
call function on 11
max of 2 and 8 = 8; 8 + 11 = 19
call function on 4
max of 10 and 7 = 10; 4+10 = 14
max of 19 and 14 at 3 = 3 + 19 = 22
"""
class Node:
    def __init__(self,val=0):
        self.val = val
        self.left = None
        self.right = None

    def dfs_max_sum(self,root):

        if root == None:
            return 0
        if root.left == None and root.right == None:
            return root.val

        left = self.dfs_max_sum(root.left)
        right = self.dfs_max_sum(root.right)
        max_child = max(left,right)

        return root.val + max_child

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(2)
e = Node(8)
f = Node(10)
g = Node(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g


tree = Node()
tree.dfs_max_sum(a)
