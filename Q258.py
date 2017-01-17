class Solution(object):
    def addDigits(self, num):
        """
        :param num: int
        :return: int
        """
        while num >= 10:
            temp = num
            cnt = 0
            while temp > 0:
                cnt += temp % 10
                temp /= 10
            num = cnt
        return num
        # return 1 + (num - 1) % 9
        pass


if __name__ == '__main__':
    print (Solution().addDigits(7))