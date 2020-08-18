class Solution:
    def hasCycle(self, head: ListNode):
        pSlow = head
        pFast = head
        while(pSlow):
            pSlow = pSlow.next
            pFast = pFast.next if pFast else pFast
            pFast = pFast.next if pFast else pFast
            if pFast and pSlow and pFast == pSlow: return True
        return False