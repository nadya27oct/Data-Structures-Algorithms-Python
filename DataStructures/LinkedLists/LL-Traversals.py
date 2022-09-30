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

linked_list_array(a)

q = Node("q")
linked_list_array(q) # -> [ 'q' ]
linked_list_array(None)

def recursive_linked_list_array(head):
    arr = []
    fill_values(head,arr)
    return arr

def fill_values(head,arr):

    if head==None:
        return
    arr.append(head.val)
    fill_values(head.next,arr)

recursive_linked_list_array(a)

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
Write a function to return the value of the linked list at the specified index.
If there is no node at the given index, then return None.

# a -> b -> c -> d
get_node_value(a, 2) = 'c'
get_node_value(a, 7) = None

For recursive solution, we have 2 base cases. When node is Null, return null.
Affirmative base case: when count == index, return node value.

traverse_ll(c,2,2) --> return 'class'
traverse_ll(b,2,1)
traverse_ll(a,2,0)
"""

def get_node_value(head,index): # Time complexity: O(n); Space: O(1)

    count = 0
    current = head

    while current!=None:
        if count == index:
            return current.val
        count +=1
        current = current.next
    return

get_node_value(a,2)
get_node_value(a,7)

def recursive_node_value(head,index):

    count = 0
    return traverse_ll(head,index,count)

def traverse_ll(head,index,count):
    if head == None:
        return

    if count == index:
        return head.val

    count += 1
    return traverse_ll(head.next,index,count)

print('recursive',recursive_node_value(a,2))
print('recursive',recursive_node_value(a,7))

# Another recursive method: start at index = 2 and return node value corresponding to index = 0.
def recursive_node_value_1(head, index):

    if head == None:
        return

    if index == 0:
        return head.val

    return recursive_node_value_1(head.next,index-1)

print('2nd_recursive',recursive_node_value_1(a,3))
print('2nd_recursive',recursive_node_value_1(a,0))
print('2nd_recursive',recursive_node_value_1(a,7))

"""
Reverse a linked list. Return new head of linked list.
      A->B->C->D->null
null<-A<-B<-C<-D

We need a previous pointer. At the end, A is tail. So A.next -> Null and D is head node.
Stop when current is at null.

At the start, current -> head -> A. previous -> null. next -> B
At B, current -> head = B
     current.next = A       A<-B
     previous -> A

At C,  current -> C
       current.next = previous = B  A<-B<-C

At D, current -> D
      previous = C A<-B<-C<-D

current.next = Null. Loop ends. Previous = D.

At each step, we need to point current node to its previous.
"""
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")

a.next = b
b.next = c
c.next = d
d.next = e

def reverse_list(head): #A->B->C->D->null

    current = head      #current = A
    previous = None     #previous = Null, current.next =B

    while current != None:
        next = current.next #B. Do not want to lose pointer from A.
        current.next = previous # Reverse. Point current node to previous node. Now previous becomes the current node we are sitting
        previous = current  #Advance previous and current nodes.
        current = next #current = B

    return previous

#reverse_list(a)

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

def recursive_reverse(head,prev=None):

    if head == None:
        print(prev.val)
        return prev

    next = head.next # next=b
    head.next = prev # current = a; a->Null
    prev = head
    return recursive_reverse(next,prev)

recursive_reverse(a)
