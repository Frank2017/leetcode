#coding=utf-8
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        lenNum = len(nums)
        # 记录最长的递增序列长度
        LIS = [1] * lenNum
        # 记录当前位置对应的序列个数
        res = [1] * lenNum
        maxN = -1
        sumN = 0
        for i in range(lenNum):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    # 此时序列长度有更改
                    if LIS[i] < LIS[j] + 1:
                        LIS[i] = LIS[j] + 1
                        res[i] = res[j]
                    # 若序列长度和ｊ一样，则需要记录当前与长度一样的个数
                    elif LIS[i] == LIS[j] + 1:
                        res[i] += res[j]
            if LIS[i] > maxN:
                maxN = LIS[i]
        for i in range(lenNum):
            if LIS[i] == maxN:
                sumN += res[i]

        return sumN


if __name__ == '__main__':
    s = [1,3,5,4,7]
    print Solution().findNumberOfLIS(s)
