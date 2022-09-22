"""
In M x N grid, determine number of ways to travel from start to end.
Can only travel down or right but not diagonal.
1x1 grid, there is only 1 way.
2x2 grid, there are 2 ways. [Down,Right and Right,Down]
2x0 grid, no way.
2x3 grid, there are 3 ways:
Down,Right,Right...coordinates are (2,3) (1,3) (1,2) (1,1)
Right,Down,Right...coordinates are (2,3) (2,2) (1,2) (1,1)
Right,Right,Down...coordinates are (2,3) (2,2) (2,1) (1,1)

2 x 3 grid. 2 rows and 3 columns

Picture each coordinate in a tree with start point as parent and each down and right as child nodes.
(2,3)
Down ---> (1,3) --> Down --> (0,3) ...End of route. Leaf Node. Base Case
                --> Right--> (1,2)--> Down -->(0,2)..Leaf Node
                                  --> Right-->(1,1)
Right --> (2,2)--> Down --> (1,2)--> Down -->(0,2)
                                 --> Right-->(1,1)
               --> Right--> (2,1)--> Down -->(1,1)
                                 --> Right-->(2,0)
1x1 grid - There is exactly one way to travel from start to end in 1x1 grid.
Anything with 0xn or mx0 is another base case. There is no way to go from start to end.
(2,1) == (1,2)

                   down    (3,2)  right
            (2,2)                          (3,1)
    (1,2)            (2,1)           (2,1)      (3,0)
(0,2)   (1,1)     (1,1)  (2,0)    (1,1)  (2,0)
"""

def gridTraveler(m,n):

    if m == 1 and n == 1:
        return 1

    if m==0 or n == 0:
        return 0
        
    return gridTraveler(m-1,n) + gridTraveler(m,n-1)
# Recursively get the sum of ways by going down and going right.
# If direction is down, reduce number of rows but keep column constant. If direction is right, keep row same and reduce column count.

print(gridTraveler(2,3))
print(gridTraveler(3,3))
print(gridTraveler(1,3))
print(gridTraveler(14,14))
"""
Time and space complexity for brute force recursive solution:
Time complexity - How many function calls? There are m+n levels in the tree until we reach base case
(when one of the arguments is zero). Ex:(2,3) (1,3) (1,2) (1,1) --> to 0,0.
O(2^(n+m))
Space complexity - Height of the tree. m+n levels --> O(m+n)
"""


#Memoization
cache = {}
def memoized_grid_traveler(m,n):

    key = (m,n)
    if key in cache:
        return cache[key]

    else:
        if m == 1 and n == 1:
            return 1
        if m == 0 or n == 0:
            return 0


        cache[key] = memoized_grid_traveler(m-1,n) + memoized_grid_traveler(m,n-1)
        return cache[key]


print(memoized_grid_traveler(3,2))
print(memoized_grid_traveler(14,14))
print(memoized_grid_traveler(4,3))
"""
What are the nodes that function has to travel through?
If grid traveler is (2,3), the only possible values in the tree are m = {0,1,2} and n={0,1,2,3}.
There are m*n possible combinations of nodes.
Time complexity: O(m*n)
Space complexity: O(m+n)
"""
