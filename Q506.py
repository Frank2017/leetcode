class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        arr = sorted(enumerate(nums), key=lambda x:x[1])
        result = list(range(0,len(nums)))
        medal = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        print(arr)
        lena = len(arr)
        for i in list(range(lena)):
            if i <= (lena - 3 - 1):
                result[arr[i][0]] = (lena - i).__str__()
            else:
                result[arr[i][0]] = medal[lena - i - 1]
        return result


if __name__ == '__main__':
    arr = [1,2,3,4,5]
    Solution().findRelativeRanks(arr)