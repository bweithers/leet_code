class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if not grid: return
        
        m = len(grid)
        n = len(grid[0])
        
        # print(m,n)
        
        flat_copy = []
        for row in grid:
            for x in row:
                flat_copy.append(x)
        # print(flat_copy)
        flat2 = [None for _ in flat_copy]
        
        for i,x in enumerate(flat_copy): flat2[(i+k)%len(flat_copy)] = x
        # print(flat2)
        
        grid2 = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(flat2[i*n+j])
            grid2.append(row)
        
        return grid2