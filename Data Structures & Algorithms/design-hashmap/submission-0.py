class ListNode:
   def __init__(self, key = -1, val = -1, next = None):
       self.key = key
       self.val = val
       self.next = next


class MyHashMap:


   def __init__(self):
       # since we know that there will only be a finite amount of calls, we can initalize an array of 1000 and then mod key % 1000 to figure out which bucket
       # to store it
       # for collisions, we can represent it as a linked list so if 2 keys have the same hash it'll be tacked onto the list
       # have a dummy at the start so if we delete a node we can set dummy->next to none
       self.map = [ListNode() for _ in range(1000)]
      
   def hash(self, key):
       return key % len(self.map)


   def put(self, key: int, value: int) -> None:
       # needs to traverse through the bucket to see if the key exists
       # if not we make a new node and tack it onto the end
       hashedKey = self.hash(key)
       curr = self.map[hashedKey]


       while curr.next is not None:
           if curr.next.key == key:
               curr.next.val = value
               return
           else:
               curr = curr.next


       node = ListNode(key, value)
       curr.next = node
       return
  
   def get(self, key: int) -> int:
       hashedKey = self.hash(key)
       curr = self.map[hashedKey]


       while curr is not None:
           if curr.key == key:
               return curr.val
           else:
                           curr = curr.next


       return -1
      
   def remove(self, key: int) -> None:
       hashedKey = self.hash(key)
       curr = self.map[hashedKey]


       while curr.next is not None:
           if curr.next.key == key:
               curr.next = curr.next.next
               return
           else:
               curr = curr.next

