# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        p_node, p_previous = head.next, head
        self.hash_table = {head.val,}
        while(p_node):
            if p_node.val not in self.hash_table:
                self.hash_table.add(p_node.val)
                p_previous = p_node
            else:
                p_previous.next = p_node.next
            p_node = p_node.next
        return head