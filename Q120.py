class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        row = len(triangle)
        for i in range(row-2,-1,-1):
            col = len(triangle[i])
            for j in range(col):
                triangle[i][j] += min([triangle[i+1][j], triangle[i+1][j+1]])
        return triangle[0][0]


if __name__ == '__main__':
    tri = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print Solution().minimumTotal(tri)