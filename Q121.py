class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if len(prices) == 0:
            return profit
        score = [prices[0]]
        for i in range(1,len(prices)):
            if (prices[i] - score[i-1]) > 0:
                score.append(score[i-1])
                if prices[i] - score[i] > profit:
                    profit = prices[i] - score[i]
            else:
                score.append(prices[i])
        return profit

if __name__ == '__main__':
    print Solution().maxProfit([1,2])