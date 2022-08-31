"""
Write two functions that finds the factorial of any number. One should be recursive and the other should use a for loop (iterative).
If n = 4.
n * (n-1) * (n-2) * (n-3) * (n-5)
5 * (5-1) * (5-2) * (5-3) * (5-4)
i=0; 0<4; factorial = 5 * 4 =
                          20 * 3 =
                              60 * 2 =
                                   120 * 1 = 120
"""

def factorial_iterative(n):
    if n <=1:
        return 1
    else:
        i = 2
        output = n * (n-1)
        while i < n:
            output = output * (n - i)
            i += 1

        return output

factorial = factorial_iterative(5)
print(factorial)
factorial = factorial_iterative(7)
print(factorial)
factorial = factorial_iterative(0)
print(factorial)
# Time complexity - O(n)
