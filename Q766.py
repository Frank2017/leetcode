class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(n):
            a = 0
            b = i
            while a < m-1 and b < n-1:
                if matrix[a][b] != matrix[a + 1][b + 1]:
                    return False
                a += 1
                b += 1
        for i in range(1, m):
            a = i
            b = 0
            while a < m - 1 and b < n-1:
                if matrix[a][b] != matrix[a + 1][b + 1]:
                    return False
                a += 1
                b += 1
        return True


if __name__ == '__main__':
    a = [[1,2],[2,2]]
    print(Solution().isToeplitzMatrix(a))