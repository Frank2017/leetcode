class Solution(object):
    def binsearch(self,numbers, st, en, target):
        if st > en:
            return -1
        mid = int((st + en) / 2)
        if numbers[mid] == target:
            return mid
        if numbers[mid] > target:
            return self.binsearch(numbers, st, mid - 1, target)
        if numbers[mid] < target:
            return self.binsearch(numbers, mid + 1, en, target)
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        lenn = len(numbers)
        for i in list(range(0, lenn)):
            if (target - numbers[i]) in numbers:
                j = self.binsearch(numbers, i+1, lenn-1,target-numbers[i])
                if i < j:
                    return [i+1, j+1]


if __name__ == "__main__":
    arr = [1, 2, 3, 4,4,9,56,90]
    target = 8
    print(Solution().twoSum(arr, target))