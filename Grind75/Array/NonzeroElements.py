"""
For an array of integers, write an algorithm that brings all non zero elements to left of array and returns the number of non-zero elements.
The algorithm should operate in place, i.e. do not create a new array.
Order of non-zero elements does not matter.
arr = [1,0,2,0,0,3,4]. Possible answer is 4 after arranging array [4,3,2,1,0,0,0]

ex: [1,0,0,2]
a[0]=1. not 0. keep where it is. counter = 1--> [1,0,2,0]
a[1]=0. move it to temp. queue. counter = 1--> [1,]
a[2]=2. not 0. if before is 0 swap 2 with a[i-1].
a[3]=0. 0. kepe it there as we have reached end.

[1,0,0,2]
1,
"""

def brute_force_shift_zeros(array):

    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] == 0:
                array[i],array[j] = array[j],array[i]
    counter = 0
    for i in array:
        if i != 0:
            counter +=1
        else:
            break

    return array,counter

# print(brute_force_shift_zeros([1,0,2,0]))
# print(brute_force_shift_zeros([0,0,0,0,9,8,10,-4]))
# print(brute_force_shift_zeros([1,0,0,2]))

def shift_zeroes(array):

    counter = 0
    for i in range(len(array)-1):
        if array[i] == 0:
            j = next_none_zero_element(i,array)
            if j:
                array[i],array[j] = array[j],array[i]

            else:
                return array,counter

        if array[i] != 0:
            counter +=1

def next_none_zero_element(i,array):

    for j in range(i+1,len(array)):
        if array[j] != 0:
            return j

# print(shift_zeroes([1,0,2,0,0,3,4]))
# print(shift_zeroes([0,0,0,0,9,8,10,-4]))

def move_zeroes(array):

    l = 0

    for r in range(len(array)):
        if array[r]!=0:
            array[l],array[r] = array[r],array[l]
            l += 1

    return l,array

print(move_zeroes([1,3,0,0,12]))
"""
[0,1,0,3,12] r=0,l=0
[1,0,0,3,12] r=1,l=1
[1,0,0,3,12] r=2,l=1
[1,3,0,0,12] r=3  a[1],a[3]=a[3],a[1] l=2
[1,3,0,0,12] r=4  a[2],a[4]=a[4],a[2] l=3
"""
