"""
383. Ransom Note
Given two strings ransomNote and magazine, return true if ransomNote can be
constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Input: ransomNote = "a", magazine = "b"
Output: false

Input: ransomNote = "aa", magazine = "ab"
Output: false
ransom = {a:2}, magazine = {a:1,b:1}


1 approach: O(n log n) time complexity
ransomNote.sorted() == magazine.sorted()

2nd approach:
keep a frequency of ransom through hash map -> ransom = "aaq" -> ransom = {a:2,q:1}
keep a frequency of magazine only for those items in ransom: magazine: "husyakia" -> magazine = {a:2}
if len(ransom_hash) != len(magazine_hash): return false
if ransom[letter] > magazine[letter]: return false
else true

Time complexity: 0(r+k+r) = 0(n)
0(r) where r=number of ransomNote elements
0(k) where # O(k) where k = number of r in magazine
0(r) to iterate through r

Space: 0(r+r) = O(n)
"""
import collections

def canConstruct(ransomNote,magazine):

    freq_ransom = collections.Counter(ransomNote)

    freq_magazine = dict()
    for m in magazine:
        if m in freq_magazine:
            freq_magazine[m] += 1
        else:
            if m in freq_ransom:
                freq_magazine[m] = 1

    if len(freq_magazine) != len(freq_ransom):
        return False

    for letter in freq_ransom: # O(c) where c=number of common elements between ransomNote and magazine.
        if freq_ransom[letter] > freq_magazine[letter]:
            return False
    return True


print(canConstruct("fihjjjjei","hjibagacbhadfaefdjaeaebgi")) #false
print(canConstruct("bg","efjbdfbdgfjhhaiigfhbaejahgfbbg")) #true
print(canConstruct("aa","aab")) #true
print(canConstruct("aaq","husyakia"))
