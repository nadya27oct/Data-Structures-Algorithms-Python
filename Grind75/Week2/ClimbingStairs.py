"""
70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

n=1, 1
n=2, 1+1 or 2
n=3, 1+1+1 or 2+1 or 1+2 = 3 = f(1) + f(2)
n=4, 1+1+1+1 or 2+1+1 or 1+1+2 or 1+2+1 or 2+2 = 5 = f(3) + f(2)
n=5, 1+1+1+1+1 or 2+1+1+1 or  1+2+1+1 or 1+1+2+1 or 1+1+1+2 or 2+2+1 or 2+1+2 or 1+2+2 = 8 = f(4) + f(3)

stepscount(5):
memoization(5,memo={3:3,4:5,5:8}) -> 8
memoization(4,memo={3:3,4:5}) + memoization(3,memo={}) -> 5 + 3
memoization(3,memo={3:3}) + memoization(2,memo={}) -> 3 + 2
memoization(2,memo={}) + memoization(1,memo={}) --> 2 + 1

O(2*n) = 0(n) -> Time and Space complexity
We have to call the function at each of these nodes.
            f(5)
         f(4)   f(3)
     f(3)   f(2)
  f(2)  f(1)


"""

def StepsCount(n):

    memo = dict()

    def Memoization(n,memo):

        if n in memo:
            return memo[n] # If we already calculated stepscount(2), access from memo hash.

        else: #Otherwise save function value in memo hash.
            if n<=2:
                return n
            else:
                memo[n] = Memoization(n-1,memo) + Memoization(n-2,memo)

            return memo[n]

    return Memoization(n,memo)

print(StepsCount(6))
print(StepsCount(5))
print(StepsCount(38))

def climbStairs(n):

    if n <= 2:
        return n

    else:
        return climbStairs(n-2) + climbStairs(n-1)


print(climbStairs(6))
print(climbStairs(5))
print(climbStairs(38))
