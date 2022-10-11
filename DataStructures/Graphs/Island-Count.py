"""
Write a function, island_count, that takes in a grid containing Ws and Ls.
W represents water and L represents land.
The function should return the number of islands on the grid.
An island is a vertically or horizontally connected region of land.

Each coordinate is a node in a graph. Each node has 4 neighbors.
node = (i,j).
neighbors = (i+1,j)
            (i-1,j)
            (i,j+1)
            (i,j-1)
Iterate through each coordinate in grid.  If coordinate = L, travel to neighboring coordinates using helper function.
Helper function should return a boolean to indicate whether or not we are visiting a new node/coordinate.

Undirected graph problems need to keep track of already visited nodes to avoid infinite cycles.

Time complexity = O(r*c)
Space complexity = O(r*c)

explore(0,0,visited=set()); grid[0][0] == 'W'
explore(0,1,visited=set()); visited = [(0,1)];
    explore(1,1,[(0,1)]); grid[1][1] == 'L'; visited = [(0,1),(1,1)]
    explore(-1,1,[(0,1),(1,1)]); grid[-1][0] = out of bound; False
    explore(0,2,[(0,1),(1,1)]); grid[0][2] = out of bound; False
    explore(0,0,[(0,1),(1,1)]); grid[0][0] = W; False

"""

def island_count(grid):

    count = 0
    visited = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid,r,c,visited) == True:
                count +=1

    return count

def explore(grid,r,c,visited):

    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
        return False

    if grid[r][c] == 'W':
        return False

    if (r,c) in visited:
        return False
    visited.add((r,c))

    explore(grid,r+1,c,visited)
    explore(grid,r-1,c,visited)
    explore(grid,r,c+1,visited)
    explore(grid,r,c-1,visited)

    return True # Just explored a brand new island, so need to count it.

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

island_count(grid) # -> 3

grid = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]
island_count(grid) # -> 1
