"""
Implement Depth First Search traversal for binary tree.
        9
  4           20
1   6      15    170
In-Order: [1,4,6,9,15,20,170]
Pre-Order: [9,4,1,6,20,15,170] We want to push to list at beginning.
Post-Order: [1,6,4,15,170,20,9]
"""

class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def dfs_InOrder(self):
        return self.traverse_in_order(self.root,[])

    def traverse_in_order(self,node,list): #Initially it checks if root node has a left child. then traverse all the way down.

        print(node.value)
        if node.left != None:
            self.traverse_in_order(node.left,list)
        # Once there is no more node left. We only append after we ensure that we are at the bottom of left nodes.
        list.append(node.value)

        if node.right != None:
            self.traverse_in_order(node.right,list)

        return list

    def dfs_PreOrder(self):
        return self.traverse_pre_order(self.root,[])

    def traverse_pre_order(self,node,list):
        print(node.value)

        list.append(node.value)
        if node.left!= None:
            self.traverse_pre_order(node.left,list)

        if node.right!=None:
            self.traverse_pre_order(node.right,list)

        return list

    def dfs_PostOrder(self):
        return self.traverse_post_order(self.root,[])

    def traverse_post_order(self,node,list):
        print(node.value)

        if node.left != None:
            self.traverse_post_order(node.left,list)

        if node.right != None:
            self.traverse_post_order(node.right,list)

        list.append(node.value)
        return list

    def insert(self,value):
        if self.root == None:
            self.root = Node(value)

            return

        else:
            new_node = Node(value)
            current_node = self.root

            while (current_node.left != new_node) and (current_node.right != new_node):
                if value < current_node.value:
                    if current_node.left == None:
                        current_node.left = new_node
                    else:
                        current_node = current_node.left

                else:
                    if current_node.right == None:
                        current_node.right = new_node
                    else:
                        current_node = current_node.right

            return

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
print(tree.dfs_InOrder())
print(tree.dfs_PreOrder())
print(tree.dfs_PostOrder())
