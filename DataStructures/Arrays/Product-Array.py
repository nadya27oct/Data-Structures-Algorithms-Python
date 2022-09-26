"""
Given an array, output a product of array except for self.
[1,2,3,4]  --> [24,12,8,6]
Brute force: for each element compute product with all other elements.
a[0]: a[1] * a[2] * a[3] b = [1,2,3] = 0
a[1]: a[2] * a[3] * a[0] b = [0,2,3] = 1
a[2]: a[3] * a[0] * a[1] b = [0,1,3]
a[3]: a[0] * a[1] * a[2] b = [0,1,2]

Time complexity - O(n*n)
Space complexity - O(n)
"""

def compute_product(array):

    output = []
    for a in range(len(array)):
        product = 1
        for b in range(len(array)):
            if a != b:
                product *= array[b]
        output.append(product)

    return output


print(compute_product([1,2,3,4]))
print(compute_product([-1,1,0,-3,3]))

"""
[1,2,3,4] --> [24,12,8,6]


a[i] = a[0]..a[i-1] * a[i+1]..a[-1]

Product of array[2] = a[0] * a[1] * a[3]
original arr = [1,2,3,4]
prefix =       [1,2*1=2,3*2=6,4*6]
               [1,2,6,24]
suffix =       [24,24,12,4]
a[0] = prefix[-1] * suffix[1]
a[1] = prefix[0] * suffix[2] = 1*12
a[2] = prefix[1] * suffix[3] = 2*4
a[3] = prefix[2] * suffix[4] = 6

Time complexity - O(n)
Space complexity - O(n)
"""

def compute_product_1(array):

    n = len(array)
    prefix = [1] * n
    prefix[0] = array[0]

    for i in range(1,n):
        prefix[i] = array[i] * prefix[i-1]

    suffix = [1] * n
    suffix[n-1] = array[-1]

    for i in range(n-2,-1,-1):
        suffix[i] = array[i] * suffix[i+1]

    output = [1] * n
    output[0] = suffix[1]

    for i in range(1,n-1):
        output[i] = prefix[i-1] * suffix[i+1]

    output[n-1] = prefix[n-2]

    return output

print(compute_product_1([1,2,3,4]))

"""
Improve space complexity to O(1) by storingb output in same array.

[2,5,3,4]
[60,24,40,30]

left = [2,10,30,120]
       [0, 1, 2, 3]
right = [120,60,12,4]
        [0, 1, 2, 3]

output[3] = 30 = left[2]
output[2] = 10 * 4
output[1] = 2 * 12
output[0] = 60
"""

def compute_product_2(array):

    n = len(array)
    output = [1] * n
    product = 1

    for i in range(n):
        output[i] = product * array[i] # [2,10,30,120]
        product = product * array[i]

    output[n-1] = output[n-2] # output[3] = output[2] = 30, new output = [2,10,30,30]

    product = array[n-1] # product starts at 4. product array = [120,60,12,4]
    for j in range(n-2,0,-1):
        output[j] = product * output[j-1]
        product = product * array[j]

    output[0] = product
    return output

print(compute_product_2([2,5,3,4]))
print(compute_product_2([1,2,3,4]))
