"""
Given an integer n, find the index value of Finbonacci sequence.
Finbonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
Each value is the sum of 2 previous numbers.
If n = 5, 2+3=5.
If n = 8, 8+13=21.
index      value
0         0 = 0
1         1 = 1
2         1 = 1 + 0 = a[2] = a[1] + a[0]
3         2 = 1 + 1 = a[3] = a[2] + a[1]
4         3 = 2 + 1 = a[4] = a[3] + a[2]
5         5 = 3 + 2 = a[5] = a[4] + a[3]
n                     a[n] = a[n-1] + a[n-2]
        2  3
a=[0,1,1+0,2+1]

recursive(5) = recursive(4) + recursive(3)
recursive(4) = recursive(3) + recursive(2)
recursive(3) = recursive(2) + recursive(1)
recursive(2) = recursive(1) + recursive(0)
"""


def fibonacciIterative(n):

    fibonacci = [0,1]

    for i in range(2,n+1):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

    return fibonacci[n]

fib_4 = fibonacciIterative(4)
fib_5 = fibonacciIterative(5)
fib_8 = fibonacciIterative(8)
fib_15 = fibonacciIterative(15)
print('iterative 40',fibonacciIterative(40))

#Time complexity - Linear O(n-2). Space complexity- Linear O(n)


def fibonacciRecursive(n):

    if n < 2:
        return n
    else:
        return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)

print('recursive 1',fibonacciRecursive(1))
print('recursive 3',fibonacciRecursive(3))
print('recursive 5',fibonacciRecursive(5))
print('recursive 10',fibonacciRecursive(10))
print('recursive 40',fibonacciRecursive(40))
"""
Space complexity is O(2^n). As n increases with each additional element, the function calls increase exponentially.
fibonacci(4)--->fibonacci(3)--->fibonacci(2)--->fibonacci(1)
                                            --->fibonacci(0)
                            --->fibonacci(1)
            --->fibonacci(2)--->fibonacci(1)
                            --->fibonacci(0)
Recursive is not an optimal solution for Finbonacci Series.
"""
