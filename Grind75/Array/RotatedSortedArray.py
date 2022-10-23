"""
Leetcode 33
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
"""

def search(nums,target):

    l = 0
    r = len(nums)-1

    return BinarySearch(nums,target,l,r)

def BinarySearch(nums,target,l,r):

    if l <= r:
        mid = (l+r) // 2

        if target == nums[mid]:
            return mid

        if nums[mid] >= nums[l]:    # left portion
            if target > nums[mid] or target < nums[l]:
                return BinarySearch(nums, target, mid+1, r)
            if target < nums[mid]:
                return BinarySearch(nums, target, l, mid-1)

        else: # right portion -> a = [5,1,2,3,4], target = 1
            if target < nums[mid] or target > nums[r]:
                return BinarySearch(nums, target, l, mid-1)
            if target > nums[mid]:
                return BinarySearch(nums, target, mid+1, r)
    else:
        return -1

arr1 = search([4,5,6,7,0,1,2],target=0) #4
arr2 = search([4,5,6,7,0,1,2],target=3) #-1
arr3 = search([1],target=0) #-1
arr4 = search([5,1,3], target = 3) # 2
arr5 = search([5,1,3],target = 5) # 0
arr6 = search([5,1,2,3,4], target = 1) #1
arr7 = search([4,5,6,7,8,0,1,2], target = 2) #7
arr8 = search([4,5,6,7,8,1,2,3],8) #4

# Time (n) = O(log n) as it is a binary search
# Space (n) = O(log n) as we have to call function recursively.
