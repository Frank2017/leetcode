import numpy as np
class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        maxLen = 0
        memo = [[0] * (len(A) + 1) for _ in range(2)]
        for i in range(len(B)):
            for j in range(1, len(A)+1):
                if B[i] == A[j-1]:
                    memo[i % 2][j] = memo[(i-1) % 2][j-1] + 1
                    if memo[i % 2][j] > maxLen:
                        maxLen = memo[i % 2][j]
                else:
                    memo[i % 2][j] = 0
        return maxLen

if __name__ == '__main__':
    A = [1, 2, 3, 2, 1, 2]
    B = [3, 2, 1, 2, 4, 7]

    print Solution().findLength(A, B)

