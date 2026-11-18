
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])

        count = 0

        def dfs(i, j):

            if (i < 0 or i >= m or
                j < 0 or j >= n or
                grid[i][j] == "0"):
                return

            grid[i][j] = "0"

            dfs(i + 1, j)  # Down
            dfs(i - 1, j)  # Up
            dfs(i, j + 1)  # Right
            dfs(i, j - 1)  # Left

        for i in range(m):
            for j in range(n):

                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count
