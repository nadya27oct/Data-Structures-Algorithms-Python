"""
Implement Merge Sort.
Merge sort uses divide and conquer approach.
1. Divide the array into smaller sub-arrays until there is only 1 element left. Base case - 1 element per sub-array.
2. Sort each subarray.
2. Merge sorted sub-arrays until the entire input array is sorted.
"""

def mergeSort(arr):

    if len(arr) <= 1:
        return arr
    else:                       # Split array into sub-arrays at the mid point
        mid = len(arr)/2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        return merge_sorted_arrays(
                    mergeSort(left_arr),
                    mergeSort(right_arr))

def merge_sorted_arrays(left,right):

    #Merge two sorted arrays. left = [4,5,13], right=[7,10,11]
    result=[]
    i=j=0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1                      # 4<7, result=[4], i=1,j=0.5<7, result=[4,5], i=2,j=0.
                                        #13>7,result=[4,5,7] i=2,j=1. 13>10,result=[4,5,7,10] i=2,j=2.
        else:                           #13>11,result=[4,5,7,10,11] i=2,j=3. while condition (i<3 & j<3) is false -> j=3.
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i +=1

    while j < len(right):
        result.append(right[j])
        j +=1

    print(result)
    return result

array = [5,4,13,10,7,1]
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
mergeSort(numbers)
mergeSort(numbers)
