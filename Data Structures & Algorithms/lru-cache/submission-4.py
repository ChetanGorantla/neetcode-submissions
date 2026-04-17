class DoublyLinkedNode:
    def __init__(self, val=None, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.nxt = nxt


class LRUCache:
    # need to maintain a doubly linked list
    # to be able to add in O(1) and remove in O(1)
    # maintain a doubly linked list of the KEYS
    # hashmap of key value pairs
    



    def __init__(self, capacity: int):
        self.hashmap = {}
        self.nodes = {}
        self.capacity = capacity
        self.size=0
        self.head = None
        self.tail = None

    def move_to_tail(self, node: DoublyLinkedNode):
        if node is not self.tail:

            # detach
            # remove prev
            if node.prev:
                node.prev.nxt = node.nxt
            else:
                # node was head
                self.head = node.nxt
                if self.head:
                    self.head.prev = None
            
            if node.nxt:
                node.nxt.prev = node.prev
            else:
                # node was tail (shouldn't really happen)
                self.tail = node.prev

            # attach at tail
            node.prev = self.tail
            node.nxt = None

            if self.tail:
                self.tail.nxt = node
            else:
                # no values present, need to initialize
                self.head = node

            self.tail = node

    def get(self, key: int) -> int:
        print("Reinserting " + str(key))
        print(self.hashmap)
        print(self.nodes)
        node = self.nodes.get(key)
        if node is None:
            return -1
        
        self.move_to_tail(node)
            
        return self.hashmap[key]


    def put(self, key: int, value: int) -> None:
        print("Putting " + str(key))

        if key in self.nodes:
            # update value and insert at tail, but don't change size
            # or create new node
            self.hashmap[key] = value
            self.move_to_tail(self.nodes[key])
            return

        # if nothing in the doubly linked list we need to initialize it
        if not self.head:
            node = DoublyLinkedNode(key, None, None)
            self.head = node
            self.tail = node
        else:
            # insert to end
            old_tail = self.tail
            new_tail = DoublyLinkedNode(key, None, None)
            new_tail.prev = old_tail
            self.tail.nxt = new_tail
            self.tail = self.tail.nxt
        
        # add to hashmaps
        self.nodes[key] = self.tail
        self.hashmap[key] = value
        self.size+=1
        # put the nodes
        # check capacity overflow
        if self.size > self.capacity:
            print("Popping " + str(self.head.val))
            lru_key = self.head.val
            if lru_key in self.hashmap:
                self.hashmap.pop(lru_key)
            if lru_key in self.nodes:
                self.nodes.pop(lru_key)

            old_head = self.head

            self.head = old_head.nxt
            if self.head:
                self.head.prev = None
            else:
                self.tail = None #Nothing left
            #detach old ptr
            old_head.prev = old_head.nxt = None
            self.size-=1
        # deleted LRU and shifted head
        

