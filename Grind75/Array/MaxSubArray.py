"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
"""

def brute_force_subarray(array):

    max = array[0]
    for i in range(0,len(array)):
        sum = array[i]
        for j in range(i+1,len(array)):
            sum += array[j]

            if sum > max:
                max = sum

    return max


brute_force_subarray([5,4,-1,7,8])
brute_force_subarray([1,-3,2,1,-1])
"""
[-2, 2, 5, -11, 6]
[-2, 2, 7, -4, 2]
i=0; maxSum = -2; curSum=-2
i=1; curSum = max(2,2-2) = 2; maxSum = 2
i=2; curSum = max(5,5+2) = 7; maxSum = 7
i=3; curSum = max(-11,-11+7) =-4; maxSum = 7
i=4; curSum = max(6,-4+6) = 6; maxSum = 7
"""

def max_sum_from_subarray(array):
    maxSum = array[0]
    curSum = array[0]
    for i in range(1,len(array)):
        curSum = max(array[i],array[i]+curSum)
        maxSum = max(curSum,maxSum)


    return maxSum

print(max_sum_from_subarray([5,4,-1,7,8]))
print(max_sum_from_subarray([-2,1,-3,4,-1,2,1,-5,4]))
