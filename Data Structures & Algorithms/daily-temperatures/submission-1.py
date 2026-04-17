class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        days = []
        for i in range(0, len(temperatures)-1):
            count = 1
            curr = temperatures[i]
            r = i+1
            nxt = temperatures[r]
            stack.append(curr)
            while (temperatures[r] <= curr):
                print(curr, temperatures[r])
                if (r == len(temperatures)-1):
                    count = 0
                    break
                else:
                    r+=1
                    count+=1
            days.append(count)

        days.append(0)
        return days


