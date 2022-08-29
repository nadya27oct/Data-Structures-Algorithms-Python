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
