"""
11. Contain with Most Water
https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

min = 1, max = 8, area = 1
6>min & 6<max; area = 1*2 or new min= 6; 6*1 -> maxArea = 6
2<min; new min = 2; 2*2 or current max; maxArea = current = 6
5<min; 5*3 or current max; maxArea = 5*3=15; new min = 5
4<min;4*4 or current max: maxArea = 16; new min = 4
8>=max; max = 8; 8*5 = 40
3<min; 3*6 or current max = 40
7>min & 7<max; area = 40 or new min = 7; 7*7
"""
def bruteforceArea(height):

    area = 0

    for i in range(len(height)):
        for j in range(i+1,len(height)):
            h = min(height[i],height[j])
            cur = h*(j-i)
            area = max(cur,area)

    return area

print(bruteforceArea([8,2]))
print(bruteforceArea([4,1,8,6,2]))
print(bruteforceArea([1,8,6,2,5,4,8,3,7]))


def maxArea(height):

    if len(height) == 2:
        return min(height)

    area = 0
    l=0
    r=len(height)-1

    while l<r:
        h = min(height[l],height[r])
        curArea = h*(r-l)
        area = max(area,curArea)

        if height[l] < height[r]:
            l+=1
        elif height[l] >= height[r]:
            r-=1

    return area

print(maxArea([4,1,8,6,2]))
print(maxArea([1,8,6,2,5,4,8,3,7]))
