class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        longest = 0
        for n in setNums:
            if n-1 not in setNums: #looking only at possible start points. if not a start point, skip over it.
                length = 1
                while (n+length) in setNums: #looking until the end of the consecutive sequence
                    length+=1
                longest = max(length, longest)

        return longest 
