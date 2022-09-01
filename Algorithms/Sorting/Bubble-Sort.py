"""
Perform bubble sort on below list.
Time complexity - O(n^2) and space complexity is O(1).
Iterate through each element with next element and swap position if the prev element > next element.

           l=99,44,6,2
Iteration 1: 44,99,6,2
             44,6,99,2
             44,6,2,99

            l=44,6,2,99
iteration 2: 6,44,2,99
             6,2,44,99

           l=6,2,44,99
iteration 3: 2,6,44,99

"""

def bubble_sort(array):

    length = len(array)
    for i in range(0,length):
        for j in range(0,length-1):
            if array[j]>array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

        print(i,array)
    print('final_array',array)

    return array

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

print('before',numbers)
bubble_sort(numbers)
