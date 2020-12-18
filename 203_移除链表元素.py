# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        while(head and head.val == val):
            head = head.next
        pnode = head
        while(pnode):
            tempnode = pnode.next
            while(tempnode and tempnode.val == val):
                tempnode = tempnode.next
            pnode.next, pnode = tempnode, tempnode
        return head