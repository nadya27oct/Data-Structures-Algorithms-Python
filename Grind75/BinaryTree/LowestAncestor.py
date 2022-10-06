"""
Given two nodes, find the lowest common ancestor between the two nodes in a Binary Search Tree.
A node can be an ancestor of itself.
Lowest common ancestor is last ancestor node that is common for both. Not minimum ancestor node value.
               6
             /   \
            2      8
          /  \    /  \
         0    4  7    9
            /  \
           3    5
Common Ancestors for nodes 5 and 0: 2 and 6. Then LCA = 2

Start at root as root is the common ancestor of every single node.
p=2, p<6. So p is left subtree. q=8, q >6. So q is right subtree.
So lowest ancestor common for both p and q is root node 6.

If p = 7 and q = 9, p > 6 and q > 6, so go to left subtree.
Now root node = 8. Since p < 8 and q > 8, then LCA =  8.

If p=6 and q=0, then root = p and root > q. Here root is LCA.

If p=9 and q=4, p > 6 and q < 6, so LCA = root.

What is the lowest common ancestor given a tree with a node and 2 children (left and right)?
Start with one node - a. If we can find 2 and 8 in tree with node 6, then 6 is lowest common ancestor.
        6               6               6
      /   \               \            /
     2     8               8          2

All 3 scenarios above will give LCA = 6.
"""

class Node:
    def __init__(self,val=0):
        self.val = val
        self.left = None
        self.right = None

    def lowestCommonAncestor(self,root,p,q):

        cur = root
        while cur != None:
            if p.val>cur.val and q.val>cur.val: # right subtree
                cur = cur.right

            if p.val<cur.val and q.val<cur.val: # left subtree
                cur = cur.left

            if (p.val<cur.val and q.val>cur.val) or (p.val>cur.val and q.val<cur.val):
                return cur

            if cur.val == p.val or cur.val == q.val:
                return cur

# Time complexity: O(log n) which is the height of tree. If BST is unbalanced, then O(n)
# Space complexity: O(1)

    def recursiveLCA(self,root,p,q):

        if root == None:
            return None

        elif p.val < root.val and q.val < root.val:
            return self.recursiveLCA(root.left)

        elif p.val > root.val and q.val > root.val:
            return self.recursiveLCA(root.right)

        else:
            return root


a = Node(6)
b = Node(2)
c = Node(8)
d = Node(0)
e = Node(4)
f = Node(3)
g = Node(5)
h = Node(7)
i = Node(9)



a.left = b
a.right = c
b.left = d
b.right = e
e.left = f
e.right = g
c.left = h
c.right = i

p=Node(2)
q=Node(6)

tree = Node()
tree.lowestCommonAncestor(a,p,q)
tree.recursiveLCA(a,p,q)

p=Node(0)
q=Node(5)
tree.lowestCommonAncestor(a,p,q)
tree.recursiveLCA(a,p,q)

p=Node(9)
q=Node(3)
tree.lowestCommonAncestor(a,p,q)
tree.recursiveLCA(a,p,q)
