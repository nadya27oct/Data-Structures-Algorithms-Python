"""
409. Longest Palindrome
Given a string s which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

hash = {a:1,b:1,c:4,d:2}

string = "nursesrunhese"
hash={n:2,u:2,r:2,s:3,e:3,h:1}

string = "abcb", hash = {a:1,b:2,c:1}
palindrome = "bab" or "bcb"

string = "racecar"
hash={n:2,u:2,r:2,s:1,e:1}

string = "ccc", hash = {c:3}
"""

def longestPalindrome(s):

    hash = dict()
    for char in s:
        if char not in hash:
            hash[char] = 0
        hash[char] += 1

    pairs = 0
    single_letters = 0

    for char in hash:
        if hash[char] % 2 == 0:
            pairs += hash[char]
        else:
            if hash[char] > 1:
                pairs += hash[char] - 1
            single_letters += 1
    return pairs + 1 if single_letters >= 1 else pairs

str1 = longestPalindrome("abccccdd") # 7
str2 = longestPalindrome("abcbe") #3
str3 = longestPalindrome("ccc") #3
str4 = longestPalindrome("a") #1
