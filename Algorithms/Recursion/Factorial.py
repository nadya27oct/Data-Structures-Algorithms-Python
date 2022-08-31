"""
Write two functions that finds the factorial of any number. One should be recursive and the other should use a for loop (iterative).
If n = 4.
Recursive: 5! = 5 * 4!
                    4 * 3!
                        3 * 2!
                            2 * 1!
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

factorial = factorial_iterative(0)
factorial = factorial_iterative(5)
factorial = factorial_iterative(7)

# Time complexity - O(n-2) in Iterative function.

def factorial(n):

    if n < 2:
        return 1

    return n * factorial(n-1) # We keep going until we hit the base case,n=2.
    #n -= 1

recursive = factorial(3)
recursive = factorial(5)

#factorial(3 * factorial(2 * factorial(1)))
# Time complexity in Recursive function - O(n) as we call function recursively.
