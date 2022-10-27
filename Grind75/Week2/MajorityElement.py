"""
169. Majority Element
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than n / 2 times.
You may assume that the majority element always exists in the array.

Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

def majorityElement(nums):

    majority = len(nums)//2

    freq = dict()

    for n in nums:
        freq[n] = 1 + freq.get(n,0)
        if freq[n] > majority:
            return majority

print(majorityElement([3,4,3]))
print(majorityElement([2,2,1,1,1,2,2])) # O(n) = space = time

def Majority(nums): # Constant space

    max_element = None
    count = 0

    for n in nums:
        if count == 0:
            max_element = n
        count += 1 if n == max_element else  -1
    return max_element

print(Majority([3,4,3]))
print(Majority([7, 7, 5, 7, 5, 1]))
