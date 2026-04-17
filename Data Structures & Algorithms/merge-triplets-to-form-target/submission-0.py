class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # it's not just if we're able to locate those integers
        # because we may not be able to get to the target
        # through max computations
        # (we might accidentally overwrite a matching value in a different pos)

        # how can we do this greedily?
        # we want to sort in descending order
        # so that when we loop and find a target value, we can safely
        # just continue using that target value without needing to do
        # a max computation
        # because it will forcefully be larger than the comparison value
        # since it'll appear later in the descending array

        sorted(triplets, reverse=True)

        curr = [0, 0, 0]
        
        # actually we just need to remove any triplets where any value
        # is greater than its target relative
        # because that means we CANNOT use this to find our solution
        # because it'll exceed our target when we take a max function
        # therefore we must discard any exceeding triplets
        # and from the rest of the valid triplets, if we are able to locate
        # the target value, then we have a valid solution, because when we
        # take the max operation, it'll forcefully be at a max the target
        # so when we go thru the whole array
        # if our maximum values are matching we are done

        max_i = 0
        max_j = 0
        max_k = 0

        optimal = []

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            optimal.append(triplet)
        
        for triplet in optimal:
            max_i = max(max_i, triplet[0])
            max_j = max(max_j, triplet[1])
            max_k = max(max_k, triplet[2])
        
        return [max_i, max_j, max_k] == target