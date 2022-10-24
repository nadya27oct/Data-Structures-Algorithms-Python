"""
Implement a queue using a stack.
Use main stack to perform queue operations.
A holding stack to initially push elements.
For pop operation, return pop from main stack after moving elements from Holding stack.

If main stack is not empty, then pop from main.
If main stack is empty, then pop from holding.
"""

class Queue:
    def __init__(self):
        self.main = []
        self.holding = []

    def push(self,x):
        self.holding.append(x)
        return

    def pop(self):
        main_stack = self.move_from_holding_to_main()
        return main_stack.pop()

    def peek(self):
        main_stack = self.move_from_holding_to_main()
        return main_stack[-1]

    def move_from_holding_to_main(self):

        if len(self.main) ==0:
            while len(self.holding) > 0:
                self.main.append(self.holding.pop())

        return self.main

queue = Queue()
queue.push(5)
queue.push(31)
queue.push('gates')
print(queue.peek()) #5
print(queue.pop()) #5
print(queue.peek())
print(queue.pop()) #31
print(queue.peek())
