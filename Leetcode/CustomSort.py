"""
791. Custom Sort String
You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
Permute the characters of s so that they match the order that order was sorted.
More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.
Return any permutation of s that satisfies this property.

Example 1:

Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation:
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in order, it can be at any position in the returned string.
"dcba", "cdba", "cbda" are also valid outputs.

Example 2:
Input: order = "cbafg", s = "abcd"
Output: "cbad"


order = "cba"
order_dict = {c:0,b:1,a:2}

s = "abccd"
s_position = {2:a,1:b,0:c} --> append d to final
s_count = {a:1,b:1,c:2}

n = size of order
m = size of s
Time = n + m + m = 0(N)
Space = n + m + m = 0(N)
"""

def customSortString(order,s):

    order_d = dict()

    for i in range(len(order)):
        order_d[order[i]] = i

    s_order = dict()
    s_count = dict()

    final = ""
    for j in s:
        if j in order_d:
            s_order[order_d[j]] = j
            if j not in s_count:
                s_count[j] = 0
            s_count[j] +=1
        else:
            final += j

    for i in range(len(s_order)):
        letter = s_order[i]
        string = letter * s_count[letter]
        final += string


    return final

customSortString(order = "cba", s = "abcd")   #dcba
customSortString(order = "kqep", s = "pekeq") #kqeep

"""
Efficient method
order = 'cba'; s = 'aabcccdfg'
s_freq = {a:2, b:1, c:3, d:1, f:1, g:1}

We don't need a dictionary to maintain order index of first one.
Multiply each element from 'order' with the freq count in s.
Then add any remaining characters in s with their freq count to final answer.

for i in order:
    if i in s_freq:
        final = i * s_freq[i]
"""

def sortString(order,s):

    final = ""
    s_freq = dict() #

    for i in s:
        if i not in s_freq:
            s_freq[i] = 0
        s_freq[i] += 1

    for o in order:
        if o in s_freq:
            final += o * s_freq[o]
            s_freq.pop(o)

    remaining = [k*v for k,v in s_freq.items()]

    return final+"".join(remaining)

print(sortString("cba","aabcccdfg"))
print(sortString("xycbaf","jiybafc"))
