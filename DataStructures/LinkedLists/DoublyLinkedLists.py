class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def add_element_to_end_of_list(self,value):

        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.prev = self.head

        else:
            new_node.prev = self.tail
            self.tail.next = new_node #[10->5]
            #print('new_node val',new_node.value)

        self.tail = new_node
        self.length += 1
        #print('tail after each insert',self.tail.value)

        return

    def add_element_to_start(self,value):

        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = self.head

        else:
            new_node.next = self.head #[10,5] insert 6.->[6,10,5]
            self.head.prev = new_node
            self.head = new_node

        self.length +=1
        return

    def insert(self,index,value):


        if index >= self.length:
            self.add_element_to_end_of_list(value)

        elif index ==0:
            self.add_element_to_start(value)

        else:
# a=[1, 10, 5, 16, 20]. Add 90 at index = 2.
#a1=[1, 10, 99, 5, 16, 20]
            new_node = Node(value)
            current_node = self.head

            for i in range(index - 1): #[0,1]-->[1,10]-->[2,5]
                current_node = current_node.next

            leader = current_node # Current node is at index =2, value = 10.
            follower = leader.next # 5 comes after 10.
            leader.next = new_node #Get leader to point to new node
            new_node.prev = leader #New node should point to leader on left
            new_node.next = follower # new node should also point to follower on right
            follower.prev = new_node # follower should point to new node to left

        self.length +=1

        return

    def display_list(self):


        if self.head is None:
            print('empty list')

        else:
            doubly_ll = []

            while self.head is not None:
                doubly_ll.append(self.head.value)
                self.head = self.head.next

            return doubly_ll


dll = DoublyLinkedList()
dll.add_element_to_end_of_list(10)
dll.add_element_to_end_of_list(5)
dll.add_element_to_end_of_list(16)
dll.add_element_to_start(1)
dll.insert(100,20)
dll.insert(2,99)
print(dll.display_list())
