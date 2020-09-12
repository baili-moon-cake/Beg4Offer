class Solution:
    def hanota(self, A, B, C):
        """
        Do not return anything, modify C in-place instead.
        """
        if len(A) == 0:
            return
        elif len(A) == 1:
            C.append(A.pop(-1))
            return
        elif len(A) == 2:
            B.append(A.pop(-1))
            C.append(A.pop(-1))
            C.append(B.pop(-1))
            return
        self.corefunc(len(A), A, B, C)

    def corefunc(self, n, src_list, agency_list, dst_list):
        if n == 2:
            agency_list.append(src_list.pop(-1))
            dst_list.append(src_list.pop(-1))
            dst_list.append(agency_list.pop(-1))
            return
        self.corefunc(n-1, src_list, dst_list, agency_list)
        dst_list.append(src_list.pop(-1))
        self.corefunc(n-1, agency_list, src_list, dst_list)


sol = Solution()
sol.hanota([4,3,2,1,0], [], [])