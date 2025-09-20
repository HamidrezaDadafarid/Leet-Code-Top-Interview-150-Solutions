# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def hasCycle1(self, head: ListNode) -> bool:
        if head is None:
            return False

        slow, fast = head, head

        # fast itself must not be nil (so fast.next is a valid access).
        # fast.next must not be nil (so fast.next.next is a valid access).
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True

        return False

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def hasCycle2(self, head: ListNode) -> bool:
        s = set()

        while head:
            if head in s:
                return True

            s.add(head)
            head = head.next

        return False
