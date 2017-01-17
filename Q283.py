class Solution(object):
    def moveZeros(self, nums):
        # for i in range(1, len(nums)):
        #     for j in range(i, 0, -1):
        #         if 0 == nums[j - 1]:
        #             temp = nums[j - 1]
        #             nums[j - 1] = nums[j]
        #             nums[j] = temp
        # return nums
        ls = [x for x in nums if x == 0]
        er = [x for x in nums if x != 0]
        nums = er + ls
        return nums


if __name__ == '__main__':
    arr = [0, 2, 0, 3, 12, 0]
    # ls = [x for x in arr if x == 0]
    # er = [x for x in arr if x != 0]
    # arr = er + ls
    # print arr
    print Solution().moveZeros(arr)