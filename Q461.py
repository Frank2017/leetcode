# coding=utf-8
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :param x: int
        :param y: int
        :return:  int
        """
        z = x ^ y
        # 下述代码可以快速求解x，y异或结果中1的个数
        cnt = 0
        while z:
            cnt += 1
            z &= (z - 1)
        return cnt


if __name__ == "__main__":
    s = Solution()
    print s.hammingDistance(1, 1)
