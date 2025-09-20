class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    result = ListNode()
    tail = result
    total, carry = 0, 0
    val1, val2 = 0, 0

    while l1 is not None or l2 is not None:
        val1 = l1.val if l1 is not None else 0
        val2 = l2.val if l2 is not None else 0

        total = val1 + val2 + carry
        carry = total // 10
        tail.next = ListNode(total % 10)
        tail = tail.next

        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next

    if carry:
        tail.next = ListNode(1)

    return result.next
