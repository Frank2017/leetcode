class Solution(object):
    def singleNumber(self, nums):
        """
        :param nums:
        :return:
        """
        result = 0
        for i in range(0, len(nums)):
            result ^= nums[i]
        return result


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 3, 4, 1]
    #test update
    print (Solution().singleNumber(arr))