class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        strsum = sum(map(lambda x:ord(x), s1)) + sum(map(lambda x:ord(x), s2))
        len1 = len(s1)
        len2 = len(s2)
        memo = [[strsum] * (len1 + 1),[strsum] * (len1 + 1)]
        for i in range(1, len2+1):
            for j in range(1, len1+1):
                if s1[j-1] == s2[i-1]:
                    memo[(i-1) % 2][j] = memo[(i-2)%2][j-1] - 2 * ord(s1[j-1])
                else:
                    memo[(i-1) % 2][j] = min([memo[(i-1)%2][j-1], memo[(i-2)%2][j]])
        return memo[(len2+1)%2][len1]


if __name__ == '__main__':
    # str1 = "delete"
    # str2 = "leet"
    # print Solution().minimumDeleteSum(str1, str2)
    # pass

    a = [[[0] * 3]for _ in range(2)]
    a[0][0][0] = 1
    print a