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

findKthLargest([3,2,1,5,6,4], 4)
findKthLargest([3,2,1,5,6,4], 2)

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
len(greater) + 1 < k ==>  3 < 4; function([3,2,1],k=1)
pivot = 1, nums = [3,2]; less = [], greater = [3,2]
len(greater) + 1 < k ==>  3 > 1 ; function([3,2],k=1)
pivot = 2, nums = [3]; less = [], greater = [3]
len(greater) + 1 < k ==>  2 > 1 ; function([3],k=1)
pivot = 3, nums = []; less = [], greater = []
len(greater)+1 = k, so pivot = 3
"""


def kthLargest(nums,k):

    n = len(nums)
    K = n - k

    def quickSelect(l,r):

        pivot = nums[r]     # last element
        pointer = l         # left most index

        for i in range(l,r):
            if nums[i] <= pivot:
                nums[pointer],nums[i] = nums[i],nums[pointer]
                pointer += 1

        nums[pointer],nums[r] = nums[r],nums[pointer]
        if pointer > K:
            return quickSelect(l,pointer-1)

        if pointer < K:
            return quickSelect(pointer+1,r)

        if pointer == K:
            return nums[pointer]

    return quickSelect(0,n-1)

kthLargest([4,9,8,2,6],2)
kthLargest([3,2,1,5,6,4], 4)

"""
3rd approach: Quick Select
n = [4,9,8,2,6], k=2: sorted = [2,4,6,8,9] => len(n) - k = 5-2=> sorted n[3] = 8

quickSelect(0,5); start --> pointer = 0, pivot = nums[4] = 6 --> [4, 9, 8, 2, 6]
i=0, pivot = 6, 4 < 6; pointer = 1, nums[1] = 9, nums[0]= 4
i=1, pivot = 6, 9 > 6; pointer = 1, nums[1] = 9, nums[1]= 9
i=2, pivot = 6, 8 > 6; pointer = 1, nums[1] = 9, nums[2]= 8
i=3, pivot = 6, 2 < 6; pointer = 2, nums[2] = 8, nums[3] = 9 -->  [4, 2, 8, 9, 6]
END OF LOOP --> [4, 2, 6, 9, 8]
pointer = 2, k = 3, So pointer < K

quickSelect(3,4); start --> [4, 2, 6, 9, 8]
i=3,  pointer = 3; pivot = nums[4] = 8, 9 > 8
END OF LOOP; swap pointer with right most element.
nums = [4,2,6,8,9]
pointer = 3, k = 3: So nums[3]=8
"""
