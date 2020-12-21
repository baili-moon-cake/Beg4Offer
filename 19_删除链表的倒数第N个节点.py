# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None
        pfast, pslow = head, head
        for _ in range(n):
            pfast = pfast.next
            if pfast is None:
                return head.next
        while(True):
            pfast = pfast.next
            if pfast is None:
                pslow.next = pslow.next.next
                return head
            else: 
                pslow = pslow.next
        return head
