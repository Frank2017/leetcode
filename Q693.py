class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n, cur = divmod(n, 2)
        while n > 0:
            if cur == n % 2:
                return False
            else:
                n, cur = divmod(n, 2)
        return True



if __name__ == '__main__':
    print(Solution().hasAlternatingBits(10))