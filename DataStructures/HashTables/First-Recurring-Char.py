'''
Given an array, find the first recurring character.

array = [2,5,1,2,3,5,1,2,4]. It should return 2
array = [2,1,1,2,3,5,1,2,4]. It should return 1
array = [2,3,4,5].It should return undefined

for each element if it doesnt exist, add it as key
2, not in hash so hash[2] = 1
5 not in hash so hash[5] = 1
1 not in hash so hash[1] = 1
2 in hash -> output 2
'''
def recurring_character(array):


    counts = dict()
    for i in range(len(array)-1):
        if array[i] in counts:
            return array[i]

        else:
            counts[array[i]] = 1

    return 'undefined'


print(recurring_character([2,5,1,2,3,5,1,2,4]))
print(recurring_character([2,1,1,2,3,5,1,2,4]))
print(recurring_character([2,3,5,4]))

# Increase space complexity by O(n)
# But time complexity is at O(n)
