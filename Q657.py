class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        h = 0
        v = 0
        slen = len(moves)
        for i in range(slen):
            if moves[i].upper() == 'U':
                h += 1
                continue
            if moves[i].upper() == 'D':
                h -= 1
                continue
            if moves[i].upper() == 'L':
                v -= 1
                continue
            if moves[i].upper() == 'R':
                v += 1
                continue
        if h == 0 and v == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    m = "Ud"
    print Solution().judgeCircle(m)