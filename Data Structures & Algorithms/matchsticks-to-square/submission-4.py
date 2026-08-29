class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)

        if total % 4 != 0:
            return False

        target = total // 4

        matchsticks.sort(reverse=True)

        if matchsticks[0] > target:
            return False

        memo = {}

        def backtrack(length, completed, mask):
            if completed == 3:
                return True

            if (length, completed, mask) in memo:
                return memo[(length, completed, mask)]

            for i in range(len(matchsticks)):
                # stick already used
                if mask & (1 << i):
                    continue

                new_length = length + matchsticks[i]

                if new_length > target:
                    continue

                new_mask = mask | (1 << i)

                if new_length == target:
                    if backtrack(0, completed + 1, new_mask):
                        memo[(length, completed, mask)] = True
                        return True
                else:
                    if backtrack(new_length, completed, new_mask):
                        memo[(length, completed, mask)] = True
                        return True

            memo[(length, completed, mask)] = False
            return False

        return backtrack(0, 0, 0)