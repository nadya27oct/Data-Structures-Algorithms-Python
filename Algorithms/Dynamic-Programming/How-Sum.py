"""
Write a function that takes a targetSum and an array of numbers as arguments.
Return any combination of array that generates target sum.
targetSum = 7 array=[5,3,4,7]
output = [3,4] or [7]

                    7
     (-5)    (-3)       (-4)    (-7)
     2        4           3        0
          (-3)  (-4)    (-3)      []
          1       0       0
        null      []      []

Time complexity:
Number of recursive calls O(n^m)
Space: stack space O(m)
"""

def howSum(targetSum,array,new=[]):

    if targetSum == 0:
        return []

    if targetSum < 0:
        return None

    for i in array:
        remainder = targetSum - i
        result = howSum(remainder,array,new)
        if result!= None:
            new.append(i)
            return new

    return None

print(howSum(7,[5,3,4,8],[]))
print(howSum(8,[2,3,5],[]))
print(howSum(7,[2,4],[]))


def memoized_howSum(targetSum,array,memo={}):

    if targetSum in memo:
        return memo[targetSum]
    else:
        if targetSum == 0:
            return []

        if targetSum < 0:
            return None

        for i in array:
            remainder = targetSum - i
            result = memoized_howSum(remainder,array,memo)
            if result!= None:
                result.append(i)
                memo[targetSum] = result
                return memo[targetSum]

        return None

print(memoized_howSum(7,[5,3,4,8],{}))
print(memoized_howSum(8,[2,3,5],{}))
print(memoized_howSum(7,[2,4],{}))

"""
Memoized
# of Recursive calls - O(m*n*m). Time complexity reduced from exponential to polynomial with memoization.
Each recursive call appends to list.
O(m*m)
Space complexity mostly comes from memo hash.
Key is unique values of target sum and value is an array of size n.
"""
