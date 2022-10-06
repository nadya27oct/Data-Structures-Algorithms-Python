"""
Given a head of a linked list, determine if the linked list has a cycle in it.
pos indicates the index of node the tail of linked list next is connected to.
3->2->0->-4; pos = 1. Linked list is a circle. 4->2

1->5->8->1; pos=-1. Linked List is not a circle.

1->2; pos=0. Linked list is a circle 2->1.

3 -> 2 -> 0 -> -4; pos=2
two pointers = i, j = 0
increment i+1 and j+2. Eventually i+j if linked list is a cycle.
3 -> 2 -> 0 -> -4
    i=1  j=2            at 1st iteration (2,0)
         i=2
    j=1                 at 2nd iteration (0,2)
               i=3
               j=3      at 3rd iteration

1 -> 5 -> 8 -> 4 -> 3; pos=-1
i=1      j=1
    i=2       j=2
         i=3
"""

class Node:
    def __init__(self,val=0):
        self.val = val
        self.next = None

    def isCycle(self,head):

        visited = set()

        current_node = head
        while current_node!= None:
            if current_node in visited:
                return True
            else:
                visited.add(current_node)
            current_node = current_node.next
        return False
# Time complexity - O(n) as we have to visit every node once and adding a node is O(1) operation.
# Space complexity - O(n) as we have to add every node to visited set.

    def LinkedListCycle(self,head):

        slow=head
        fast=head

        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
# Time complexity - O(n) as we have to visit every node once to find a cycle.
# Space complexity - O(1) as we only maintain 2 variables - fast and slow.

a = Node(3)
b = Node(2)
c = Node(0)
d = Node(-4)

a.next = b
b.next = c
c.next = d
d.next = b  #3->2->0->-4

node = Node()
print(node.isCycle(a))
print(node.LinkedListCycle(a))

one = Node(1)
two = Node(5)
three = Node(8)
four = Node(1)

one.next =two
two.next = three
three.next = four

single = Node(2) # 2

node.isCycle(one)
node.LinkedListCycle(one)
print(node.LinkedListCycle(single))
