class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.hmap = {}
        self.capacity = capacity
    
    def log(self):
        curr = self.head
        while curr:
            node_string = f"({curr.key},{curr.value})"
            if curr == self.head:
                node_string+="H"
            elif curr == self.tail:
                node_string+="T"
            print(node_string, end="->")
            curr = curr.next
        print()

    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1
        node = self.hmap[key]
        if len(self.hmap) == 1 or node == self.tail:
            return node.value

        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
            node.next = None
            node.prev = self.tail
            self.tail.next = node
            self.tail = self.tail.next
        
        else:
            prev = node.prev
            next = node.next

            node.next = None
            node.prev = self.tail
            self.tail.next = node
            self.tail = self.tail.next            

            prev.next = next
            next.prev = prev
        
        return node.value

    def _delete_least_recent(self):
        key = self.head.key
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        del self.hmap[key]

    def put(self, key: int, value: int) -> None:
        # if key exists then just update value of node
        if key in self.hmap:
            self.hmap[key].value = value
            self.get(key)
            return
        
        # if we're at capacity, remove least recent
        if len(self.hmap) == self.capacity:
            self._delete_least_recent()

        node = Node(key, value)

        # add the node
        if self.tail:
            node.prev = self.tail
            self.tail.next = node
            self.tail = self.tail.next
        else:
            self.tail = node
            self.head = node
        
        if not self.head:
            self.head = node
        
        self.hmap[key] = node
