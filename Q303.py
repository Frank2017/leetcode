import numpy as np

class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.acu = [0]
        for n in nums:
            self.acu.append(self.acu[-1] + n)


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.acu[j+1] - self.acu[i]

if __name__ == '__main__':
    arr = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(arr)
    print obj.sumRange(0,4)



        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # param_1 = obj.sumRange(i,j)