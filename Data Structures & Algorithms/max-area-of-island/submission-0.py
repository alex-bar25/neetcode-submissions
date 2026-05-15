class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0

        # area of one islands
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c+ 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    currentArea = dfs(r, c)
                    maxArea = max(maxArea, currentArea)

        return maxArea