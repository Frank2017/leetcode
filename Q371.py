class Solution(object):
    def getSum(self, a, b):
        """
        :param a: int
        :param b: int
        :return: int
        """
        # if abs(a) == abs(b) and a * b < 0:
        #     return 0
        # s = a ^ b
        # # print(bin(a))
        # # print(bin(b))
        # # print("s=>",s)
        # c = (a & b) << 1
        # # print("c=>",c)
        # cnt = 0
        # while (0 != c):
        #     temp = s
        #     print("temp=>",temp)
        #     s = temp ^ c
        #     print("sloop=>",s)
        #     c = (temp & c) << 1
        #     print("cloop=>",c)
        #     if cnt == 10:
        #         exit()
        #     cnt += 1
        # return s
        while(b):
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a
        pass

if __name__ == '__main__':
    print (Solution().getSum(-14, 13))