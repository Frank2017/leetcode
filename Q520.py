class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        wC = word.upper()
        wL = word.lower()
        wB = word.capitalize()

        if word in [wC, wB, wL]:
            return True
        else:
            return False


if __name__ == '__main__':
    Solution().detectCapitalUse('USA')