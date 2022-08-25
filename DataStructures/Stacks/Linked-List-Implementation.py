'''
Stack is a data structure that allows adding and removing elements in a Last In First Out order.
First element that is added last is also the element that is removed first.
Peek: Add node to top. We want "Google" --> "Udemy"
Stack = "udemy"
top = bottom = "udemy"
Add google: "google" -> "udemy"; new_node is Google .
Google should point to current head. new_node.next = current head
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
        if self.length > 0:
            print('Top node of stack',self.top.value)

        else:
            print('Empty Stack')


    def push(self,value):
        new_node = Node(value)

        if self.length == 0: # stack = Empty. top = bottom = udemy.
            self.top = new_node
            self.bottom = new_node
            print('Top=Bottom=',self.top.value)
        else:
            current_head = self.top   #We want to hold reference to whatever is top
            self.top = new_node  #Google will not be the top node.
            self.top.next = current_head
            print('top node',self.top.value)

        self.length += 1
        return


    def pop(self):
# current stack = ['stack_overflow','discord','google','udemy']. remove stack_overflow.
# current top -> stack_overflow. current top NEXT -> discord.
# new top = discord.
        if self.length <= 1:
            self.top = None
            self.bottom = None
            print('Stack is empty')

        else:
            current_top = self.top
            self.top = current_top.next
            print('node removed',current_top.value)
            print('current top',self.top.value)

        self.length -= 1

mystack = Stack()
mystack.peek()
mystack.push('udemy')
mystack.push('google')
mystack.push('discord')
#mystack.push('stack_overflow')
mystack.pop()
mystack.pop()
mystack.pop()
mystack.peek()
