class TimeMap:

    def __init__(self):
        self.mapping = {}

    # define binary search to return next best index if not located
    # (left side next best)
    def search(self, target: int, vals: List[int]):
        # look for this target among our mapped vals
        l = 0
        r = len(vals)-1
        while l < r:
            m = (l+r+1)//2
            if vals[m][0] < target:
                l = m
            elif vals[m][0] > target:
                r = m-1
            else:
                return m
        """
        if vals[l] < target:
            return l+1
        else:
            return l
            """
        return l

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapping:
            self.mapping[key] = [(timestamp, value)]
        else:
            ind = self.search(timestamp, self.mapping[key])
            self.mapping[key].insert(ind+1, (timestamp, value))
            
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapping:
            return ""
        #print(self.mapping)
        ind = self.search(timestamp, self.mapping[key])\
        # we are not looking for exact matches
        # we are looking for closest
        #print(ind)
        if ind in range(len(self.mapping[key])) and self.mapping[key][ind][0] <= timestamp:
            return self.mapping[key][ind][1]
        return ""
