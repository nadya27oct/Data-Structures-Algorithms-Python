
'''
Implement Linked List class.
10 -->5--> 16
First attribute is head, 2nd attribute is next.

LinkedList =
{head:
    {value:10,
    next:
        {value : 5,
        next : {value: 16,
                next: null}}}}
We implement node in a class called Node. Creates an object instance with 2 variables.
data - to keep node value.
next - as pointer
__init__ : To initialize node and covers data extraction & storage (self.data) and pointer to connected node (self.next)

'''
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None # Pointer to next node. Last element is always pointing to Null.

class LinkedList:

    def __init__(self):
        self.head = Node() #Doesnt contain actual data. Placeholder to allow us to point to 1st element to the list.
        #self.tail = self.head
        #self.length = 0
# When we first create the Linked List, the list is empty & there are no nodes.
# So head -> None & tail -> head = None. Empty list has length 0.

    def insert(self,data): # Add a new data point to the end of current list.
        new_node = Node(data)
        cur = self.head
        while cur.next != None: # Next node of the current node is not Null, iterate through each node.
            cur = cur.next
        cur.next = new_node

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head

        self.head = new_node

        return


    def display_linked_list(self):

        if self.head == None:
            return 'Empty Linked List'
        else:
            elements = []
            cur_node = self.head
            while cur_node.next != None:
                cur_node = cur_node.next
                elements.append(cur_node.data)

            return elements

MyLinkedList = LinkedList()
print(MyLinkedList.display_linked_list())
MyLinkedList.insert(10)
print(MyLinkedList.display_linked_list())
MyLinkedList.insert(5)
print(MyLinkedList.display_linked_list())
MyLinkedList.insert(16)
print(MyLinkedList.display_linked_list())
MyLinkedList.prepend(1)
print(MyLinkedList.display_linked_list())


class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linkedlist:

    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self,data):
        new_node = node(data)

        if self.head == None:
            self.head = new_node

        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1

        return

    def prepend(self,data):
        new_node = node(data)
        new_node.next = self.head # new_node.next is the pointer of new value -> which will be pointing to current head.
        self.head = new_node #No longer old head. It is the new value

    def print_linkedlist(self):
        linked_list = []
        current_node = self.head

        while current_node!=None:
            linked_list.append(current_node.data)
            current_node = current_node.next

        return linked_list

    def length_ll(self):
        count = 0
        current_node= self.head

        while current_node !=None:
            count += 1
            current_node = current_node.next

        return count

    def insert_ll(self,index,value):
        if index >= self.length:
            return self.append(value)

        new_node = node(value)

        leader = self.traverse_to_index(index-1)
        holding_pointer = leader.next ##['One', 18.5, 3, 'Berlin', 99] 3 is held at holding pointer
        leader.next = new_node
        new_node.next =  holding_pointer

        return

    def traverse_to_index(self,index):
        counter = 0
        current_node = self.head

        while counter < index: #['One', 18.5, 3, 'Berlin', 99]
            current_node = current_node.next # keep moving current node to right.
            counter += 1

        return current_node

    def remove_element(self,index):
        # Assume index is positive and less than length of ll.
        #'One'-> 18.5 -> 100 -> 3 -> 'Berlin'-> 99
        # Remove 100 @ index = 2. Point 18.5 -> 3. Find the leader (18.5) & then we need a reference to 3
        leader = self.traverse_to_index(index-1)
        #print('leader current',leader.data) 18.5
        #print('leader next',leader.next.data) 100

        unwanted_node = leader.next # Remove this node 100. leader.next point to node at 2nd index where value =100.
        leader.next = unwanted_node.next # We now want 18.5 to point to 3.

        return
'''
We have 3 nodes. *--*--*
Insert a node after 2nd *. We need to find when we reach 2nd node.
traverse to index(2). 0,1,2. at the end of this method, we know what 1st node is pointing to.
'''

ll = linkedlist()
#ll.head = node(10)
#print('head',ll.head.data)
#print('pointer at head',ll.head.next)

ll.append(18.5)
ll.append(3)
ll.append('Berlin')
print(ll.length_ll())
print(ll.print_linkedlist())
ll.prepend('One')
ll.insert_ll(200,99)
print(ll.print_linkedlist())
#print(ll.traverse_to_index(2))
ll.insert_ll(2,100)
print(ll.print_linkedlist())
ll.remove_element(2)
print(ll.print_linkedlist())
print('value of last node in linked list',ll.tail.data)
print('value of head node pointer',ll.head.next.data)
