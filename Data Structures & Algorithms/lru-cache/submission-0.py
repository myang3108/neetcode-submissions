class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # map key to node!!! not the val!!
        self.cap = capacity
        self.head = Node(0,0) # lru
        self.tail = Node(0,0) # mru
        self.head.next = self.tail
        self.head.prev = None
        self.tail.prev = self.head
        self.tail.next = None

         
    def get(self, key: int) -> int:
        # if it exists, we return the value
        # then remove it from the current place in the list
        # add it to the back
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        # update the value if it exists
        # put it in the back
        # otherwise add it and then put it in the back
        # before we do that check to see the size
        if key in self.cache:
            self.remove(self.cache[key])
        
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(newNode)

        if len(self.cache) > self.cap:
            lru = self.head.next
            self.remove(lru) # remove from linked list and delete from the hashmap
            del self.cache[lru.key]

            
            
    def insert(self, node):
        # insert this node to the back of the list
        tmp = self.tail.prev
        tmp.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = tmp


    def remove(self, node):
        # remove the node from the list
        node.prev.next = node.next
        node.next.prev = node.prev