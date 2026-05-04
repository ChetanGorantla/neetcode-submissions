class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # ideally we want to put together high + low
        # and converge
        # so first sort the array

        list.sort(people)
        #print(people)
        # maintain two pointers (l, r)
        l = 0
        r = len(people)-1
        c = 0
        # converge
        while (l <= r):
            # right person too heavy; make them separate and shift to next heavy
            pair = people[l] + people[r]
            if pair > limit:
                #print(f"single {r}")
                c+=1
                r-=1
            else:
                #print(f"double {l}, {r}")
                c+=1
                r-=1
                l+=1
        
        return c