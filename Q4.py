class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            A = nums2
            B = nums1
            m = len2
            n = len1
        else:
            A = nums1
            B = nums2
            m = len1
            n = len2
        imin = 0
        imax = m
        half_len = (m+n+1) // 2
        while(imin <= imax):
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and j > 0 and A[i] < B[j-1]:
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                imax = i - 1
            else:
                if i == 0:
                    left_max = B[j-1]
                elif j == 0:
                    left_max = A[i-1]
                else:
                    left_max = max(A[i-1], B[j-1])
                if (m+n) % 2 == 1:
                    return left_max * 1.0
                if i == m:
                    right_min = B[j]
                elif j == n:
                    right_min = A[i]
                else:
                    right_min = min(A[i], B[j])
                return (left_max + right_min) / 2.0


if __name__ == '__main__':
    a = [1,2,3,4]
    b = [6,8,9,10]

    print(Solution().findMedianSortedArrays(a, b))