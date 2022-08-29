'''
Question - Implement a Queue using Stacks.
Implement a FIFO queue using only 2 stacks. The implemented queue should support all functions of a queue (push, peek, pop and empty).
Queue - FIFO data structure where elements are inserted from one side (rear) and removed from the other (front).
Stack - LIFO data structure where elements are added and removed from same side (top).

Queue           Stacks
|d|             |d| - d comes out first
|c|             |c|
|b|             |b|
|a| - a comes   |a|
    out first
'''

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self,x):
        """Push element x to back of queue. Stack 1 is the main stack. Stack 2 is holding stack.
        Push 1. stack1 = [1]        stack2=[]
        Push 2. stack1 = []         stack2=[1]
                stack1 = [2]        stack2=[1] --- pop stack2 & append to stack1
                stack1 = [2,1]      stack2=[]
        Push 3. stack1 = []         stack2=[2,1] -- pop stack1 & append to stack2
                stack1 = [3]        stack2=[2,1]
                stack1 = [3,2,1]    stack2 = [] -- pop stack2 & append to stack1
        """
        while len(self.stack1)!=0:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(x)

        while len(self.stack2)!=0:
            self.stack1.append(self.stack2.pop())

        return self.stack1

    def pop(self): # Removes the element at the front of the queue and returns it.
        remove_item = self.stack1.pop()

        return remove_item

    def peek(self): # Returns the element at the front of the queue.
        return self.stack1[-1]

    def empty(self):
        if len(self.stack1) == 0:
            return True
        else:
            return False


obj = MyQueue()
push_1 = obj.push(1)
push_2 = obj.push(2)
push_3 = obj.push(3)
print('Front of the queue',obj.peek())
pop = obj.pop()
print('element removed',pop)
is_empty = obj.empty()
print(is_empty)
