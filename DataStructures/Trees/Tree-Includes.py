"""
Return True or False whether a node exists in Binary Tree.
Example: e
Output: true
            a
           / \
          b   c
         / \    \
        d   e    f
Approach:
Breadth-First: Add child nodes to queue. When a node leaves queue, check if it is target node.
If tree is empty, return False as we cannot find target value in an empty tree.

Depth-First-Recursive: There are 2 base cases.
If node is None, return false.
If node matches target value, return True.

Function is called recursively on each branch which will output a boolean value.
node(d)-->False. node(e)-->True, so node(b) = node(d) or node(e)-->True
node(f)-->False. node(c)-->False, so root = node(a) = node(b) or node(c)-->True
            a
           / \
          b   c
         / \    \
        d   e    f

"""

class Node:

    def __init__(self,val=0):
        self.val = val
        self.left = None
        self.right = None

    def search_node_bfs(self,root,search_val):

        if root==None:
            return False

        queue = [root]

        while queue:
            curr_node = queue.pop(0)

            if curr_node.val == search_val:
                return True
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)

        return False

    def search_node_dfs_recursive(self,root,target):

        if not root:
            return False

        if root.val == target:
            return True

        return self.search_node_dfs_recursive(root.left,target) or self.search_node_dfs_recursive(root.right,target)


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

tree = Node()
tree.search_node_bfs(a,'e')
tree.search_node_bfs(a,'j')
print(tree.search_node_dfs_recursive(a,'e'))
print(tree.search_node_dfs_recursive(a,'j'))
