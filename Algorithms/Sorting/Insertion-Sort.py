"""
Implement insertion sort. Compare each element with next and if it is higher, compare with previous element before that
and move it to the front.
Assume x=[7,12,90,3].
Compare x[0] < x[1] : nothing happens.
        x[1] < x[2] : nothing happens
        x[2] > x[3] : x[2],x[3] = x[3],x[2]
        x[2] < x[1] (3<12), x[2],x[1] = x[1],x[2]
        x[1]

for i in range(3):
    if a[i] > a[i+1]:  -->a[2] > a[3]
        a[i+1],a[i] = a[i],a[i+1] --> a[3],a[2] ==a[2],a[3]
----------------------------------------
a=[7,12,3,90]
i=[0,1,2,3]
        for i in range(i,0,-1)
            if a[i] < a[i-1]             --> a=[1]
                a[i],a[i-1] =a[i-1],a[i] --> a=[7,3,12,90]
"""
def insertSort(array):

    for i in range(len(array)-1):
#First we loop over the array. If element is greater than next element, switch positions and keep checking if it is higher than previous element.
        if array[i] > array[i+1]:
            array[i+1],array[i] = array[i],array[i+1]

            for i in range(i,0,-1):
                if array[i] < array[i-1]:
                    array[i],array[i-1] = array[i-1],array[i]

    return array


# Time complexity - O(n^2) but can be O(n) if array is nearly sorted.
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
insertSort(numbers)
