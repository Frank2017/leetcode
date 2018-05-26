class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        kinds = list(set(candies))
        divLen = len(candies) / 2
        sisterLen = len(kinds)
        return sisterLen if sisterLen < divLen else divLen

if __name__ == '__main__':
    arr = [0,1,2,3,4,5]
    print Solution().distributeCandies(arr)