'''
Given two sorted arrays, return a sorted array merged by two inputs.

Check input. Can 2nd array be empty? Are both inputs arrays?

a = [2,4,6,8], ab=[2,5,11] => final=[2,2,4,6,6,8,11]
final = a1

min(a[0],b[0]) => 2
min(a[1],b[0]) => 2
min(a[1],b[1]) => 4
min()

'''
def merged_array(array1,array2):

    final=[]
    i = 0
    j = 0

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            final.append(array1[i])
            i += 1

        else:
            final.append(array2[j])
            j += 1

    while i < len(array1):
        final.append(array1[i])
        i += 1

    while j < len(array2):
        final.append(array2[j])
        j += 1

    return final

array1=[0,3,70]
array2=[4,6,30,37,90]

print(merged_array(array1,array2))
