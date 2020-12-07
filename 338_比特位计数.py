from typing import List

class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0,]
        ret = []
        cnt_bits = (num).bit_length() - 1
        cnt_bits_copy = cnt_bits
        while(cnt_bits):
            ret += [1,] + [1+v for v in ret]
            cnt_bits -= 1
        ret.append(1)
        ret += [1+ret[idx] for idx in range(num-2**cnt_bits_copy)]
        return [0,] + ret

sol = Solution()
ans = sol.countBits(0)
print(ans)