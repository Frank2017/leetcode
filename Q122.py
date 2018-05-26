class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_p = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_p += (prices[i] - prices[i-1])
        return max_p


if __name__ == '__main__':
    print Solution().maxProfit([])