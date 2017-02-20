import numpy as np
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
        if self.primer[area]:
            return [area, 1]
        L = int(math.sqrt(area))
        while L <= area:
            W = area / L
            if W > math.floor(W):
                L += 1
            else:
                W = int(W)
                return [L, W] if L > W else [W, L]
    pass


if __name__ == "__main__":
    area = 1
    # print(np.ones((1, 3)).astype(int).reshape(3))
    # print(int(math.sqrt(5)))
    print(Solution().constructRectangle(area))