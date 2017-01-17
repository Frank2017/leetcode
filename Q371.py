class Solution(object):
    def getSum(self, a, b):
        """
        :param a: int
        :param b: int
        :return: int
        """
        s = a ^ b
        c = (a & b) << 1
        while (0 != c):
            temp = s
            s = temp ^ c
            c = (temp & c) << 1
        return s
        pass

if __name__ == '__main__':
    print Solution().getSum(-1, 1)