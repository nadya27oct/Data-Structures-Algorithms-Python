"""
110 - Balanced Binary Tree.
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Approach 1: Bottom up recursive where leaf node is checked and bubbled upwards.
A tree with an empty node will be a balance tree. Reture True.
Then is left sub tree balanced and right sub tree is balanced. Compute depth at each root node.
Max(Left,right) + 1 is the depth at root node.
        3
      /   \
    9      20
          /  \
         15   7

Approach 2: At each node, we check the depth of left and right subtrees.
"""

class Node:
    def __init__(self,val=0):
        self.val = val
        self.right = None
        self.left = None

    def isTreeBalanced(self,root):

        return self.Depth(root)[0]

    def Depth(self,root):

        if root==None:
            return [True,0]

        left = self.Depth(root.left)
        right = self.Depth(root.right)

        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

        return [balanced,max(left[1],right[1])+1]

    def CheckBalanced(self,root):

        if root == None:
            return True

        leftDepth = self.CheckDepth(root.left)
        rightDepth = self.CheckDepth(root.right)

        if (leftDepth - rightDepth) > 1:
            return False

        return self.CheckBalanced(root.left) and self.CheckBalanced(root.right)

    def CheckDepth(self,root):

        if root == None:
            return 0

        return 1 + max(self.CheckDepth(root.left),self.CheckDepth(root.right))


a = Node(3)
b = Node(9)
c = Node(20)
d = Node(15)
e = Node(7)

a.left = b
a.right = c
c.left = d
c.right = e

tree = Node()
#print(tree.isTreeBalanced(a))
print(tree.CheckBalanced(a))

a = Node(1)
b = Node(2)
c = Node(2)
d = Node(3)
e = Node(3)
f = Node(4)
g = Node(4)

a.left = b
a.right = c
b.left = d
b.right = e
d.left = f
d.right = g

tree = Node()
#print(tree.isTreeBalanced(a))
#print(tree.CheckBalanced(a))
