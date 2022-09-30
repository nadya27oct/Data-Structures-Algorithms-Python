"""
Given a list of n integers arr[0..(n-1)], determine the number of different pairs of elements within it which sum to k.
If an integer appears in the list multiple times, each copy is considered to be different;
that is, two pairs are considered different if one pair includes at least one array index which the other doesn't,
even if they include the same values.

Example 1: n = 5, k = 6
arr = [1, 2, 3, 4, 3, 7, 7]
output = 2
The valid pairs are 2+4 and 3+3.
{1:1,2:1,3:2,4:1,7:2}


Example 2: n = 5, k = 6
arr = [1, 5, 3, 3, 3]
output = 4
There's one valid pair 1+5, and three different valid pairs 3+3 (
the 3rd and 4th elements, 3rd and 5th elements, and 4th and 5th elements).

{1: 1, 3: 3, 5: 1, 9:1}
A combination of keys equal to k.
"""

def numberOfways(arr,k):

    n = len(arr)
    pairs = dict()
    for a in arr:
        if a in pairs:
            pairs[a] +=1
        else:
            pairs[a] = 1

    counter = 0
    for a in arr:
        remainder = k - a #6-1
        if remainder in pairs and remainder == a:
            counter += 1
        if remainder in pairs and remainder != a:
            counter += 0.5
    return int(counter)

numberOfways([1, 5, 3, 3, 3, 9],6)
numberOfways([1, 2, 3, 4, 3, 7, 7],6)
print(numberOfways([1, 2, 3, 4, 3],10))
