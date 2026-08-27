class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # one node must have the indegree of everyone
        # and the outdegree of nobody
        # we can just track the counts rather than the actual people
        outdegree = defaultdict(int)
        indegree = defaultdict(int)
        for u, v in trust:
            outdegree[u]+=1
            indegree[v]+=1
        print(outdegree)
        print(indegree)
        for i in range(1, n+1):
            if indegree[i] == n-1 and i not in outdegree:
                return i
        
        return -1
