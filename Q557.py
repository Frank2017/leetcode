class Solution(object):
    def reversestr(self, str):
        return str[::-1]
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = s.split(' ')
        arr = map(lambda x:self.reversestr(x), arr)
        return ' '.join(arr)


if __name__ == '__main__':
    s = r"Let's take LeetCode contest"
    print Solution().reverseWords(s)