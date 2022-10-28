"""
67. Add Binary
Given two binary strings a and b, return their sum as a binary string.

Input: a = "11", b = "1"
Output: "100"

Input: a = "1010", b = "1011"
Output: "10101"

 1         111
 11         1010      1100
  1 +       1111 +       1 +
100        10001      1101

0+0 = 0-->0, carry = 0
1+0 = 1-->1, carry = 0
1+1 = 2-->0, carry = 1
1+1+1 = 3->1, carry = 1
retained value -> addition%2 and carry value is addition>1

m = len(a), n = len(b), x = max(m,n)
Time: 0(m+n+x) = 0(n)
Space: O(x) = 0(n)
"""

def addBinary(a,b):

    result = []
    carry = 0

    i = len(a)-1
    j = len(b)-1

    while i >= 0 or j >=0:
        total = carry
        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1
        str_to_add = str(total % 2)
        result.append(str_to_add)
        carry = 1 if total > 1 else 0

    if carry != 0:
        return str(carry) + ''.join(result[::-1])
        
    return ''.join(result[::-1])

print(addBinary("11","1"))
print(addBinary("1010","1011"))
print(addBinary("10","0"))
