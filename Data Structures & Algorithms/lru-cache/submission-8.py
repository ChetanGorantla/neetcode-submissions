class LRUCache:
    # we need to maintain two hashmaps
    # one hashmap is key value pair
    # the other one represents a key to uses?
    # when we want to put, if the capacity exceeds, we need to remove the key that was used last
    # how do we want to store the least recently used key?
    # store the latest time that a key was used?
    # increment time each instance?
    # we can't loop through the times
    # we can rather just make a linked list that connects all uses
    # treat that as a sliding window
    # whenever we want to add, we append to the end of the linked list
    # whenever we need to pop, we shift the beginning of the linked list
    # and remove from the cache

    # we also need to figure out a way to ensure we are skipping over stale values
    # whenever we decide to pop
    # we don't want to pop a duplicate
    # maybe we need to maintain a set?
    # we can actually just check to see what's in the hashmap
    # we should maintain the frequency of a key in the window?
    # that way, whenever we want to pop we should decrement the frequency
    # and only stop popping whenever the frequency == 0
    # and in that instance truly remove that from the cache
    # that's our first instance of a key that is truly deleted
    
    # why do we need a doubly linked list? can't we just use a singly linked list?
    # let's first try a singly linked list

    # if we use a doubly linked list,
    # we don't need to iterate to get rid of a duplicate.
    # when we want to update the state of (get, put) a node that already exists in the cache, 
    # we can have a hashmap that maps a key to a listnode
    # and essentially bridge the gap across and push it to the end
    # that way it's o(1)
    
    class ListNode():
        def __init__(self, curr, prev = None, next=None):
            self.curr = curr
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int):
        self.cache = {}
        self.nodes = {}
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key]
            self.update_state(key)
            # check to see if we exceed capacity
            if len(self.cache) > self.capacity:
                # we need to pop from the start
                # no duplicates possible, remove from cache
                #print(self.cache)
                #print(key)
                #print(self.head)
                #print(self.tail)

                lru = self.head
                # must shift head
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
                else:
                    self.tail = None
                

                # remove from nodes
                self.cache.pop(lru.curr)
                self.nodes.pop(lru.curr)

                # shift the head
        else:
            val = -1

        

        return val

    def put(self, key: int, value: int) -> None:

        # update state BEFORE you add to the cache
        self.update_state(key)
        # return the value if it exists
        self.cache[key] = value

        # check to see if we exceed capacity
        if len(self.cache) > self.capacity:
            # we need to pop from the start
            # no duplicates possible, remove from cache
            #print(self.cache)
            #print(key)
            #print(self.head)
            #print(self.tail)

            lru = self.head
            # must shift head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            

            # remove from nodes
            self.cache.pop(lru.curr)
            self.nodes.pop(lru.curr)

            # shift the head

    def update_state(self, key:int):
        # first we need to check if the key is already in the cache.
        # later we check to see if we exceed the capacity because that's contingent on whether or not
        # our key is already in the cache

        if key in self.cache:
            
            # we need to jump
            # locate that node to delete
            node_to_shift = self.nodes[key]
            if node_to_shift == self.tail:
                # no op
                return
            elif node_to_shift == self.head:
                self.head = self.head.next
                self.head.prev = None
                self.tail.next = node_to_shift
                node_to_shift.prev = self.tail
                node_to_shift.next = None
                self.tail = node_to_shift
            else:
                # middle case
                # jumped pointers
                node_to_shift.prev.next = node_to_shift.next
                node_to_shift.next.prev = node_to_shift.prev
                # shift this to the end
                node_to_shift.prev = self.tail
                self.tail.next = node_to_shift
                node_to_shift.next = None
                # shift the tail
                self.tail = node_to_shift
            
            #if node_to_shift.next:
            #    node_to_shift.next.prev = node_to_shift.prev

        else:
            # we can just append to the end
            new_node = self.ListNode(key)
            if not self.head:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            
            # add this node to nodes
            self.nodes[key] = new_node
        
        
            
            
            
        


        
