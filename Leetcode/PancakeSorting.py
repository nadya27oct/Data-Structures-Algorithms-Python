"""
Given an array of integers, sort the array by performing a series of pancake flips.

In one pancake flip we do the following steps:

Choose an integer k where 1 <= k <= arr.length.
Reverse the sub-array arr[0...k-1] (0-indexed).
For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, we reverse the sub-array [3,2,1], so arr = [1,2,3,4] after the pancake flip at k = 3.

Return an array of the k-values corresponding to a sequence of pancake flips that sort array.

Input: arr = [3,2,4,1]
Output: [4,2,4,3]
Explanation:
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: arr = [3, 2, 4, 1]
After 1st flip (k = 4): arr = [1, 4, 2, 3]
After 2nd flip (k = 2): arr = [4, 1, 2, 3]
After 3rd flip (k = 4): arr = [3, 2, 1, 4]
After 4th flip (k = 3): arr = [1, 2, 3, 4], which is sorted.

[3,2,4,1], flip where k=4.
a[0],a[3] -> [1,2,4,3]
a[1],a[2] -> [1,4,2,3]


i=0, j=k-1=3
while i<j-1 and j>i+1:
    a[0],a[3] i=1,j=2
    a[1],a[2] i=2,j=1
i={0,1}
j={3,2}
"""

def flip(arr,k):

    i=0
    j=k-1
    while i<j:
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j-=1

    return arr

def pancake_sort(arr):

    n = len(arr)
    if n <= 1:
        return arr

    else:
        result = []
        while n > 1:
            max_element = max(arr[:n])
            if arr[n-1] != max_element:
                max_idx = arr.index(max_element)
                flip(arr,max_idx+1)
                result.append(max_idx+1)
                flip(arr,n)
                result.append(n)
            n -=1
        return result,arr

print(pancake_sort(arr = [1, 5, 4, 3, 2]))
print(pancake_sort([3,2,4,1]))
print(pancake_sort([1,2,3]))
print(pancake_sort([1,3,1]))
print(pancake_sort([10,9,4,3,2,1,9,10,8,7,9]))

"""
max=len(arr) = 5
a.index(5) = 1, so k  = 2
flip(k+1) -> [5,1,4,3,2]...(1, 5, [2], [5, 1, 4, 3, 2])
if 5 = a[0], flip(k) = 5 -> [2,3,4,1,5]

max=5-1= 4
a.index(4) = 2, so k  = 3
flip(3) -> [4,3,2,1,5]
if 4 = a[0], flip(k) = 4 -> [1,2,3,4,5]

max=5-2= 3
a.index(3) = k  = 2
flip(2) -> [3,1,2,4,5]
if 3 = a[0], flip(k) = 3 -> [2,1,3,4,5]

max=5-3=2
a.index(2) = k  = 1
flip(2) -> [1,2,3,4,5]
"""
