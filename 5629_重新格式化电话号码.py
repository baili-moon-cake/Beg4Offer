class Solution:
    def reformatNumber(self, number: str) -> str:
        char_list = []
        for char in number:
            if char == ' ' or char == '-':
                continue
            char_list.append(char)
        
        n = len(char_list)
        ret_str = ''
        divisor, remains = n//3, n%3
        if remains == 1:
            divisor -= 1
        for idx in range(divisor):
            ret_str += ''.join(char_list[idx*3:(idx+1)*3])
            ret_str += '-'
        char_list = char_list[3*divisor:]
        n = len(char_list)        
        if n <= 3:
            ret_str += ''.join(char_list)
        elif n == 4:
            ret_str += ''.join(char_list[:2])+'-'+''.join(char_list[2:])
        if ret_str.endswith('-'):
            ret_str = ret_str[:-1]
        return ret_str


sol = Solution()
inp = "1-23-45 67"
ans = sol.reformatNumber(inp)
print(ans)

