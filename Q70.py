class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1]
        dp.append(1)
        for i in range(2,n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]


if __name__ == '__main__':
    print Solution().climbStairs(4)
    pass