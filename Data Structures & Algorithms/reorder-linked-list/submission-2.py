# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        cur = slow.next
        slow.next = None
        
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        
        list1 = head
        list2 = prev

        while list2:
            tmp1 = list1.next
            tmp2 = list2.next

            list1.next = list2
            list2.next = tmp1

            list1 = tmp1
            list2 = tmp2
