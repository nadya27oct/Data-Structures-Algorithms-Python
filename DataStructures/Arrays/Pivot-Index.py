"""
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal
to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there
are no elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0

Brute force:
i=0; check a[:0] = [] vs a[1:]
i=1; check a[:1] == a[2:]
i=2; check a[:2] == a[3:]
i=3; check a[:3] == a[4:]
i=4; check a[:4] == a[5:]
i=5; check a[:5] vs a[6:]

Input: nums = [1,7,3,4,1,6]
       left = [1,8,11,15,16,22]
      right = [22,21,14,11,7,6]

left[3] + array[1] + right[4] =

Input: nums = [1,7,3,6,5,6]
       left = [1,8,11,17,22,28]
      right = [28,27,20,17,11,6]

      left[3] = right[5-2] = right[3]


"""

def pivotindex(array):

    for i in range(len(array)):
        if sum(array[:i]) == sum(array[i+1:]):
            return i

    return -1

pivotindex([1,7,3,6,5,6])
pivotindex([1,2,3])
pivotindex([2,1,-1])

def pivotindex_1(array):

    n = len(array)
    left = [1] * n
    left[0] = array[0]

    for i in range(1,n):
        left[i] = array[i] + left[i-1]

    right = [1] * n

    pivot = []
    for j in range(n-1,-1,-1):
        if j==n-1:
            right[j] = array[n-1]
        else:
            right[j] = right[j+1] + array[j]

        if right[j] == left[j]:
            pivot.append(j)

    if pivot:
        return pivot.pop()
    return -1

pivotindex_1([-1,-1,0,1,1,0])
pivotindex_1([1,7,3,6,5,6])
pivotindex_1([-1,-1,0,0,-1,-1])
pivotindex_1([2,1,-1])
pivotindex_1([-4,4,10])

"""
[1,7,3,1,2,9]
l = 1,8,11,12,14,23
r = 23,14,12
"""

def pivotindex_2(array):

    leftSum = 0
    rightSum = sum(array)

    for i in range(len(array)):
        leftSum += array[i]
        if rightSum == leftSum:
            return i
        rightSum -= array[i]

    return -1

assert pivotindex_2([-1,-1,0,1,1,0]) == 5
assert pivotindex_2([1,2,3]) == -1
assert pivotindex_2([2,1,-1]) == 0
