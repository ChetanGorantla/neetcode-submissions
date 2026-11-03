class SeatManager:
    # use a priority queue to get O(logn) reserve
    # and O(logn) unreserve
    # otherwise reserve would be O(n)
    # and unreserve would be O(1)
    # does the split of requests match this benefit
    # yeah looks like it

    def __init__(self, n: int):
        self.slots = [1]*n
        self.pq = []
        for i in range(1, n+1):
            self.pq.append(i)

    def reserve(self) -> int:
        candidate = heapq.heappop(self.pq)
        self.slots[candidate-1] = 0
        return candidate
        
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.pq, seatNumber)
        self.slots[seatNumber-1] = 1
        
