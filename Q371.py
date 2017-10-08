class Solution(object):
    def getSum(self, a, b):
        """
        :param a: int
        :param b: int
        :return: int
        """
        MAX = 0x7FFFFFFF
        MIN = 0x80000000
        mask = 0xFFFFFFFF
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
            # print 'a = ', a
            # print 'b = ', b
        return a if a <= MAX else ~(a ^ mask)

        # # substract
        # while b != 0:
        #     borrow = ((~a) & b) & mask
        #     a = (a ^ b) & mask
        #     b = (borrow << 1) & mask
        # return a if a<=MAX else (~a ^ mask)
        pass

if __name__ == '__main__':
    print (Solution().getSum(2, -2))