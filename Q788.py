class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        ans = 0
        for s in range(1,N+1):
            S = str(s)
            ans += (all(d not in '347' for d in S) and
            any(d in '2569' for d in S))
        return ans

if __name__ == '__main__':
    print(Solution().rotatedDigits(12))