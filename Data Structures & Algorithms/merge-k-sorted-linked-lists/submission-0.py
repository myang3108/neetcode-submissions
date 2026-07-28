# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 1 2 3
        # 1 3 5
        # 3 6
        # use a heap -> store all 3 heads in a minheap
        # there will always only be 3 or less nodes in the heap
        # each time we pop from the heap add the next reference in if there is one
        # keep going until heap is empty

        heap = []
        dummy = ListNode()
        curr = dummy

        # first put all the heads in
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        while heap:
            val, i, currnode = heapq.heappop(heap)
            curr.next = currnode
            curr = curr.next
            if currnode.next:
                heapq.heappush(heap, (currnode.next.val, i, currnode.next))
        
        return dummy.next


        