class Solution(object):
    def reverseString(self, s):
        """
        :param s: str
        :return: str
        """
        return s[::-1]

if __name__ == '__main__':
    s = "hello"
    print Solution().reverseString(s)