# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = l1
        second = l2
        dummy = ListNode(0)
        third = dummy
        carry = 0

        while first and second:
            val = first.val + second.val + carry
            carry = 0

            if val >= 10:
                carry += 1
                val = val % 10
            third.next = ListNode(val)
            third = third.next
            first = first.next
            second = second.next
        while first:
            val = first.val + carry
            carry = 0
            if val >= 10:
                carry += 1
                val = val % 10
            third.next = ListNode(val)
            third = third.next
            first = first.next
        while second:
            val = second.val + carry
            carry = 0
            if val >= 10:
                carry += 1
                val = val % 10
            third.next = ListNode(val)
            third = third.next
            second = second.next
        if carry > 0:
            third.next = ListNode(carry)

        return dummy.next
        

