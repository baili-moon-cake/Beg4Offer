# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pointA, pointB = headA, headB
        lengthA = 0
        lengthB = 0
        while(pointA or pointB):
            if pointA:
                lengthA+=1
                pointA = pointA.next
            if pointB:
                lengthB+=1
                pointB = pointB.next
        fast, slow = (headA, headB) if headB.next else (headB, headA)
        for i in range(diff):
            fast = fast.next
        while(fast and slow):
            if fast == slow:
                return fast
            else:
                fast, slow = fast.next, slow.next 
        return None