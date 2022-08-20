'''
Question
Given an array and a sum, return true or false if any pairs of elements in the array add up to the sum.

examples
list = [6,4,3,2,1,7], sum=9
==>true [6,3],[2,7]
'''

# Brute force solution
# Check each element against other elements.
# a[0] a[1]
# a[0] a[2]
# a[1] a[2]

def has_pairs_with_sum(array,sum):

    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] + array[j] == sum:
                return True

    return False

print(has_pairs_with_sum([6,4,3,2,1,7],9))
print(has_pairs_with_sum([9,10,1,2],9))

# Time complexity - O(n*2). Quadratic time operations

'''
Better solution
Instead of looping through array twice, we can check if sum
set = empty
9 - 6 = 3 not in
9 - 4 = 5 if 5 not in a[i]
sum - element ==> compliment in array => return true
sum - element not in array go to next element
'''

def has_pairs_with_sum1(array,sum):

    elements = set()
    for i in range(len(array)):
        if i in elements:
            return True
        else:
            elements.add(sum - array[i])

    return False

print(has_pairs_with_sum1([6,4,3,2,1,7],9))
