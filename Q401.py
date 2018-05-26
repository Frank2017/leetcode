class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        def cntone(n):
            return bin(n).count('1')
            pass
        res = []
        hdict = [0] * 12
        mdict = [0] * 60
        for i in range(0,12):
            hdict[i] = cntone(i)
        for i in range(0, 60):
            mdict[i] = cntone(i)
        for i in range(len(hdict)):
            for j in range(len(mdict)):
                if hdict[i] + mdict[j] == num:
                    res.append("%d:%02d" % (i,j))
        return res


if __name__ == '__main__':
    print(Solution().readBinaryWatch(1))
