class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        wcnt = 0
        prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]
        for i in range(L, R+1):
            cnt = bin(i).count('1')
            if cnt in prime:
                wcnt += 1
        return wcnt


if __name__ == '__main__':
    print(Solution().countPrimeSetBits(849331, 857572))
