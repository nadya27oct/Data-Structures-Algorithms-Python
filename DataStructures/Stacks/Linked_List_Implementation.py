'''
Stack is a data structure that allows adding and removing elements in a Last In First Out order.
First element that is added last is also the element that is removed first.
Udemy->Twitter->Google
'''

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0   #initially top & bottom of stack is empty

    def peek(self): # Look up top node of stack
        pass

    def push(self): # add node to top
        pass

    def pop(self): # remove node from top
        pass
