'''
Implement Stacks using Arrays.
Start initializing array with an empty array.
[udemy-> 0]
[udemy ->0, google -> 1]
['udemy','google']

'''

class ArrayStack:
    def __init__(self):
        self.array = []

    def peek(self):
        if len(self.array) == 0:
            print('empty array')

        else:
            print('last item',self.array[len(self.array)-1])

    def push(self,value):
        self.array.append(value)

        return self.array

    def pop(self):
        self.array.pop()

        return self.array

my_stack = ArrayStack()
my_stack.peek()
print(my_stack.push('udemy'))
print(my_stack.push('google'))
print(my_stack.push('discord'))
print(my_stack.push('stack_overflow'))
my_stack.peek()
print(my_stack.pop())
my_stack.peek()
