class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # locate all indices of all numbers in the array
        # num -> [ind1, ind2 ...]
        # maybe we loop over all possible numbers
        # for each index, we can replace all from ind1 - k to ind1 + k, inclusive
        # ensure that we don't double count
        # to prevent double counting, for each number, we need to maintain a left bound
        # and right bound
        # left bound is used when for max(ind1-k, left bound, 0)
        # right bound is used when min(ind1+k, ind2) if ind2 else ind1+k
        # set left bound to right bound
        # ensure we have a check to see if ind2 actually exists

        """
        indices = defaultdict(list)
        for i in range(len(nums)):
            indices[nums[i]].append(i)

        maxbeauty = 0
        for num in indices:
            leftbound = 0
            inds = indices[num]
            beauty = 0
            for i in range(len(inds)):
                ind = inds[i]
                l = max(ind-k, leftbound)
                r = min(ind+k, inds[i+1] if i < len(inds)-1 else len(nums)-1)
                leftbound = r+1
                beauty += r-l+1
            maxbeauty = max(maxbeauty, beauty)
        
        return maxbeauty
        """

        # solved the wrong problem LOL oops
        nums.sort()
        l = 0
        maxlen = 0
        for r in range(len(nums)):
            # we need to figure out the window such that all elements 
            # are within 2k of the range
            # so compress our l while nums[r]-nums[l] > 2k
            while nums[r]-nums[l] > 2 * k:
                l+=1
            maxlen = max(maxlen, r-l+1)
        return maxlen
                


