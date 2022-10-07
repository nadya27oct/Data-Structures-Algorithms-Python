"""
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

pow(2,3) = 2^3 = 2 * 2 * 2 = 3
pow(2.1,-4) = 1/(2.1^4) = 1/2.1 * 1/2.1 * 1/2.1 * 1/2.1= 0.05142
pow(4.768,0) = 1

n: is an integer
x: is a float

myPow(2,4)
abs_n = 4
result = fastPow(2,4)
half = fastPow(2,2)
abs_n = 4
fastPow(2,2) * fastPow(2,2)
fastPow(2,2) = fastPow(2,1) * fastPow(2,1) = 2 * 2 = 4

"""

def myPow(x,n):

    if n == 0:
        return 1

    abs_n = abs(n)

    result = fastPow(x,abs_n)

    if n > 0:
        return result

    elif n < 0:
        return 1.0/result

def fastPow(x,n):
    if n == 1:
        return x

    half = fastPow(x,n//2)

    if n%2==0:
        return half * half
    else:
        return half * half * x

print(myPow(3,4))
print(myPow(3,-4))
print(myPow(4.7689,0))
print(myPow(0.99999,948688))
print(myPow(2.7,-3))
print(myPow(0.00001,2147483647))
print(myPow(2.00000,-268435456))
