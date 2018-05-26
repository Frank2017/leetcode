class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        sums = 0
        print nums
        for i in range(0, len(nums), 2):
            sums += nums[i]
        return sums


if __name__ == '__main__':
    arr = [1,2,3,4]
    print Solution().arrayPairSum(arr)