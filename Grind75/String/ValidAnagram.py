"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""

def validAnagram(s,t):

    if len(s) != len(t):
        return False

    freq_count_s = dict()

    for i in s:
        freq_count_s[i] = s.count(i)

    for j in t:
        if j not in freq_count_s:
            return False
        elif j in freq_count_s and t.count(j)!=freq_count_s[j]:
            return False
            
    return True


example1 = validAnagram('anagram','nagaram')
print(example1)
example2 = validAnagram('rat','car')
print(example2)
example3 = validAnagram('ab','b')
print(example3)
example4 = validAnagram('aacc','ccac')
print(example4)
example5 = validAnagram('anagtam','nbgbram')
print(example5)
