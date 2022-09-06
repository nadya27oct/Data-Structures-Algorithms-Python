"""
Given the root of a tree, determine whether it is a valid binary search tree.
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
We need to walk through all nodes of the tree to ensure that it is valid BST.
Both the left and right subtrees must also be binary search trees.
  5
1   4
   3  6
Is left subtree a bst? 1<5. Yes and No child nodes after 1.Yes
Is right subtree a bst? 4<5. No. Not a BST.
Run time O(n) as we have to visit each node. Space complexity - O(n) massive stack each time we do recursive call.
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

    list = []
    inorder(root)

    for i in range(1,len(list)):
        if list[i] <= list[i-1]:
            return False
    return True

    def inorder(node):
        nonlocal list
        if node == None:
            return True

        inorder(node.left)
        list.append(node.val)
        inorder(node.right)
