'''
peek - get first node
enqueue - add a node
dequeue - remove from a queue. Removes from front of the list.
Each person below gets in line in this order - 1. Joy, 2. Matt, 3. Pavel, 4. Samir
dequeue one by one based on first come first serve basis.
'''
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if self.length > 0:
            return self.first.value
        else:
            return('Empty Queue')

    def enqueue(self,value):
        new_node = Node(value)

        if self.first == None:  #Joy -> first = last
            self.first = new_node
            self.last = new_node

        else:
            self.last.next = new_node #Matt: Joy -> head; Matt -> last  Joy->Matt
            self.last = new_node #Pavel: Joy -> head; Pavel -> last......Joy -> Matt -> Pavel

        self.length += 1

        return

    def dequeue(self):
        if self.length <= 1:
            self.first = None
            self.last = None
        else:
            second_node = self.first.next   # queue=[Joy -> Matt -> Pavel -> Samir]
            self.first = second_node        #dequeue= [Matt -> Pavel -> Samir]

            # print('current second_node',second_node.value)
            # print('new 1st node',self.first.value)
            # print('new 2nd node',self.first.next.value)

        self.length -= 1
        return


queue = Queue()
queue.enqueue('Joy')
queue.enqueue('Matt')
queue.enqueue('Pavel')
queue.enqueue('Samir')
queue.peek()
queue.dequeue()
queue.peek()
queue.dequeue()
queue.peek()
