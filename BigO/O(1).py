a100 = list(range(100))
a10000 = list(range(10000))
a100000 = list(range(100000))

def find_10th_and_20th_element(array):
    t0 = time.time()
    print(array[9])
    print(array[19])

    t1=time.time()

    print('Time taken:',round(t1-t0,4))


find_10th_and_20th_element(a100)
find_10th_and_20th_element(a10000)
find_10th_and_20th_element(a100000)

'''
Run time operation - O(1) - Regardless of the size of input, the operation only occurs once.
Constant Time - Getting a value from specifc index
'''
