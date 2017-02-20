class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len1 = len(nums)
        result = -1
        cnt = 0
        for i in list(range(len1)):
            if nums[i] == 1:
                cnt += 1
            else:
                if cnt > result:
                    result = cnt
                cnt = 0
        # 整个数组全部为1
        if cnt > result:
            result = cnt
        return result

if __name__ == "__main__":
    nums = [1]
    print(Solution().findMaxConsecutiveOnes(nums))