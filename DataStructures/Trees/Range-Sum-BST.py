"""
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
            10
          /    \
         8      15
        / \       \
       7   9       18
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
"""

class Node:
    def ___init__(self,val=0):
        self.val = val
        self.left = None
        self.right = None
class Node:
    def __init__(self,val=0):
        self.val = val
        self.left = None
        self.right = None

    def rangeSumBST(self,root,low,high,rangeSum=0):

        if root == None:
            return 0

        if root.val >= low and root.val <= high:
            rangeSum = root.val

        left = self.rangeSumBST(root.left,low,high)
        right = self.rangeSumBST(root.right,low,high)

        return left + right + rangeSum

a=Node(10)
b=Node(5)
c=Node(15)
d=Node(3)
e=Node(7)
f=Node(18)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

tree = Node()
print(tree.rangeSumBST(a,7,15))
print(tree.rangeSumBST(a,11,18))
