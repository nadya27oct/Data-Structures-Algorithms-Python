"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()[]{}"
Output: true

Example 2:
Input: s = "(]"
Output: false

Example 3:
Input: s = "()"
Output: true

Time complexity: 0(n) - Only looping through string once.
Space complexity: O(n) - Brackets is O(3) - constant.
But stack might be n elements in worst case where s="{{{{{"

"""

def is_valid(string):

    if len(string) % 2 == 0:
        brackets = {')':'(','}':'{',']':'['}
        s = list(string)

        stack = []
        for i in range(len(s)):
            if s[i] in brackets.values():
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False

                if brackets[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0

    else:
        return False

example1 = "()[]{}"
print(is_valid(example1))
example2 = "(]"
print(is_valid(example2))
example3 = "()"
print(is_valid(example3))
example4 = "(((((())))))"
print(is_valid(example4))
example5= "(((((((()"
print(is_valid(example5))
print(is_valid("]"))
print(is_valid("([}}])"))
print(is_valid("}]"))
