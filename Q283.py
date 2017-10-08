class Solution(object):
    def moveZeros(self, nums):
        nonezero = -1
        cur = 0
        for i in range(len(nums)):
            if nums[cur] != 0:
                nonezero += 1
                if nonezero != cur:
                    nums[nonezero] = nums[cur]
                    nums[cur] = 0
            cur += 1
        return nums


if __name__ == '__main__':
    arr = [0, 2, 0, 3, 12, 0]
    # ls = [x for x in arr if x == 0]
    # er = [x for x in arr if x != 0]
    # arr = er + ls
    # print arr
    print (Solution().moveZeros(arr))