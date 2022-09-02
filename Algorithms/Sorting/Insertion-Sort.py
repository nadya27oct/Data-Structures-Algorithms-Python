"""
Implement insertion sort. Compare first 2 elements
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
        if array[i] > array[i+1]:
            array[i+1],array[i] = array[i],array[i+1]

            for i in range(i,0,-1):
                if array[i] < array[i-1]:
                    array[i],array[i-1] = array[i-1],array[i]

    return array

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
insertSort(numbers)
