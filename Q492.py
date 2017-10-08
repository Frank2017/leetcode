import numpy as np
import time
import math


class Solution(object):
    MAX = 10000000
    primer = np.ones((1, MAX + 1)).astype(int).reshape(MAX + 1)

    def __init__(self):
        # 建立素数表
        self.primer[0] = self.primer[1] = 0
        for i in list(range(3, self.MAX+1)):
            self.primer[i] = 0 if i % 2 == 0 else 1
        t = int(math.sqrt(self.MAX))
        for i in list(range(3, t)):
            if self.primer[i]:
                j = i * i
                while j < (self.MAX + 1):
                    self.primer[j] = 0
                    j += 2*i
    pass

    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        L = int(math.sqrt(area))
        while L <= area:
            W = int(area / L)
            if L * W == area:
                return [L, W] if L >= W else [W, L]
            if L * W != area:
                L += 1


    pass


if __name__ == "__main__":
    area = 1
    st = time.time()
    print(Solution().constructRectangle(area))
    en = time.time()
    print(en - st)