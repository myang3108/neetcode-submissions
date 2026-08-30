# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # need a dummy node at the start
        dummy = ListNode(0, head)
        curr = head # walk through the list until null or a multiple of 4
        # need a start that represents where curr was originally (tail) -> which is what we pass into the reverse list as the head
        prev = dummy

        while curr is not None:
            tail = curr 
            i = 0
            while curr is not None and i < k:
                curr = curr.next
                i += 1
            if i != k:
                prev.next = tail
            else:
                prev.next = self.reverse(tail, k)
                prev = tail
        
        return dummy.next


    def reverse(self, node, k):
        curr = node
        prev = None
        while curr is not None and k > 0:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            k -= 1

        return prev
        