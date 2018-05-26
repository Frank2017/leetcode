class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = [[0] * (n+1) for _ in range(m+1)]
        def count01(s):
            return sum(1 for c in s if c =='0'), sum(1 for c in s if c =='1')


        for z,o in [count01(s) for s in strs]:
            for i in range(m,-1,-1):
                for j in range(n,-1,-1):
                    if i >= z and j >= o:

                        memo[i][j] = max([1+memo[i-z][j-o], memo[i][j]])

        return memo[m][n]


if __name__ == '__main__':
    s = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    print Solution().findMaxForm(s, m, n)
