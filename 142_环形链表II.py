# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return None
        p_fast, p_slow = head, head
        stepcnts_fast, stepcnts_slow = 0, 0
        try:
            while(True):
                p_fast, stepcnts_fast = p_fast.next, stepcnts_fast+1
                if p_fast is p_slow:
                    break
                p_fast, stepcnts_fast = p_fast.next, stepcnts_fast+1
                if p_fast is p_slow:
                    break
                p_slow, stepcnts_slow = p_slow.next, stepcnts_slow+1
                if p_fast is p_slow:
                    break
        except AttributeError as e:
            return None
        p_behind, p_forward = head, head
        for _ in range(stepcnts_fast - stepcnts_slow):
            p_forward = p_forward.next
        while(p_forward is not p_behind):
            p_forward = p_forward.next
            p_behind = p_behind.next
        return p_forward


"""
ListNode

"""