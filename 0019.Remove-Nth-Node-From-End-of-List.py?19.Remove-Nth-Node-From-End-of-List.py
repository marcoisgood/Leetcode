"""

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        tmp = head
        count = 0

        while tmp is not None:
            tmp = tmp.next
            count += 1

        k = count - n

        prev = None
        ptr = head
        while k != 0:
            prev = ptr
            ptr = ptr.next
            k-=1

        if prev is None:
            return head.next
        else:
            prev.next = ptr.next
            ptr.next = None
            return head


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head = Solution().removeNthFromEnd(head,4)
    print(head.next.val)
