"""
215. Kth Largest Element in an Array
Given an array and an integer k, find the kth largest element in sorted array not kth distinct element.
Solve in O(n) time complexity.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

"""

def brute_force_method(nums,k):

    nums.sort()

    return nums[-k]

brute_force_method([3,2,3,1,2,4,5,5,6], k = 4)
# Time complexity = O(N log N) where N = # of elements in array.
# Space complexity = 0(1)

def findKthLargest(nums, k): # [3,2,1,5,6,4], k=2

    lesser = []
    greater = []
    pivot = nums.pop() # 4

    for n in nums: #[3,2,1,5,6], k = 2, pivot = 4;
        if n < pivot:
            lesser.append(n) #less = [3,2,1]
        else:
            greater.append(n) #greater = [5,6]

    if len(greater)+1 == k: # 3 vs 2
        return pivot
    elif len(greater)+1 > k: # 3 > 2
        return findKthLargest(greater, k)
    else:
        return findKthLargest(lesser,k - len(greater) - 1)

print(findKthLargest([3,2,1,5,6,4], 4))
print(findKthLargest([3,2,1,5,6,4], 2))

# nums = [1,2,3,4,5,6]; 4th largest element is nums[2] = 3

"""
2nd approach:
function([3,2,1,5,6,4],k=2); pivot = 4
nums = [3,2,1,5,6]; less = [3,2,1], greater = [5,6]
len(greater)+1 > k => 3 > 2: function([5,6],k=2); pivot = 6
nums = [5]
less = [5]; greater = []
len(greater)+1 < k => 1 < 2: function([5],k=1); pivot = 5
nums = []
len(greater)+1 > k => 1 == 1, so pivot = 5

function([3,2,1,5,6,4],k=4); k = arr[2]
pivot = 4, nums = [3,2,1,5,6]; less = [3,2,1], greater = [5,6]
len(greater) + 1 < k ==>  3 < 4; function([3,2,1],1)
pivot = 1, nums = [3,2]; less = [], greater = [3,2]
len(greater) + 1 < k ==>  3 > 1 ; function([3,2],1)
pivot = 2, nums = [3]; less = [], greater = [3]
len(greater) + 1 < k ==>  2 > 1 ; function([3],1)
pivot = 3, nums = []; less = [], greater = []
len(greater)+1 = k, so pivot = 3
"""
