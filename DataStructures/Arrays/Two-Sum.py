'''
Given an array of integers nums and an integer target, return indices of two numbers such that their sum equals target.
Solution should be less than O(n^2) complexity.

nums=[3,2,10,4]
target = 6 ---- Output = [1,2]

nums=[3,3]
target = 6 ---- Output = [0,1]

Brute force - checking each elements of the array. O(n^2) operation.
for i in range(3), for j in range(1,3), if nums[i] + nums[j] = target, print(i,j)

Less Time Complex Method
Turn array into a hash map where element is key and index is value.
start with empty hash.
is 6 - 3 = 3 not in hash, add to hash with index. hash={3:0}
6 - 2 = 4 not in hash, add to hash. hash ={3:0,2:1}
6 - 10 = -4 not in hash so hash = {3:0,2:1,10:2}
6 - 4 in hash. return hash[2],4

'''

def pair_sum_brute_force(nums,target):

    for n in range(len(nums)):
        for m in range(n+1,len(nums)):
            if nums[n] + nums[m] == target:
                return([n,m])

print(pair_sum_brute_force(nums=[3,2,10,4],target=6))
print(pair_sum_brute_force(nums=[3,3],target=6))

def pair_sum(nums,target):

    nums_hash = dict()

    for i in range(len(nums)):
        if target - nums[i] in nums_hash:
            return [nums_hash[target - nums[i]],i]
        else:
            nums_hash[nums[i]] = i

print(pair_sum(nums=[3,2,10,4],target=6))
print(pair_sum_brute_force(nums=[3,3],target=6))
print(pair_sum_brute_force([7,2,11,13],target=24))
