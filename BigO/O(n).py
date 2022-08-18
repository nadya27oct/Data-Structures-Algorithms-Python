import time
array = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank']

a100 = ['nemo' for i in range(100)]
a10000 = ['nemo' for i in range(10000)]
a100000 = ['nemo' for i in range(100000)]

def findnemo(array):

    t0=time.time()
    for i in range(len(array)):
        print('running')
        if array[i] == 'nemo':
            print('Found Nemo')
            break
    t1=time.time()
    print('Time taken:',round(t1-t0,3))

findnemo(array)
findnemo(everyone)
findnemo(a100)
findnemo(a10000)
findnemo(a100000)

'''
Run time operation - O(n) Linear Time.
As number of elements in an array increases, the number of operations increases in a linear manner.
'''
