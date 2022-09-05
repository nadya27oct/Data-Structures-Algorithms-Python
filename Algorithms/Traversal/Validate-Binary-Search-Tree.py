"""
Given the root of a tree, determine whether it is a valid binary search tree.
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
  5
1   4
   3  6
Is left subtree a bst? 1<5. Yes and No child nodes after 1.Yes
Is right subtree a bst? 4<5. No. Not a BST.
"""

class Solution:
    def isvalidBST(self,root):

        def valid_BST(node,low,high):
            if node == None:
                return True
            if not (node.val > low and node.val < high):
                return False

            return (valid_BST(node.left,low,node.val)) # Left subtree has to be less than parent or current node value.
                    and (valid_BST(node.right,node.val,high))

        return valid_BST(root,float("-inf"),float("inf"))

"""
Implement an in-order traversal.
First we traverse left sub-tree. Next we visit node. Then we traverse right sub-tree.
In-Order traversal shows final list of elements from binary search tree in ascending order.
If an element is not greater than previous, then it is NOT a bst.
"""

def isvalidBST(self,root):

    def inorder(node,list=[]):
        if node == None:
            return True

        if node.left != None:
            inorder(node.left,list)
        list.append(node.val)

        if list[-1] < list[-2]:
            return False

        if node.right != None:
            inorder(node.right)
