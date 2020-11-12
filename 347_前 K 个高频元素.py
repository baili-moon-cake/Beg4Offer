from typing import List


from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:    
        return [k for k,v in Counter(nums).most_common()[:k]]