boxes = [1,2,3,4,5]


def create_all_pairs(array):

    pairs = []
    for i in range(len(array)):
        for j in range(len(array)):
            pairs.append([array[i],array[j]])
    print(pairs)
create_all_pairs(boxes)

'''
Run Time Operations - On^2
Nested Loops are O(n * n) - Quadratic time
Every time number of elements increase, operations increase quadratically.
When each element of a collection/array is compared with each element from another collection,
run time operation is O(a*b).
'''

def matching_characters(array1,array2):

    for i in array1:
        for j in array2:
            print(i,array1.index(i),array2.index(j))

array1='language'
array2='spanish'
matching_characters(array1,array2)

'''
Run Time Operation - O(n * m)
'''
