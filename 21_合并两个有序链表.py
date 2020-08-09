# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None or l2 is None:
            return l1 if l2 is None else l2
        if l1.val <= l2.val:
            self.coreFunc(l1,l1.next,l2)
            return l1
        else:
            self.coreFunc(l2,l1,l2.next)
            return l2
    def coreFunc(self, curNode: ListNode, l1: ListNode, l2: ListNode)
        if l1 is None or l2 is None:
            curNode.next = l1 if l2 is None else l2
        else:
            if l1.val<=l2.val:
                curNode.next = l1
                self.coreFunc(l1, l1.next, l2)
            else:
                curNode.next = l2
                self.coreFunc(l2, l1, l2.next)
