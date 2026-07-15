# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [0, n-1, 1, n-2, 2, n-3, ...]
        # break list into 2
        # reverse the second half of the list
        # merge the 2
        if head.next is None:
            return

        slow = head
        fast = head
        p = None

        while fast is not None and fast.next is not None:
            p = slow
            slow = slow.next
            fast = fast.next.next
        
        p.next = None

        prev = None
        tmp = None
        newhead = slow

        while newhead is not None:
            tmp = newhead.next
            newhead.next = prev
            prev = newhead
            newhead = tmp
        
        def merge(head1, head2, flag):
            if head1 and not head2:
                return head1
            if not head1 and head2:
                return head2
            if flag:
                tmp = head1.next
                head1.next = head2
                merge(tmp, head2, not flag)
            if not flag:
                tmp = head2.next
                head2.next = head1
                merge(head1, tmp, not flag)
        
        merge(head, prev, 1)
        





