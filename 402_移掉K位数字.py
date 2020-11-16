class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if num == '0' or num == '' or k == len(num):
            return '0'
        elif k == 0:
            return num

        num_str = num 
        while(k>0):
            num_str = self.corefunc(num_str)
            k += -1
            if num_str == '0' or num_str == '':
                return '0'
        return num_str


    
    # 找逆序对,如果没有就去除最后一个字符;
    def corefunc(self, num_str):
        for idx in range(len(num_str)-1):
            if num_str[idx] > num_str[idx+1]:
                return (num_str[:idx]+num_str[idx+1:]).lstrip('0')
        return num_str[:-1].lstrip('0')
            
        