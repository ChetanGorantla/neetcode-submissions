class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # we cannot treat this as four seperate cases
        # we must treat this as one case altogether
        # 
        # create a graph of every possible direction
        # 

        # if the destination is in deadends, don't add that connection
        # or if the source is in deadends, don't source it out to anywhere (continue)

        adjacency = {}
        deadend_set = set(deadends)
        if "0000" in deadend_set:
            return -1
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    for l in range(10):
                        # string = ijkl
                        curr = f"{i}{j}{k}{l}"
                        if curr in deadend_set:
                            continue
                        adjacent = []
                        for m in range(4):
                            
                            if int(curr[m]) == 0:
                                adj = curr[0:m] + "9" + curr[m+1:]
                                
                            else:
                                adj = curr[0:m] + str(int(curr[m])-1) + curr[m+1:]
                            if adj not in deadend_set:
                                adjacent.append(adj)

                            if int(curr[m]) == 9:
                                adj = curr[0:m] + "0" + curr[m+1:]
                                
                            else:
                                adj = curr[0:m] + str(int(curr[m])+1) + curr[m+1:]
                            if adj not in deadend_set:
                                adjacent.append(adj)
                        # adjacents are populated
                        adjacency[curr] = adjacent
        
        # adjacency list is fully populated
        print("populated adjacency")
        # perform bfs to get to target from 0000
        queue = deque()
        queue.append("0000")
        turns = 0
        visited = set()
        visited.add("0000")
        while queue:
            qlen = len(queue)
            for i in range(qlen):
                # explore
                src = queue.popleft()
                
                if src == target:
                    return turns
                
                
                
                # not at target yet. explore all adjacents
                
                for dest in adjacency[src]:
                    # don't revisit
                    if dest in visited:
                        continue
                    visited.add(dest)
                    queue.append(dest)
            turns+=1
        return turns if target in visited else -1

