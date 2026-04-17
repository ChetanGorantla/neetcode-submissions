class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # return 101 as a base case if this word is not matching and cannot be changed any further
        # (there are no remaining words left in the list that constitute a move)

        # when we call bfs, initialize min words to 100 so that all the 101 calls are not optimal

        # return the min lvl when doing bfs

        # only put in nodes that have not been visited yet


        

        # initial base case is that endWord is not even in the wordList
        if endWord not in wordList:
            return 0

        # first we need to create the adjacency list
        adjacency = {}
        
        # initialize adjacency list
        adjacency[beginWord] = []
        for word in wordList:
            adjacency[word] = []
        
        # our frequency map has been created, now form edges
        for a in adjacency:
            for b in adjacency:
                if a != b:
                    # compute the normalized distance
                    distance = 0
                    for i in range(len(a)):
                        if a[i] != b[i]:
                            distance+=1
                    # divide distance by 2 because if there is a character mismatch,
                    # there will be 2 chars affected, not just one
                    if distance == 1:
                        # create an edge IF an edge does not already exist between these two nodes
                        # how can we check if an edge does not exist?
                        # we need to check if b is in the adjacency list of a
                    
                        self.createEdge(a, b, adjacency)
                    
        
        
        # our adjacency list has been created 
        print(adjacency)
        
        # now we need to perform bfs on the beginWord
        queue = deque()
        level = 1
        queue.append(beginWord)

        visited = set([])
        while queue:
            qsize = len(queue)

            for i in range(qsize):
                # poll
                node = queue.popleft()
                # mark as visited
                visited.add(node)
                # check if this node is the endWord
                if node == endWord:
                    return level
                
                # this node isn't the endWord. keep exploring
                # explore neighbors that haven't been visited
                for neighbor in adjacency[node]:
                    if neighbor not in visited:
                        # explore this
                        queue.append(neighbor)
                

            level += 1

        return 0

    def populateFrequencies(self, frequencies, word):
        temp_freq = [0] * 26
        for char in word:
            temp_freq[ord(char)-ord('a')]+=1
        frequencies[word] = temp_freq

    def createEdge(self, a, b, adjacency):
        already_edge = b in adjacency and a in adjacency[b]
        if already_edge:
            return
        
        if a in adjacency:
            adjacency[a].append(b)
        else:
            adjacency[a] = [b]
        
        if b in adjacency:
            adjacency[b].append(a)
        else:
            adjacency[b] = [a]



