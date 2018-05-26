class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = [nums[0]]
        for i in range(1,len(nums)):
            if memo[-1] + nums[i] > nums[i]:
                memo.append(memo[-1] + nums[i])
            else:
                memo.append(nums[i])
        return max(memo)


if __name__ == '__main__':
    print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
