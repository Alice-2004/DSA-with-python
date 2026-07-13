class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1]*n for i in range(m)]
        def dfs(i, j):
            if i >= m or j >= n or i<0 or j<0 or obstacleGrid[i][j] == 1:
                return 0
            if i == m-1 and j == n-1:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = dfs(i+1, j) + dfs(i, j+1)
            return dp[i][j]
        return dfs(0,0)




