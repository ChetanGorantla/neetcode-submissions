class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # maintain a set of elements
        # we need to see, have we explored this before?
        # if not, let's start a double-ended sequence from this.
        # extend as far left and right as we possibly can
        # no need to memoize because the value we encounter right now 
        # is guaranteed to be the same for all values of the sequence
        maxlen = 0

        contained = set(nums)

        for num in nums:
            if num not in contained:
                continue

            contained.remove(num)
            left = num-1
            right = num+1
            while left in contained:
                contained.remove(left)
                left-=1
            while right in contained:
                contained.remove(right)
                right+=1
            
            # right now left and right are greater than their actual vaues
            # 1 5 -> 2 3 4 -> right-left-1
            maxlen = max(maxlen, right-left-1)
        return maxlen
