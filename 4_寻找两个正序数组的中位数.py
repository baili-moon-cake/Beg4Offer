class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        L = len(nums1) + len(nums2)
        if(len(nums1) <len(nums2)):
            nums1, nums2 = nums2 , nums1 #保持nums1比较长
        if L == 2:
            if len(nums2) == 0:
                return (nums1[0] + nums1[1]) / 2.0
            return (nums1[0] + nums2[0]) / 2.0

        if L%2 == 0: #even
            EorO = True 
            k = L // 2
        else: #Odd
            EorO = False
            k = L // 2 + 1
        print(EorO, k)
        def helper(nums1,nums2,k): #本质上是找第k小的数
            if(len(nums1) <len(nums2) or (len(nums1) == len(nums2) and nums1[0] > nums2[0])):
                nums1, nums2 = nums2 , nums1 #保持nums1比较长；或者两个序列长度相等时，保持nums1[0]值最小
            if(len(nums2)==0): #递归返回条件之一，短序列nums2被剔空
                if EorO == True:
                    return (nums1[k-1] + nums1[k]) / 2.0 #二序列长度之和为偶数，取nums1的第k小和k-1小数
                else:
                    return nums1[k-1] #二序列长度之和为奇数，直接返回nums1的第k小数
            if(k==1): #递归返回条件之二，两个序列都有内容。二序列长度之和为偶数时，需判断很多边界条件。
                if EorO == True:
                    n1 = min(nums1[0], nums2[0]) #取出最小的首元素
                    if n1 == nums1[0]: #如果第一个序列的首元素最小
                        return (n1 + min(nums1[1], nums2[0])) / 2.0 #因为此时，二序列长度不为0，nums1至少有两个元素，nums2至少有1个元素
                    else: #如果nums2[0]最小
                        if len(nums2) > 1: #若nums2长度大于1，则取nums2[1]与nums1[0]的较小者与nums2[0]为所需结果
                            return (n1 + min(nums1[0], nums2[1])) / 2.0 
                        else: #若nums2长度为1，则取nums1[0]与nums2[0]为结果
                            return (n1 + nums1[0]) / 2.0
                else: #二序列长度之和为奇数
                    return min(nums1[0],nums2[0])  #找最小数，比较数组首位
            t = min(k//2,len(nums2)) # 保证不上溢
            if( nums1[t-1]>=nums2[t-1] ): #递归调用，即每次以新的k值和新的nums1（比较后的长序列）nums2（剔掉k/2个元素的新序列）作为递归调用参数
                return helper(nums1 , nums2[t:],k-t)
            else:
                return helper(nums1[t:],nums2,k-t)

        return helper(nums1, nums2, k)
