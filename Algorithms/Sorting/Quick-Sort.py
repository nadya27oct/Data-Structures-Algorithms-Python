"""
Implement Quick Sort algorithm.
Quick Sort - Choose pivot element (last or random).
Stores elements less than pivot in left sub array. Stores elements greater than pivot in right sub-array.
Call quick sort recursively in sub-arrays (left and right).

1. Pivot: array[-1]
2. Left reference: element at lowest index => array[0]
3. Right reference: element at highest index excluding pivot => array[pivot-1]
4. While left reference is < pivot, increase left pointer: left+=1.
    While right reference > pivot, decrease right pointer: right -=1.
5. If both left reference > pivot and right reference < pivot, swap left and right.
6. Once left ref index >= right ref index, swap left with pivot.
"""

def quicksort(array,leftIndex,rightIndex): # Initially we call function on entire array passing index=0 and index=len-1

    if len(array) <= 1:
        return array

    if leftIndex < rightIndex: # Sub array contains at least 2 elements.

        pivotIndex = partition(array,leftIndex,rightIndex)  # partition based on what is to left of pivot and right of pivot.
        print("pivot is", array[pivotIndex])

        quicksort(array,leftIndex,pivotIndex-1)
        quicksort(array,pivotIndex+1,rightIndex)

    return array

def partition(array,left,right):

    i=left
    j=right-1
    pivot = array[right]

    while i<j:
        while i < right and array[i] < pivot:
            i += 1

        while j > left and array[j] > pivot:
            j -= 1

        if i < j:
            array[i],array[j] = array[j],array[i]

    if array[i] > pivot:
        array[i],array[right] = array[right],array[i]

    print('array after swapping i and pivot',array)
    return i


array = [19, 22, 63, 105, 2, 46]
print(array)
print(quicksort(array,0,len(array)-1))

# Use quick sort when average performance matters more than worst case.
# Time complexity - O(n log n). But worse case = O(n^2) depending on how pivot is picked.
# Space complexity - O(log n)
