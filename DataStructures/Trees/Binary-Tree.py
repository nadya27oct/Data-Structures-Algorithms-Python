"""
 Binary Tree Features
 1. At most 2 children per node
 2. Exactly 1 root or parent node.
 3. There is only 1 path between root and any node.
            a
           / \
          b   c
         / \    \
        d   e    f
Depth First Search
Store 'a' node in stack. Is stack empty? No. Remove a. Current node is a.
When node leaves stack, we visited current node.
Now look at 'a' child nodes b and c. First push c to stack and then b. stack = [c,b].
b is at top of stack.
Is stack empty? No. remove from top of stack: b.
b is now current node. b has 2 child nodes. We push e and d to stack. stack = [c,e,d]
Stack not empty. Remove from top of stack: d
d has no children. Nothing to add to stack. Finish iteration.
Pop e from stack. e has no children. Finish iteration.
Pop c from stack. c is current node. c has 1 child. Push f to stack.
Remove f from stack.
Stack is empty.
Add values to value list when ever a node leaves stack.
Complexity: n # of nodes. Time O(n)
Space: Stack - linear data structure: Space O(n)


Breadth First Search
Add node-a in queue. Is queue empty? No. Remove a. Current node is a. Visited = a
Add children of 'a' to queue. Queue = [b,c]. Finish iteration. Remove b. Current node is b. Visited = [a,b]
Add children of 'b' to queue. Push d then e. Queue = [c,d,e]. Remove c. Current node is c. Visited = [a,b,c]
c only has 1 child. Push f to end of queue = [d,e,f]. next iteration.
Remove d. Current node is d, but d has no children. Visited = [a,b,c,d]
Remove e. e has no children. Visited = [a,b,c,d,e]
Remove f. f has no children. Visited = [a,b,c,d,e,f]
Time complexity = Space = O(n)
Time is O(n) if adding and removing to queue data structure is linear time.
We add all nodes to queue so space is O(n)
"""

class Node:
    def __init__(self,val=0):
        self.val = val
        self.right = None
        self.left = None

    def DepthFirst(self,root):

        if root==None:
            return []

        stack = [root]
        output = []
        while stack:
            current_node = stack.pop()
            output.append(current_node.val)

            if current_node.right:
                stack.append(current_node.right)

            if current_node.left:
                stack.append(current_node.left)

        return output

    def DFSRecursive(self,root):

        if root == None:
            return []

        left_vals = self.DFSRecursive(root.left)   # values =[b,d,e]
        right_vals = self.DFSRecursive(root.right) # values = [c,f]

        return [root.val] + left_vals + right_vals

    def BreadthFirst(self,root):

        if not root:
            return []

        visited = []
        queue = [root]

        while queue:
            curr_node = queue.pop(0)
            visited.append(curr_node.val)
            if curr_node.left:
                queue.append(curr_node.left) #q=['b']
            if curr_node.right:
                queue.append(curr_node.right)#q=['b','c']
        return visited


"""
Recursive call stack:
DFSRecursive(a)
DFSRecursive(b)
DFSRecursive(d)
left = []...('l', [], 'd')
right = []...('r', [], 'd')     return [d]
DFSRecursive(e)
left = []...('l', [], 'e')
right = []...('r', [], 'e')     return [e]
[b,d,e]
DFSRecursive(c)
left = []...('l', [], 'c')
DFSRecursive(f)
left = []...('l', [], 'f')
right = []...('r', [], 'f') return [f]
['c','f']
[a]+['b', 'd', 'e']+['c', 'f']
"""
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
tree.DepthFirst(a)   #['a', 'b', 'd', 'e', 'c', 'f']
tree.DFSRecursive(a)
tree.BreadthFirst(a) #['a', 'b', 'c', 'd', 'e', 'f']
