class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        out = []
        for interval in intervals:
            # check to see if this interval overlaps with the last one we appended
            if out and out[-1][1] >= interval[0]:
                out[-1][1] = max(interval[1], out[-1][1])
            else:
                out.append(interval)
            
        return out