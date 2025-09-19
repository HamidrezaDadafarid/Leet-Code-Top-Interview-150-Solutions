# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True

        return False

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        s = set()

        while head:
            if head in s:
                return True

            s.add(head)
            head = head.next

        return False
