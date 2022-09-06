"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example 1:
Input: nums = [2,7,11,15], target = 22
Output: [1,3]
Explanation: Because nums[1] + nums[3] == 22, we return [1, 3].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Brute force solution. Compare each element with one another- 2 with 7,11 & 15. Then 7 with 11 and 15. Then 11 with 15.
Time complexity - O(n^2)
Using a hash table, we can store each element and its key hash[i] = array[i].
Then check if target - element (lets say dif) exists in hash table keys.
If it exists, return element position and value of dif, i.e. [i,hash[dif]=i].
If not add to keep adding to hash.
22 - 2 = 20 -> {2:0}
22 - 7 = 15 -> {2:0,7:1}
22 - 11 = 11 -> {2:0,7:1,11:2}
22 - 15 = 7 -> 7 is in key
Time complexity - O(n) as we are only looping through array once. Access in hash table is O(1) as we access by key.
Space complexity - O(n) as we have to store in hash.
"""

def pair_exists(array,target):

    pair = dict()
    for i in range(len(array)):
        diff = target - array[i]

        if diff in pair:
            return [pair[diff],i]
        else:
            pair[array[i]] = i

nums = [3,2,4]
target = 6
print(pair_exists(nums,target))
nums = [2,7,11,15]
target = 22
print(pair_exists(nums,target))
print(pair_exists([3,3],target=6))
