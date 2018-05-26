class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        lenS = len(s)
        if lenS == 0 or int(s[0]) == 0:
            return 0
        memo = [1,1]
        for i in range(1, lenS):
            # 此处说的是，若当前位和其前一位可以构成满足条件的２位数，他的拆解方式有两种，一种是将当前为拆解为单个数字
            # 另一种是将当前位和前一位组合组成一个数字，所以当前memo值是紧挨的前两个memo值加和
            if 11 <= int(s[i-1:i+1]) <= 19 or 21 <= int(s[i-1:i+1]) <= 26:
                memo.append(memo[i] + memo[i-1])
            # 此时当前位是０，他不能单独拆解，只能和前位结合，所以当前memo值是紧挨的倒数第二个memo的值
            elif int(s[i-1:i+1]) == 10 or int(s[i-1:i+1]) == 20:
                memo.append(memo[i-1])
            # 此时当前位不能和前位结合，只能单独拆解，所以当前的memo值是紧挨的倒数第一个memo值
            elif s[i] != '0':
                memo.append(memo[i])
            # 若当前位为０且不能与前位结合，则此时无法拆解，返回０
            else:
                return 0
        return memo[-1]

if __name__ == '__main__':
    print Solution().numDecodings('1000')
