class DoublyLinkedNode:
    def __init__(self, val: int, prev: DoublyLinkedNode, nxt: DoublyLinkedNode):
        self.val = val
        self.prev = prev
        self.nxt = nxt
    
class MyCircularQueue:

    def __init__(self, k: int):
        self.limit = k
        self.size = 0
        self.header = DoublyLinkedNode(None, None, None)

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        # available space
        # create a new node
        if self.isEmpty():
            new_node = DoublyLinkedNode(value, self.header, self.header)
            self.header.nxt = new_node
            self.header.prev = new_node
        else:
            new_node = DoublyLinkedNode(value, self.header, self.header.nxt)
            self.header.nxt.prev = new_node
            self.header.nxt = new_node

        self.size+=1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        # not empty, remove from queue
        
        # check if that's the only element
        if self.size == 1:
            self.header.nxt = None
            self.header.prev = None
        else:
            # not the only element, free to access prev.prev
            self.header.prev.prev.nxt = None
            self.header.prev = self.header.prev.prev
        
        self.size-=1
        return True


    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.header.prev.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.header.nxt.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.limit


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()