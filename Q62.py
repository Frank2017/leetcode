class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = [([0] * (n)) for _ in range(m)]
        for i in range(0, n):
            memo[0][i] = 1
        for j in range(0,m):
            memo[j][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                memo[i][j] = memo[i-1][j] + memo[i][j-1]
        return memo[m-1][n-1]


if __name__ == '__main__':
    print Solution().uniquePaths(1,2)
