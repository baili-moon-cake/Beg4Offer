# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        if l1 is None or l2 is None:
            return l1 if l1 else l2

        if l1.val+l2.val<10:
            res = ListNode(l1.val+l2.val)
            carry=0
        else:
            res = ListNode(l1.val+l2.val-10)
            carry=1
        pNode = res
        while(l1.next and l2.next):
            l1 = l1.next
            l2 = l2.next
            tmpNode, nextCarry=self.coreFunc(l1,l2,carry)
            if tmpNode:
                pNode.next=tmpNode
                pNode=pNode.next
                carry=nextCarry
        if l1.next:
            pNode.next = self.addTwoNumbers(l1.next,ListNode(carry))
        elif l2.next:
            pNode.next = self.addTwoNumbers(l2.next,ListNode(carry))
        else:
            pNode.next = ListNode(carry) if carry else None
        return res

    def coreFunc(self, l1, l2, carry):
        if l1.val+l2.val+carry<10:
            return (ListNode(l1.val+l2.val+carry),0)
        else:
            return (ListNode(l1.val+l2.val+carry-10),1)


