class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return
        # keep track of the cells we have already visited, a cell can only be in one island
        seen,max_size = set(),0
        
        def dfs(x,y):
            #print(x,y)
            if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid) or not grid[y][x]: return 0
            if (x,y) in seen: return 0
            seen.add((x,y))
            return 1+sum([dfs(x-1,y),dfs(x+1,y),dfs(x,y+1),dfs(x,y-1)])
        
        # iterate over the grid
        for y,row in enumerate(grid):
            for x,cell in enumerate(row):
                if cell and cell not in seen:
                    # get_island_size
                    size = dfs(x,y)
                    max_size = max(max_size,size)
                    
        return max_size