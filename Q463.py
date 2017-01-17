class Solution(object):
    def islandPerimeter(self, grid):
        """
        :param grid: list[list[int]]
        :return: int  Perimeter
        """
        m = len(grid)
        n = len(grid[0])
        cnt = 0
        for i in range(0, m):
            for j in range(0, n):
                temp = 4
                if 1 == grid[i][j]:
                    if i - 1 >= 0:
                        if 1 == grid[i-1][j]:
                            temp -= 1
                    if j + 1 < n:
                        if 1 == grid[i][j+1]:
                            temp -= 1
                    if i + 1 < m:
                        if 1 == grid[i+1][j]:
                            temp -= 1
                    if j - 1 >= 0:
                        if 1 == grid[i][j-1]:
                            temp -= 1
                    cnt += temp
        return cnt


if __name__ == '__main__':
    # grid = [[0, 1, 0, 0],
    #         [1, 1, 1, 0],
    #         [0, 1, 0, 0],
    #         [1, 1, 0, 0]]
    grid = [[0, 1, 0, 0]]
    m = len(grid)
    n = len(grid[0])
    print m, n
    print Solution().islandPerimeter(grid)

