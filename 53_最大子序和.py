class Solution:
    def maxSubArray(self, nums: List[int]):
        maxSum = float('-inf')
        curSum = 0
        for num in nums:
            curSum=num if curSum+num<0 else curSum+num
            maxSum=maxSum if curSum<=maxSum else curSum
        return maxSum
