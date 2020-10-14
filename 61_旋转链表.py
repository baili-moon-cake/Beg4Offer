# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        length, tail = 1, head
        while(tail.next):
            length += 1
            tail = tail.next
        k = k % length
        if k == 0 or length <=1:
            return head 
        c = head
        while(length-k>0):
            c, p = c.next if c.next else head, c
            k += 1
        p.next, tail.next, head = None, head, p.next
        return head