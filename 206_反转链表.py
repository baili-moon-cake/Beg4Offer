# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        prePointer = None
        curPointer = head
        while(curPointer):
            curPointer.next = prePointer
            prePointer = curPointer
            curPointer = curPointer.next
        return prePointer
