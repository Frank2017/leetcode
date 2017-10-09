# coding=utf-8
import numpy as np
import math
import time


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w = int(math.sqrt(area))
        while area % w != 0:
            w -= 1
        return [int(area/w), w]
    pass


if __name__ == "__main__":
    area = 1
    # print(np.ones((1, 3)).astype(int).reshape(3))
    # print(int(math.sqrt(5)))
    st = time.time()
    print(Solution().constructRectangle(area))
    en = time.time()
    print (en - st)