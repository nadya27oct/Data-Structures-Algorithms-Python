"""
347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Input: nums = [3,3,3,3], k = 1
Output: [3]

nums = [11,11,5,9,9,9,9,30,11,30]
freq = {11:3, 5:1, 9:4, 30:1} k=2
buckets = {{1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: []}}
Add each k,v in freq to buckets where buckets[key] = v.
{1: [5], 2: [30], 3: [11], 4: [9], 5: [], 6: [], 7: [], 8: [], 9: [], 10: []}
"""

def kFreq(nums,k):

    if len(nums) == 1:
        return nums

    freq = dict()

    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    buckets = {i:[] for i in range(1,len(nums)+1)}

    for num,count in freq.items():
        if count in buckets:
            buckets[count].append(num)

    k_most = []
    for n in range(len(buckets),0,-1):
        if buckets[n] != []:
            for num in buckets[n]:
                k_most.append(num)
                if len(k_most) == k:
                    return k_most


print(kFreq([11,11,5,9,9,8,30,30,11,30],k=2)) # {1: [8, 5], 2: [9], 3: [11, 30], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: []}
print(kFreq([1,1,1,2,2,3,3,4,5,6], k = 3))
print(kFreq([38,20,17,17,38,38,38,13,47,20], k = 3))
