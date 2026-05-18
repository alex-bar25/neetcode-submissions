class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        rowCount = [0] * len(grid)
        colCount = [0] * len(grid[0])
        servers = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    rowCount[r] += 1 
                    colCount[c] += 1

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    if rowCount[r] > 1 or colCount[c] > 1:
                        servers += 1

        return servers