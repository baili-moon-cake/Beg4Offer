# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        else:
            left, right = self.cut(head)
        sorted_left, sorted_right = self.sortList(left), self.sortList(right)
        return self.merge(sorted_left, sorted_right)

    def cut(self, head):
        slow, fast = head, head
        while(fast.next):
            fast = fast.next
            if fast.next is None:
                break
            fast = fast.next
            slow = slow.next
        left, right = head, slow.next
        slow.next = None
        return left, right

    def merge(self, left, right):
        root = ListNode(0)
        fake = root
        while(left and right):
            if left.val < right.val:
                fake.next = left
                left = left.next
            else:
                fake.next = right
                right = right.next 
            fake = fake.next
        fake.next = left if left else right
        return root.next