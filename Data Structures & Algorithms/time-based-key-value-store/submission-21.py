class TimeMap:
    
    def __init__(self):
        # map format
        # {key: [value_i]}
        # the values array is dynamic, not static
        # we want to keep the array in sorted order
        # so we can use binary search to locate where to insert (next best ind)
        # and use that same next best ind binary search to locate which value 
        # to return for get
        # since next_best represents either timestamp or the prev best timestamp
        # store values inside of the array as tuples (timestamp, val)
        self.map = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        
        ind = self.binarysearch(key, timestamp)
        print(f"Putting {(timestamp, value)} in located index {ind}, inserting at {ind+1} for {self.map[key]}")
        self.map[key].insert(ind+1, (timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        #print(self.map[key])
        best_ind = self.binarysearch(key, timestamp)
        print(f"Located best ind: {best_ind} ")
        if best_ind == -1:
            return ""
        print(self.map)
        return self.map[key][best_ind][1]

    def binarysearch(self, key: str, timestamp: int) -> int:
        arr = self.map[key]
        print(arr)
        print(timestamp)
        
        l = 0
        r = len(arr)-1
        best = -1

        while l <= r:
            mid = (l+r)//2
            if (arr[mid][0] <= timestamp):
                best = mid
                l = mid+1
            else:
                r = mid-1
        return best
            


        
            
