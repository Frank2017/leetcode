class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        len1 = len(findNums)
        len2 = len(nums)
        if nums == []:
            return []
        maxnum = max(nums)
        result = []
        for i in list(range(len1)):
            if findNums[i] == maxnum:
                result.append(-1)
            else:
                index = nums.index(findNums[i])
                if index == (len2 - 1):
                    result.append(-1)
                else:
                    flag = 0
                    for j in list(range(index + 1, len2)):
                        if nums[j] > findNums[i]:
                            result.append(nums[j])
                            flag = 1
                            break
                    if flag == 0:
                        result.append(-1)
        return result
        pass


if __name__ == "__main__":
    nums1 = []
    nums2 = []
    print(Solution().nextGreaterElement(nums1, nums2))
