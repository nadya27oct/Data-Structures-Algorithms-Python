"""Implement a function that reverses a string using iteration and recursion.
Iterative: string = 'star'
list = [], iterate through list & append(last element) to list. Then join.
['r','a','t','s']
Recursion: Any string that is empty or contains 1 letter: reverse = string.
len(string > 2).
b = b
l = ba => ab
l.pop() + l.pop()
l = bar => rab
l.pop() + l.pop() + l.pop() = l.pop + recursion('ba')
l = bark => krab
l.pop() + l.pop() + l.pop() + l.pop() = l.pop() + recursion('bar')
string.pop+string.pop+string.pop+string.pop
"""

def reverse_iterative(string):

    reverse = []
    for i in range(len(string)-1,-1,-1):
        reverse.append(string[i])

    return ''.join(reverse)


print(reverse_iterative('yoyo mastery'))

def reverse_recursive(string):

    if len(string) < 2:
        return string

    else:
        str_list = list(string)

        return str_list.pop() + reverse_recursive(string[:-1])

print(reverse_recursive('bark'))
print(reverse_recursive('yoyo mastery'))

#What is the simplest input? This is base case. Here when string = [] or 1 letter, reverse is the same.
