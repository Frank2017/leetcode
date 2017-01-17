class Solution(object):
    def canWinNim(self, n):
        """
        :param n:int
        :return: bool   win or not
        """
        return False if 0 == n % 4 else True


if __name__ == '__main__':
    print (Solution().canWinNim(11))