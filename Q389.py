class Solution(object):
    def findTheDifference(self, s, t):
        """
        :param s: str
        :param t: str
        :return: str
        """
        if s != "":
            slist = sorted(list(s))
            tlist = sorted(list(t))
            for i in range(0,len(slist)):
                if slist[i] != tlist[i]:
                    return tlist[i]
            if i == len(slist) - 1:
                return tlist[len(tlist) - 1]
        else:
            return t
        pass


if __name__ == '__main__':
    ss = ""
    tt = "a"
    print Solution().findTheDifference(ss, tt)