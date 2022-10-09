"""
56.Merge Intervals
Given an array of intervals where intervals[i] = [start_i, end_i], merge all
overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

[[1,5],[4,7],[6,10],[11,14],[15,17],[16,20]]]
compare end_0 >= start_1
i=0; start_0=1, end_0=5, start_1=4, end_1=7 => [1,7]
i=1; start_0=1, end_0=7, start_1=6, end_1=10 => [1,10]
i=2; start_0=1, end_0=10, start_1=11, end_1=14 => condition not met; append merged. result = [1,10]
i=3; start_0=11, end_1=14, start_1=15, end_1=17 => condition not met; append merged. result = [1,10],[11,14]
i=4; start_0=15, end_0=17, start_1=16, end_1=20 => [15,20]. last element, so append. result = [1,10],[11,14],[16,20]

[[1,4],[5,6]]
i=0; start_0=1, end_0=4, start_1=5, end_1=6 => condition not met; append merged. result = [1,4]
last element. append to result = [[1,4],[5,6]]

start = [1,5], end = [4,7]
start[1] >= end[0]; 5>=4; merged = [1,7]
start = [1,7], end = [6,10]; 7>=6; merged = [1,10]
start = [1,10], end = [15,17]; 10<15; APPEND [1,10]
start = [15,17] end = [16,20]; 17>=16; merged = [15,20]
"""

def mergeIntervals(intervals):

    result = []
    intervals.sort() # O(n log n)
    n = len(intervals)
    i = 0
    start = intervals[0]

    while i < n-1: # O(n)
        end = intervals[i+1]

        if start[1] >= end[0]:
            start = [start[0],max(start[1],end[1])]
        else:
            result.append(start)
            start = end
        i += 1
    result.append(start)
    return result

print(mergeIntervals([[1,4],[0,0]]))
print(mergeIntervals([[1,4],[0,1]])) # [[0, 4]]
print(mergeIntervals([[1,4],[2,3]])) #[[1,4]]]
print(mergeIntervals([[1,3]]))
print(mergeIntervals([[1,4],[5,6]]))
print(mergeIntervals([[1,5],[4,7],[6,10],[15,17],[16,20]])) #[[1, 10], [15, 20]]
print(mergeIntervals([[1,4],[0,4]])) #[[0,4]]

# Sorting takes O(n log n) and we loop through each element which takes O(n) linear time. Then total time complexity = O(n log n)
# Space complexity = O(n)
