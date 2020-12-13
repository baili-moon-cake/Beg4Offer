# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        smallnode_listnode, largenode_listnode = \
            None, None
        smallnode_listhead, largenode_listhead = \
            None, None
        while(head):
            if head.val < x:
                if smallnode_listnode is None:
                    smallnode_listnode = head
                    smallnode_listhead = head
                else:
                    smallnode_listnode.next = head
                    smallnode_listnode = head
            else:
                if largenode_listnode is None:
                    largenode_listnode = head
                    largenode_listhead = head
                else:
                    largenode_listnode.next = head
                    largenode_listnode = head
            head = head.next
        if largenode_listnode is not None:
            largenode_listnode.next = None
        if smallnode_listnode is None:
            return largenode_listhead
        smallnode_listnode.next = largenode_listhead
        return smallnode_listhead