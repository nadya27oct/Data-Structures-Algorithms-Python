'''
Given two arrays, create a function that lets a user know (true/false)
whether these two arrays contain any common items.
'''
def check_any_common(array1,array2):

    if len(set(array1).intersection(set(array2))) > 0:
        return True

    return False


array1=['a','b','c','x']
array2=['z','y','p','q','c']

check_any_common(array1,array2)

def common_elements(array1, array2):

    for a in array1:
        for b in array2:
            if a == b:
                return True
                break

    return False

common_elements(array1,array2)
#Time complexity - Big O(a*b) as two arrays can be of different size
#Space complexity - No new inputs are created. O(1)

def common_elements1(array1,array2):

    dict1 = dict()
    for a in array1:
        dict1[a] = True

    for b in array2:
        if b in dict1.keys():
            return True

    return False

common_elements1(array1,array2)

'''
Time complexity -  O(a+b) as arrays are looped separately.
Space complexity - O(a) as each element in first array is mapped to a dictionary, which takes up memory.
Although this function is fast, it is heavy on space complexity.


Question to Ask Interviewer
Confirm input parameters and output.
Ask about size of input arrays - for time/space complexity.
Brute force solution. This looks like a nested array loop, comparing each common_elements
of each array.
Testing/Edge cases - Empty arrays, mixed data types in lists, Null values.
'''
