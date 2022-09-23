"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the
same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on.
Replace the color of all of the aforementioned pixels with color.
Return the modified image after performing the flood fill.

Input: image = [[1,1,1],
                [1,1,0],
                [1,0,1]],
sr = 1, sc = 1, color = 2
Output: [[2,2,2],
         [2,2,0],
         [2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1), all pixels connected by a path of the same color as the starting pixel are
colored with the new color.
Note the bottom corner position (2,2) is not colored 2, because it is not 4-directionally connected to the starting pixel (1,1).

Base cases:
reach top border
reach bottom border
reach left border
reach right border
when actual cell is already colored
when actual cell has dif color from what we replace. image[1][2] = 0, but we are replacing pixel 1. image[i][j]!=old color

Time complexity: O(n*m)
Space complexity: O(n*m) implicit call stack.
"""
def dfs_recursion(image,i,j,old_col,new_col):
    n = len(image)
    m = len(image[0])

#base case - do nothing
    if i < 0 or i >= n or j < 0 or j>=m or image[i][j]!=old_col:
        return image

    else:
        image[i][j] = new_col
        dfs_recursion(image,i,j-1,old_col,new_col)
        dfs_recursion(image,i,j+1,old_col,new_col)
        dfs_recursion(image,i+1,j,old_col,new_col)
        dfs_recursion(image,i-1,j,old_col,new_col)

def flood_fill(image,i,j,new_col):

    old_col = image[i][j]
    if old_col == new_col:
        return image
    dfs_recursion(image,i,j,old_col,new_col)  # call recursive function starting with i,j

    return image

print(flood_fill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))
print(flood_fill([[0,0,0],[0,0,0]],0,0,0))
