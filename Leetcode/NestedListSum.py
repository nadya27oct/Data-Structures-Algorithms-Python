"""
339. Nested List Weight Sum
You are given a nested list of integers nestedList. Each element is either an integer
or a list whose elements may also be integers or other lists.

Depth of an integer is the number of lists that it is inside of.
For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

Return the sum of each integer in nestedList multiplied by its depth.

Input: nestedList = [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.

Input: nestedList = [1,[4,[6]]]
Output: 27
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.

nestedList = [[1,1],2,[1,1]]. Nested entries are 7. Maximum level of nesting - 2
N = # of nested entries in a list.
D = maximum level of nesting that function is called recursively.
Space complexity = O(N)
Time(n) = O(D)
"""
def depthSum(nestedList):

    total_depth = 0
    for i in range(len(nestedList)):
        depth_at_i = compute_element_depth(nestedList[i],weight=0)
        total_depth += depth_at_i

    return total_depth

def compute_element_depth(nestedE,weight):
    
    if type(nestedE) == list:
        nestedSum= 0
        for i in range(len(nestedE)):
            nestedSum += compute_element_depth(nestedE[i],weight + 1)
        return nestedSum

    depth = nestedE
    weight += 1
    return weight * depth

depthSum([2,3])
depthSum([[1,1],2,[1,1]])
depthSum([1,[4,[6]]])
depthSum([[[2,3]]]) # 2*3+3*3=15
