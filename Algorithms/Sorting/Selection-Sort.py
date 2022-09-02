"""
Implement a selection sorting algorithm.
Scanning list of items for smallest element and swap the beginning of the list with  that to front.
Loop through list twice to compare each element with one another.
x = [4,5,3,0]
First element is min. i=0=min. Then loop through elements from i+1 to last element comparing each to min.
Update min after each loop.
min = i = 0; check if x[0]>x[1]. Then min = i = 1
"""

def selection_sort(array):

    items = len(array)
    for i in range(items-1):
        min = i #0
        temp = array[i] # 8
        for j in range(i+1,items): #range(1,4):j=1,j=2, j=3
            if array[min] > array[j]: # a[0]=8 > a[1]=5, a[1]=5 > a[2]=4, a[2]=4>a[3]=1
                min = j              #min=5-->i=1, min=4..i=2...min=1..i=3=min


        array[i] = array[min]
        array[min] = temp
        print(array)

    return array

list = [6, 44, 99, 2, 3]
selection_sort(list)

# Time complexity - O(n^2) as we have tested for loops.
