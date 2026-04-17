class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        longest = 0
        for n in setNums:
            length = 1
            while (n - length) in setNums:
                length+=1
            longest = max(length, longest)

        return longest 
