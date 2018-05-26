class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost += [0]
        clen = len(cost)
        for i in range(2,clen):
            cost[i] = min([cost[i-1], cost[i-2]]) + cost[i]
        return cost[clen-1]

if __name__ == '__main__':
    arr = [1, 100]

    print Solution().minCostClimbingStairs(arr)