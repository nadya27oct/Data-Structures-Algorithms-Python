"""
Linked Lists are linear data structures represented by nodes that contains a value and a pointer to next node.
Here we traverse through each node in a linked list starting from head node.
"""
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d # d is tail so d.next = null
# print_linked_list(a) # A->B->C->D->null

def print_linked_list(head):

    current = head

    while current!=None: # As long as current node is not null, there are nodes to iterate through.
        print(current.val)
        current = current.next


def recursive_linked_list(head): # Base case: when are you done with function call.

    if head==None:
        return

    print(head.val)
    recursive_linked_list(head.next)

recursive_linked_list(a)

"""
Return an array for a given linked list with all value nodes within that linked list.
LL: A->B->C->D->null
output arr: ['A','B','C','D']
"""


def linked_list_array(head):

    arr = []

    current = head
    while current != None:
        arr.append(current.val)
        current = current.next

    return arr

print('iterative_array',linked_list_array(a))

q = Node("q")
print('iterative_array',linked_list_array(q)) # -> [ 'q' ]
print('iterative_array',linked_list_array(None))

def recursive_linked_list_array(head):
    arr = []
    fill_values(head,arr)
    return arr

def fill_values(head,arr):

    if head==None:
        return
    arr.append(head.val)
    fill_values(head.next,arr)

print('recursive_array',recursive_linked_list_array(a))

# Recursion is spilt into two functions, so we do not have to create multiple arrays whenever recursion function is called.

"""
Write a function to sum all nodes in a linked list that takes head of a linked list as argument.
# 2 -> 8 -> 3 -> -1 -> 7 == 19

In recursive method, base case is if node is null, return 0. Typically for linked lists, base case is when head is null.
Then return that sum to previous node at 7. total sum = 7
Then return that sum to previous node at 1. total sum = 8
Keep returning that sum to previous node until we reach head.
Time = Space--> O(n) because of call stack. Each recursive function utilizes space.
We have to add every function to call stack.

recursive_sum(a) = a.val + recursive_sum(b)
                 = a.val + + b.val + recursive_sum(c)
"""
a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

def sum_list(head):
    sum = 0

    current = head
    while current != None:
        sum += current.val
        current = current.next

    return sum

sum_list(a)  #Time complexity= O(n); Space=O(1)


def recursive_sum(head):

    if head == None:
        return 0

    return head.val + recursive_sum(head.next)

recursive_sum(a)

"""
Given a linked list, find if a target value exists. Return a boolean value.
a -> b -> c -> d
linked_list_find(a, "c") --> true
"""

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

def linked_list_find(head,target):

    current = head
    while current != None:
        if current.val == target:
            return True
        current = current.next

    return False

linked_list_find(a,'c')
linked_list_find(a,'x')

node1 = Node("jason")
node2 = Node("leneli")

node1.next = node2 # jason -> leneli
linked_list_find(node1, "jason")

def recursive_linked_list_find(head,target):

    if head == None:
        return False

    if head.val == target:
        return True

    return recursive_linked_list_find(head.next,target)

recursive_linked_list_find(a,'q')
recursive_linked_list_find(a,'d')
recursive_linked_list_find(node1, "jason")


"""
Write a function, get_node_value, that takes in the head of a linked list and an index.
The function should return the value of the linked list at the specified index.
If there is no node at the given index, then return None.
"""
