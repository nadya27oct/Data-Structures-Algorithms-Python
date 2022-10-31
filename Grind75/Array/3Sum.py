"""
15. 3Sum - Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

i;from 0:5 - nums[0] = -1
j;from 1:5 - nums[1] = 0
    k; from 2:5 - nums[2] = 1, from 3:5 - nums[3] = 2, from 4:5 - nums[4] = -1, from 5:5 - nums[5] = -4
j; from 2:5 - nums[1] = 1
    k; from 3:5 - nums[3] = 2, from 4:5 - nums[4] = -1, from 5:5 - nums[5] = -4
j; from 3:5 - nums[3] = 2
    k; from 4:5 - nums[4] = -1, from 5:5 - nums[5] = -4
j; from 4:5 - nums[4] = -1
    k; from 5:5 - nums[5] = -4
"""

def three_sum(nums):

    triplet = []
    n = len(nums)
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if nums[i]+nums[j]+nums[k] == 0:
                    triplet.append([nums[i],nums[j],nums[k]])
    return triplet

print(three_sum([-1,0,1,2,-1,-4]))
print(three_sum([0,1,1]))
print(three_sum([0,0,0]))

"""
Approach 2: Reduce time complexuty from O(n^3).
Sort the array.
To avoid duplicates, check if current element was already encountered.
a[i] + a[j] + a[k] = 0
       a[j] + a[k] = -a[i]
a = -3 3 4 -3 1 2
a.sort()
a = -3 -3 1 2 3 4
first[0] = -3, so target = 3
two combinations in a[1:] where a[i]+a[j] = target
[-3,1,2,3,4]
l = 0 = a[l] = -3
r = 4 = a[r] = 4
-3+4 = 1 < target. increment l,
a[l] = a[1] = 1+4 = 5 > target. decrement r
a[r] = a[3] = 1+3 = 4 > target. decrement r
a[r] = a[2] = 1+2 = 3 == target -> [1,2,-target] -> a[0]+a[2]+a[3]
Now we reach the end of first element. so we increment l and loop breaks.
now i = 1.
what if we have the following a = [-2,-2,0,0,2,2]
a[0] + a[2] + a[5] = -2+0+2.
we want to break the loop. increment l -> a[3] = 0

Time = O(n log n) + O(n^2) = O(n^2)
O(n log n) -> sorting
O(n^2) -> looping through array once to find 1st element and loop again to find next two elements
"""

def threeSum(nums):

    result = []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l = i+1
        r = len(nums) - 1
        while l < r:
            Sum3 = nums[l] + nums[r] + nums[i]
            if Sum3 > 0:
                r -= 1
            elif Sum3 < 0:
                l += 1
            else:
                result.append([nums[i],nums[l],nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1

    return result

print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([-3,3,4,-3,1,2]))
print(threeSum([0,0,0,0]))
