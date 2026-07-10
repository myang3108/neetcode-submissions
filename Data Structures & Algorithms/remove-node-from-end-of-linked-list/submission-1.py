# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            curr = head
            counter = 0
            while (curr is not None):
                counter += 1
                curr = curr.next
            
            # print(counter)
            if counter == 1 and n == 1:
                return None
            indexofNode = counter - n
            if indexofNode == 0:
                return head.next
            i = 0
            curr = head
            prevNode = None
            while (curr is not None and i < indexofNode - 1):
                # print(curr.val)
                curr = curr.next
                i += 1
            
            # print("stop", curr.val)
            tmp = curr.next
            if tmp.next is None:
                curr.next = None
            else:
                curr.next = tmp.next
            # head.remove(indexofNode)

            return head