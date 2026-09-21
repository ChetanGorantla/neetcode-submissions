class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # we can only traverse words that have a one character difference
        # switch to iterative bfs based on a wildcard adjacency list
        wildcards = {}
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                curr = word[:i] + "*" + word[i+1:]
                if curr not in wildcards:
                    wildcards[curr] = []
                
                wildcards[curr].append(word)
        # wildcard list populated
        # perform bfs from beginWord to see if we can
        # reach endWord
        print(wildcards)
        queue = deque()
        queue.append(beginWord)
        visited = set()
        level = 1
        
        while queue:
            qlen = len(queue)
            for j in range(qlen):
                curr = queue.popleft()
                if curr in visited:
                    continue
                
                if curr == endWord:
                    return level
                visited.add(curr)
                # not explored and not at destination yet
                # loop through all wildcards for curr
                for i in range(len(curr)):
                    wild = curr[:i] + "*" + curr[i+1:]
                    # explore all neighbors
                    for neighbor in wildcards[wild]:
                        queue.append(neighbor)
            level+=1
        
        return 0
