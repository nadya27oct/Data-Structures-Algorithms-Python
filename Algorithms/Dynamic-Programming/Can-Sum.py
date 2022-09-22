"""
Write a function that takes a targetSum and an array of numbers as arguments. Return true or false if targetSum
can be generated using numbers from array.
You may use an element as much as you want.
targetSum = 7 array=[5,3,4,7]

If an element > tragetSum, ignore those elements.
7-5=2; All array elements > targetSum, so stop traversal.
7-3=4; Eligible elements - [3,4]: 4-3 = 1
                                4-4 = 0. base
7-4=3; Eligible elements - [3]: 3-3 = 0
7-7=0 <-- base case
                    7
     (-5)    (-3)       (-4)    (-7)
     2        4           3        0
          (-3)  (-4)    (-3)
          1       0       0

targetSum = 7 array=[2,4]
             7
        (-2)  (-4)
        5           3
    (-2)  (-4)      (-2)
    3       1          1
  (-2)
   1

Height of the tree in worst case: targetSum = m
Branching factor: length of array: n. Each level can have nodes=# of elements.
Total nodes = n^m, time complexity = O(n^m)
Space complexity = O(m); height of tree in worse case.
"""

def canSum(targetSum,array):

    if targetSum == 0:
        return True

    if targetSum < 0:
        return False

    for i in array:
        remainder = targetSum - i
        if canSum(remainder,array) == True:
            return True
    return False

print(canSum(7,[5,3,4,7]))

# For DP solution, find common subtrees. Can i generate a target sum using roots of subtree.

def memoized_canSum(targetSum,array,memo={}):

    if targetSum in memo:
        return memo[targetSum]

    else:
        if targetSum == 0:
            return True

        if targetSum < 0:
            return False

        for i in array:
            remainder = targetSum - i
            if memoized_canSum(remainder,array,memo) == True:
                memo[targetSum] = True
                return True

        memo[targetSum] = False
        return False

print(memoized_canSum(7,[5,3,4,7],{}))
print(memoized_canSum(300,[4,7],{}))

"""
Now we do not have to explore a subtree that is already in cache.
So time complexity reduces to n*m (total nodes visited): O(n*m)
Space complexity = O(m); height of tree in worse case.
"""
