# coding:utf-8
import math


class Solution(object):
    def findDisappearNumbers(self, nums):
        """
        :param nums: list[int]
        :return: list[int]
        """
        # 时间复杂度O(n)，空间复杂度O（n）
        # n = len(nums)
        # cnt = []
        # for i in range(0, n):
        #     cnt.append(0)
        # for i in range(0, n):
        #     cnt[nums[i] - 1] += 1
        # result = []
        # for i in range(0, n):
        #     if 0 == cnt[i]:
        #         result.append(i+1)
        # return result
        # 时间复杂度O(n)，空间复杂度O(1)
        n = len(nums)
        for i in range(0, n):
            val = (nums[i]-1) if nums[i] > 0 else (-nums[i]-1)
            if nums[val] > 0:
                nums[val] = -nums[val]
        result = []
        for i in range(0, n):
            if nums[i] > 0:
                result.append(i + 1)
        return result
        pass


if __name__ == '__main__':
    # arr = [4, 3, 2, 7, 8, 2, 3, 1]
    arr = [1, 1, 2, 1, 1, 1, 1, 1]
    print (Solution().findDisappearNumbers(arr))