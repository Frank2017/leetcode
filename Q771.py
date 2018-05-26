class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(map(J.count, S))


if __name__ == '__main__':
    J = 'z'
    S = 'zZZ'
    print(Solution().numJewelsInStones(J,S))