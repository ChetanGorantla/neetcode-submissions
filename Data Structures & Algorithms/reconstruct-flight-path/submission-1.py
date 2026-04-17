class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # insert tuples of (src, dest) in usedtickets
        
        # need to backtrack

        # at each stop, look at all stops you haven't visited
        # visit those and try to explore

        # base case is if our visited set is of length adjacency
        # if so, return the answer as the path

        
        remainingtickets = {}
        adjacency = {}

        for ticket in tickets:
            src = ticket[0]
            dest = ticket[1]
            
            if src in adjacency:
                adjacency[src].append(dest)
            else:
                adjacency[src] = [dest]

            if dest not in adjacency:
                adjacency[dest] = []
            
            if (src, dest) in remainingtickets:
                remainingtickets[(src, dest)] += 1
            else:
                remainingtickets[(src, dest)] = 1
            

        
        # adjacency list populated
        print(adjacency)
        

        # sort so that we explore the lexicographic optimal first
        for node in adjacency:
            adjacency[node].sort()


        output = []
        # at each step, backtrack across all possible flights
        # among all the ones that return true (able to use all tickets)
        # figure out the smallest one
        # and add that to the overall path


        def explore(src, flights):
            nonlocal output
            if flights == len(tickets)+1:
                return True
            
            # otherwise we can explore this node to continue the path

            # explore
            
            for dest in adjacency[src]:
                # if we have enough tickets left to explore this edge, explore it
                if (remainingtickets[(src, dest)] > 0):
                    remainingtickets[(src, dest)]-=1
                    if explore(dest, flights+1):
                        output.append(dest)
                        return True
                    remainingtickets[(src, dest)]+=1
            

            return False

    
        # seed explore with (JFK, a set with JFK, and JFK as the starting path)
        explore("JFK", 1)
        output.reverse()
        output.insert(0, "JFK")
        return output