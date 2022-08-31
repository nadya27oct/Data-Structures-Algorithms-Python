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

#Time complexity - Linear O(n). Space complexity- Linear O(n)


def fibonacciRecursive(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)

print('recursive 2',fibonacciRecursive(2))
print('recursive 3',fibonacciRecursive(3))
print('recursive 5',fibonacciRecursive(5))
print('recursive 10',fibonacciRecursive(10))
