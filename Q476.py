# coding:utf-8
import math


class Solution(object):
    def findComplement(self, num):
        """
        :param num: int
        :return:  int
        """
        m = math.floor(math.log(num, 2)) + 1
        # n代表去掉前导0后，与num同位数的全1表示的10进制数
        n = 2 ** m - 1
        num ^= int(n)
        return num


if __name__ == '__main__':
    print (Solution().findComplement(5))
