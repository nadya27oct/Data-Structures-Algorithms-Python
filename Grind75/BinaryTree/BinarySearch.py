"""
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12]
target = 9
Output: 4


Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

List is sorted so we can discard half the items instead of traversing through every element.
Start in middle and check if 9 >= mid point.
Divide input array by half.
Is target > mid point. Go right.
Is target < mid point. Go left.
Is taregt = mid point. End.

example1 = [-1,0,3,5,9,12], target = 9
left = 0
right = 5
mid point => (5+0)/2 = 2. a[2] = 3.
9 > 3. Go right.
Left = 0+2+1 = 3.
a[3:] = [5,9,12]
mid point => (3+5)/2 = 4
9 == 9. End.

example 2 = [-1,0,3,5,9,12], target = 2
left = 0
right = 5.
mid point = (5+0)/2--> a[2] = 3
2 < 3. Go left.
Left = 0
right = mid point - 1 = 2-1 = 1
[-1,0]
mid point = 0+1/2 = 0; a[0]
2 > -1, Go right.
left = mid + 1 = 1
right = 1
a[1] = 0


"""

class Solution:
    def search(self, nums, target):

        left = 0
        right = len(nums)-1

        return self.binary_search_recursive(nums,target,left,right)

    def binary_search_recursive(self,nums,target,left,right):

        if left <= right:
            mid_point = (left + right) / 2

            if target == nums[mid_point]:
                return mid_point

            elif target > nums[mid_point]:
                return self.binary_search_recursive(nums,target,mid_point+1,right)

            else:
                return self.binary_search_recursive(nums,target,left,mid_point-1)

        else:
            return -1

obj = Solution()
print(obj.search([-1,0,3,5,9,12],9))
print(obj.search([-1,0,3,5,9,12],12))
print(obj.search([-1,0,3,5,9,12],2))

class IterativeSolution:

    def search(self,nums,target):

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) / 2


            if target == nums[mid]:
                return mid
            elif target < nums[mid]: # Discard all elements to right of mid point.
                end = mid - 1
            else: # target > nums[mid], discard all elements to left of mid point.
                start = mid + 1
        return -1

iterative = IterativeSolution()
print(iterative.search([-1,0,3,5,9,12],9))
print(iterative.search([-1,0,3,5,9,12],12))
print(iterative.search([-1,0,3,5,9,12],2))
