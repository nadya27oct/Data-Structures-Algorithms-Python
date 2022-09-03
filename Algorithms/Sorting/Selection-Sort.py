"""
Implement a selection sorting algorithm.
Scan an array for smallest element and swap the smallest to beginning of the list - which becomes sorted partition.
Currnt minimum is the first number in unsorted partition. Then we progress through array looking for the minimum number.
a = [6, 44, 99, 2, 3]
Initially, 6 is minumum. We loop through array and find that 2 is the smallest number.
We swap 6 and 2: a = [2, 44, 99, 6, 3]. We now have 2 in sorted partition.
Moving to next iteration, 44 is current minmum and scan through remaining unsorted partition to find the smallest number - 3.
Swap 44 and 3: a = [2, 3, 99, 6, 44].
Then 99 is the current min and as we loop through entire array, 6 become min: a = [2, 3, 6, 99, 44].
"""

def selection_sort(array):

    items = len(array)
    for i in range(items-1):
        min = i #0
        temp = array[i] # 8         array=[4,5,3,0]
        for j in range(i+1,items): #range(1,4):j=1,j=2, j=3
            if array[min] > array[j]: # a[0]=8 > a[1]=5, a[1]=5 > a[2]=4, a[2]=4>a[3]=1
                min = j              #min=5-->i=1, min=4..i=2...min=1..i=3=min


        array[i] = array[min]
        array[min] = temp
        print(array)

    return array

list = [6, 44, 99, 2, 3]
selection_sort(list)

# Time complexity - O(n^2) as we have nested loops.
