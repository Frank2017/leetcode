class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def judge(num):
            t = num
            while t > 0:
                if t % 10 != 0:
                    if num % (t % 10) == 0:
                        t /= 10
                    else:
                        break
                else:
                    return False
            if t > 0:
                return False
            else:
                return True

        a = [0] * (right - left + 1)
        for i in range(len(a)):
            if i + left != 0:
                if a[i] == 0:
                    if i + left < 10 and i + left > 0:
                        a[i] = 1
                    else:
                        if judge(i + left):
                            a[i] = 1
                            k = 1
                            while (i + left) * k <= left:
                                a[(i + left) * k - left] = 1
                                k += 1
                                pass
                            pass
                        pass
                    pass
                pass
            pass
        res = []
        for i in range(len(a)):
            if a[i] == 1:
               res.append(i + left)
        return res

if __name__ == '__main__':
    Solution().selfDividingNumbers(24,66)