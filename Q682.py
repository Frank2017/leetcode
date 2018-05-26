class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for i in range(len(ops)):
            if str(ops[i]).upper() == 'C':
                stack.pop(-1)
            elif str(ops[i]).upper() == 'D':
                stack.append(stack[-1] * 2)
            elif ops[i] == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(ops[i]))
        return sum(stack)


if __name__ == '__main__':
    # arr = ["5","2","C","D","+"]
    # arr = ["5","-2","4","C","D","9","+","+"]
    arr = ["36","28","70","65","C","+","33","-46","84","C"]
    print Solution().calPoints(arr)