class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ans = [[]]
        for s in S:
            n = len(ans)
            if s.isalpha():
                for i in range(n):
                    ans.append(ans[i][:])
                    ans[i].append(s.upper())
                    ans[n + i].append(s.lower())
            else:
                for i in range(n):
                    ans[i].append(s)
        return map("".join, ans)
if __name__ == '__main__':
    print(Solution().letterCasePermutation('a1b2'))