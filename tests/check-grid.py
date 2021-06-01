 
"""
You are designing a new point and click adventure game. In order to appeal to a broader set of players, you decide to include some logic puzzles in addition to a wide variety of inventory-based puzzles. The first puzzle you settle on is 'sub-Sudoku'.

Your job is to write a function that, given an NxN grid, returns true if every row and column contains the numbers 1..N

The grid can contain any integer, not just 1..N, and not just positive.

Examples:

[[1, 2, 3],
 [2, 3, 1],
 [3, 1, 2]]         -> True

[[1, 2, 3],
 [1, 2, 3],
 [1, 2, 3]]        -> False

[[1000, -1000, 6],
 [   2,     3, 1],
 [   3,     1, 2]] -> False
"""

grid1 = [[1,2,3],[2,3,1],[3,1,2]]
grid2 = [[1,2,3],[1,2,3],[1,2,3]]
grid3 = [[1000,-1000,6],[2,3,1],[3,1,2]]
grid4 = [[1, 2, 3, 4, 5],[1, 2, 3, 4, 5],[1, 2, 3, 4, 5],[1, 2, 3, 4, 5],[1, 2, 3, 4, 5]]

def check_grid(grid):
    legal = set()

    size = len(grid)
    rows_ok = True
    cols_ok = True
    
    # rows
    for i in range(0, size):    
        for n in range(1, len(grid[0])+1):
            legal.add(n)
        
        for n in grid[i]:
            if n in legal:
                legal.remove(n)
                
        if len(legal) == 0:
            rows_ok = False
                
    # cols
    for y in range(0, size):
        for n in range(1, len(grid[0])+1):
            legal.add(n)
        
        for x in range(0, size):
            
            #print("x-y: {}".format(grid[x][y]))
            if grid[x][y] in legal:
                legal.remove(grid[x][y])
                
                #print("legal: {}".format(len(legal)))
        
        if len(legal) == 0:
            cols_ok = False    
    
    if cols_ok == True and cols_ok == True:
        return False
    else:
        return True

#print(check_grid(grid1))
#print(check_grid(grid2))
#print(check_grid(grid3))
print(check_grid(grid4))