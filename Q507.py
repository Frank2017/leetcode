import math
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        cnt = 1
        if num <= 1:
            return False

        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                cnt = cnt + i
                if i != int(num / i):
                    cnt += int(num / i)
        if cnt == num:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().checkPerfectNumber(1))