"""
If Fibonacci problem is implemented recursively, the space time complexity is O(2^n) as we have to increase call stack to
fibonacci function with each recursive call.
By implementing dynamic programming solution, we can improve space complexity to O(n) through a technique called memoization where we store
value of subproblems.
"""
cache = {}
def fibonacci_dynamic(n):

    if n in cache:
        return cache[n]

    else:
        if n < 2:
            cache[n] = n
            return cache[n]
        else:
            cache[n] = fibonacci_dynamic(n-1) + fibonacci_dynamic(n-2)
            return cache[n]

print('fibonacci at 10th index',fibonacci_dynamic(10))
print('fibonacci at 9th index',fibonacci_dynamic(9))
print('fibonacci at 8th index',fibonacci_dynamic(8))

# O(n) space and time complexity
