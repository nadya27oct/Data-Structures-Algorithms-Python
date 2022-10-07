"""
Given a sorted array and an upper and lower values, return all the missing numbers from array that are inclusive of lower and
upper bounds.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b

Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: ["2","4->49","51->74","76->99"]
Explanation: The ranges are:
[2,2] --> "2"
[4,49] --> "4->49"
[51,74] --> "51->74"
[76,99] --> "76->99"

Input: nums = [-1], lower = -1, upper = -1
Output: []
Explanation: There are no missing ranges since there are no missing numbers.
"""

def MissingRange(nums,lower,upper):

    if lower == upper:
        if len(nums)>0:
            return []
        else:
            return [str(lower)]

    output = []

    if len(nums) == 0:
        output.append(str(lower)+'->'+str(upper))
        return output

    if nums[0] > lower:
        min = lower
        max = nums[0] - 1
        if min == max:
            output.append(str(min))
        if max > min:
            output.append(str(min)+'->'+str(max))

    for i in range(1,len(nums)):
        min = nums[i-1]+1
        max = nums[i]-1
        if min == max:
            output.append(str(min))
        if max > min:
            output.append(str(min)+'->'+str(max))

    if nums[-1] < upper:
        min = nums[-1] + 1
        max = upper
        if min == max:
            output.append(str(min))
        if max > min:
            output.append(str(min)+'->'+str(max))

    return output

print(MissingRange([3,6,8],0,10))
print(MissingRange([0,1,3,50,75],0,99))
print(MissingRange([],0,99))
print(MissingRange([],2,2))
print(MissingRange([-1],-2,-1))
print(MissingRange([3],3,4))
print(MissingRange([-1],-1,-1))
print(MissingRange([1,2,4,10,12],-1,15))

"""Different approach
nums = [1,2,4], lower = -1, upper = 8

Keep a pointer to prev and cur.
prev = lower - 1 = -2
cur = nums[0] = 1           -2+1 < 1-1, -1<=0, ['-1->0',]
prev = 1
cur = nums[1] = 2           1+1 <= 2-1, condition not met, ['-1->0',]
prev = 2
cur = nums[2] = 4           2+1 <= 4-1, 3<=3, ['-1->0','3']
prev = 4
cur = upper + 1 = 9         4+1 <= 9-1, 5<=8, ['-1->0',5->8]

nums = [], lower = 0, upper = 99
prev = -1
len(nums)+1 = 0; for i in range(1); i = len(nums) = 1; cur = 100, -1+1<=100-1; 0<=99; 0->99.

n = len(nums)
iterate through n, so time complexity = O(n)
space complexity, O(n)
"""

def findMissingRange(nums,lower, upper):

    output = []

    prev = lower - 1
    for i in range(len(nums)+1):
        cur = nums[i] if i < len(nums) else upper + 1

        if prev+1 <= cur-1:
            output.append(formatRange(prev+1,cur-1))

        prev = cur

    return output

def formatRange(min,max):

    if min == max:
        return(str(min))
    if max > min:
        return(str(min)+'->'+str(max))

print(findMissingRange([1,2,4,10,12],-1,15))
print(findMissingRange([],0,99))
print(MissingRange([],2,2))
print(MissingRange([-1],-2,-1))
print(MissingRange([3],3,4))
