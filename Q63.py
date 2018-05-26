class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        if row == 0:
            return 0
        col = len(obstacleGrid[0])
        memo = [([0] * col) for _ in range(row)]
        flag = False
        for i in range(0, col):
            if obstacleGrid[0][i] != 1:
                if flag:
                    memo[0][i] = 0
                else:
                    memo[0][i] = 1
            else:
                memo[0][i] = 0
                flag = True
        flag = False
        for j in range(0, row):
            if obstacleGrid[j][0] != 1:
                if flag:
                    memo[0][i] = 0
                else:
                    memo[j][0] = 1
            else:
                flag = True
                memo[j][0] = 0
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 1:
                    memo[i][j] = 0
                else:
                    memo[i][j] = memo[i-1][j] + memo[i][j-1]
        return memo[row-1][col-1]



if __name__ == '__main__':
    # d = [[0,0,0],
    #     [0,1,0],
    #     [0,0,0]]
    d =[[1,0]]
    print Solution().uniquePathsWithObstacles(d)