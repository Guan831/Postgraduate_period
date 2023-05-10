# Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        cur = dummy
        p1, p2 = l1, l2
        carry = 0
        while p1 or p2:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            _sum = val1 + val2 + carry
            carry = _sum // 10
            cur.next = ListNode(_sum % 10)
            cur = cur.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        if carry:
            cur.next = ListNode(carry)
        return dummy.next
