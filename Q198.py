class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        len_n = len(nums)
        rob_amount = [nums[0], max([nums[0],nums[1]])]
        for i in range(2, len_n):
            if nums[i] + rob_amount[i-2] > rob_amount[i - 1]:
                rob_amount.append(nums[i] + rob_amount[i-2])
            else:
                rob_amount.append(rob_amount[i-1])
        return rob_amount[-1]



if __name__ == '__main__':
    print Solution().rob([2,1,1,2,2,1])