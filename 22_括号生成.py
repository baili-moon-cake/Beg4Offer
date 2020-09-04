class Solution:
    def generateParenthesis(self, n: int):
        return list(self.generateParenthesisRecursively(n))
    def generateParenthesisRecursively(self, n: int):
        if n== 1:
            return {'()',}
        previous_ret = self.generateParenthesis(n-1)
        ret = set()
        for _str in previous_ret:
            for left_insert_idx in range(len(_str)):
                for right_insert_idx in range(left_insert_idx, len(_str)):
                    _new_str = _str[:left_insert_idx]+'('+_str[left_insert_idx:]
                    _new_str = _new_str[:right_insert_idx+1]+')'+_new_str[right_insert_idx+1:]
                    ret.add(_new_str)
        return ret

if __name__ == "__main__":
    solution = Solution()
    ans = solution.generateParenthesis(3)
    print(ans)