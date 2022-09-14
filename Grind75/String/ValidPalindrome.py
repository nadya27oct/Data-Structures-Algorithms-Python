"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

recursion:
s = 'kayak'
base case = list is empty or list = 1.
otherwise recursively call list[1] == list[-1]
list.pop()
list.pop()
s[0] == s[4]
s[1] == s[3]
s[2] == s[2]
"""

def isPalindrome(string):

    if len(string) == 0:
        return True

    only_alpha = ''
    for s in string:
        if s.isalnum():
            if s.isupper():
                only_alpha += s.lower()
            else:
                only_alpha += s

    left = 0
    right = len(only_alpha)-1
    for i in range(left,right+1):
        if left <= right:
            if only_alpha[left] != only_alpha[right]:
                return False
            else:
                left +=1
                right -=1
    return True

# s='kayak is heavy'
# print(isPalindrome(s))
# print(isPalindrome('deed'))
# print(isPalindrome('a '))
# print(isPalindrome(' '))
# print(isPalindrome("A man, a plan, a canal: Panama"))
# print(isPalindrome("race a car"))

def check_if_palindrome(string):

     only_alpha = ''.join(filter(lambda s: s.isalnum(),string))
     only_alpha = only_alpha.lower()

     return recursion(only_alpha)

def recursion(s):
    if len(s) <= 1:
        return True

    first_char = s[0]
    last_char = s[-1]

    if first_char==last_char:
        return recursion(s[1:-1]) #returning function calls
    else:
        return False


print(check_if_palindrome("race a car"))
print(check_if_palindrome("A man, a plan, a canal: Panama"))
print(check_if_palindrome("Ed, I saw Harpo Marx ram Oprah W. aside."))
print(check_if_palindrome("Are we not pure? Irony dooms a man a prisoner up to new era."))
