class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        else:
            for s in range(len(A)):
                if all(A[(s+i) % len(A)] == B[i] for i in xrange(len(A))):
                    return True
            else:
                return False
