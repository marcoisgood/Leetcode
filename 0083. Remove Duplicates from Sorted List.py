"""

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

               if not head or head.next is None:
            return head

        p1 = head
        while p1:
            if p1 is None or p1.next is None:
                return head

            elif p1.next.val == p1.val:
                p1.next = p1.next.next

            else:
                p1 = p1.next
