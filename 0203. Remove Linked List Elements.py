# Remove all elements from a linked list of integers that have value val.
#
# Example:
#
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Ans 1
# class Solution:
#     def removeElements(self, head: ListNode, val: int) -> ListNode:
#
#         if not head:
#             return
#         if head.next == None and head.val == val:
#             return
#         prev = None
#         res = prev
#         curr = head
#
#         while curr:
#             if curr.val != val:
#                 if prev == None:
#                     prev = curr
#
#                 else:
#                     prev.next = curr
#                     prev = prev.next
#             else:
#                 if prev == None:
#                     head = head.next
#             curr = curr.next
#
#         if prev is not None:
#             prev.next = None
#             return head
#         else:
#             return None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        curr = res = ListNode()
        curr.next = head

        while curr:
            while curr.next and curr.next.val == val:
                curr.next = curr.next.next
            curr = curr.next

        reuturn res.next
