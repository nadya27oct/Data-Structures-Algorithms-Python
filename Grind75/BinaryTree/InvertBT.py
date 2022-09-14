"""
Given the root of a binary tree, invert the tree, and return its root.

Tree:
            4
        2       7
      1   3    6  9

Inverted Tree:
            4
        7       2
     9    6   3    1
"""

class Solution:

    def invertTree(self,root):
#If root is null, return null.
        if not root:
            return
#swap the children
        temp = root.right
        root.right = root.left
        root.left = temp
#invert subtree, left and right.
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# Time complexity: O(n) - every node needs to be visited once.
# Space complexity: O(h) due to recursive calls - where h is height of tree.

#Iterative Approach
# Breadth First Traversal where we go through each parent node.
# Put each child node in a given level in queue then we can access each FIFO basis.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class IterativeSolution:
    def invert_Iteratively(self,root):

        if root == None:
            return root

        queue = []
        queue.append(root)
#Iterate through nodes in queue while queue is not null.
        while queue:
            curr_node = queue.pop()
#Then swamp children similar to recursive.
            temp = curr_node.left
            curr_node.left = curr_node.right
            curr_node.right = temp

            if curr_node.left:
                queue.append(curr_node.left)

            if curr_node.right:
                queue.append(curr_node.right)

        return root
