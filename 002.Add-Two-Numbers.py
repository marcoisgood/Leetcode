"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        res = ListNode(0)
        ans = res
        tmp = 0

        while True:
            if l1 is not None:
                tmp = tmp + l1.val
                l1 = l1.next
            if l2 is not None:
                tmp = tmp + l2.val
                l2 = l2.next
            ans.val = tmp % 10
            tmp = tmp // 10
            if tmp == 0 and l1 is None and l2 is None:
                break

            ans.next = ListNode(0)
            ans = ans.next
        return res

if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next =ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next =ListNode(6)
    l2.next.next = ListNode(4)
    result = Solution().addTwoNumbers(l1, l2)
    print(result)
