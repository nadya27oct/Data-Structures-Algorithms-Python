"""
Implement Breadth First Search for tree traversal.
We visit children before visiting grand-children. 9->4->20->1->6->15->170.
Here is the tree.
        9
  4           20
1   6      15    170
To implement, we save the final search output in a variable list.
Start with adding current node value to queue.
Append elements to list from queue: current node will go in first. Remove elements from queue based on FIFO basis.
BFS = [9, 4, 20, 1, 6, 15, 170]
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def breadth_first_search(self):
        current_node = self.root
        list = [] #array that will insert items in order of BFS.
        queue = [] #to keep track of level we are at so we can access children as we go through each level

        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)

            list.append(current_node.data)

            if current_node.left != None:
                queue.append(current_node.left)

            if current_node.right != None:
                queue.append(current_node.right)

        return list

    def recursive_breadth_first_search(self,queue,list):

        #base case => queue.length = 0.
        if len(queue) == 0:
            return list

        current_node = queue.pop(0)  #grab current node
        list.append(current_node.data)
        if current_node.left != None:
            queue.append(current_node.left)

        if current_node.right != None:
            queue.append(current_node.right)

        print(list)
        return self.recursive_breadth_first_search(queue,list)


    def insert(self,value):
        if self.root == None:
            self.root = Node(value)

            print("inserted root",self.root.data)
            return

        else:
            new_node = Node(value)
            current_node = self.root

            while (current_node.left != new_node) and (current_node.right != new_node):
                if value < current_node.data:
                    if current_node.left == None:
                        current_node.left = new_node
                        print("left node",current_node.left.data)
                    else:
                        current_node = current_node.left

                else:
                    if current_node.right == None:
                        current_node.right = new_node
                        print("right node",current_node.right.data)

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
tree.breadth_first_search()
tree.recursive_breadth_first_search([tree.root],[])
