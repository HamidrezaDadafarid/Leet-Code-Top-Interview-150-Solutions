# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head = ListNode()
        tail = head

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        while list1 is not None:
            tail.next = list1
            list1 = list1.next
            tail = tail.next

        while list2 is not None:
            tail.next = list2
            list2 = list2.next
            tail = tail.next

        return head.next
