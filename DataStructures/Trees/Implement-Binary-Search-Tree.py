"""
To implement Binary Search Tree, we first keep track of nodes to right and left of current node through Node class.
In BinarySearchTree class, initialize root node with null value.
When inserting values to BST, check if value < root, then move to left node.
If left node is empty, left = new value.
Else compare value with left node. current parent = new value. Perform above.

Insert:
If tree is empty, then first insert is root node. Root = 9.
Insert 4: If 4 < 9 so go to left. If left is empty. left = 4.
        9
    4
Insert 6: If 6 < 9, Go Left. Left is not empty. Now compare 6 against 4. Is 6 < 4? No. Go right. Right is empty. Right = 6.
            9
    4
        6
Insert 20: If 20 > 9. Go Right. If Right is empty, Right=20.
            9
    4           20
        6
Insert 1: 1 < 9. Go left.Is 1<4? Yes! Go left.Left is empty so Left = 1.
"""
class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        insert_node = Node(value)
        if self.root == None:
            self.root = insert_node
            print('inserted to root',self.root.value)
            return
        else:
            current_node = self.root

            while (current_node.left != insert_node) and (current_node.right != insert_node): #Exit Loop when insert node position has been found.
                if value < current_node.value: # Move to Left tree.
                    if current_node.left == None:
                        current_node.left = insert_node # Left = New Node

                    else:
                        current_node = current_node.left # Compare New Node with Left Parent.

                else: # Move to Right Tree.
                    if current_node.right == None:
                        current_node.right = insert_node
                    else:
                        current_node = current_node.right

            return


    def lookup(self,search_value):
        if self.root == None:
            return("Tree is empty")

        else:
            current_node = self.root
            while current_node != None:
                if search_value == current_node.value:
                    return("Found")
                elif search_value < current_node.value: # Move left
                    current_node = current_node.left
                elif search_value > current_node.value: # Move Right
                    current_node = current_node.right

            return("Not Found")


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
print(tree.lookup(10))
print(tree.lookup(15))
