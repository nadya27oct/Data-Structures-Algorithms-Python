"""
Write a function, minimum_island, that takes in a grid containing Ws and Ls.
W represents water and L represents land. The function should return the size of the smallest island.
An island is a vertically or horizontally connected region of land.
Start by iterating through grid[i][j]. Then use a helper function to compute island size when a coordinate = 'L' 
Keep track of visited 'L' coordinates.
Any coordinate that is out of bounds will not contribute to size. Return 0.
If coordinate = 'W', return 0 as they contribute nothing to size.
Otherwise add coordinate to visited and check if neighbors are part of the same island.

explore_size(grid,0,0,visited); return 0: no island.
when comparing min size, we want to compare for non 0 sizes.
"""

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

def minimum_island(grid):

    island_size = float('inf')
    visited = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = explore_size(grid,r,c,visited)
            if size > 0 and size < island_size:
                island_size = size

    return island_size

def explore_size(grid,r,c,visited):

    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
        return 0

    if grid[r][c] == 'W':
        return 0

    if (r,c) in visited:
        return 0

    visited.add((r,c))
    size = 1
    size += explore_size(grid,r-1,c,visited)
    size += explore_size(grid,r+1,c,visited)
    size += explore_size(grid,r,c-1,visited)
    size += explore_size(grid,r,c+1,visited)

    return size

test_0=minimum_island(grid) # -> 2
print(test_0)
