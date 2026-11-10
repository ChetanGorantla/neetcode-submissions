class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # group of 3 websites in a row that occured for the most users
        
        # use an array of simple appends to track triples
        # contribute towards an overall score
        # at each step figure out the max score based on what 
        # we just incremented

        # store a mapping of the triple to the set of users
        # use a set to ensure we don't double count a user

        # if timestamps are guaranteed to be increasing order,
        # we can disregard them

        # (web1, web2, web3) : set(user1, user2, ...)
        scores = defaultdict(set)
        maxscore = 0
        maxtriple = None

        # we need to maintain previous 2 websites for each user
        # and update them by pushing forward when a new site comes in
        # user : [prev2, prev1]
        previous = defaultdict(list)
        
        n = len(username)
        # it's not just the last 2
        # we can make a triple with any previously explored 
        # not guaranteed to be in ascending order
        # we need to bisect based on (timestamp, website)

        # we can't do it in order
        # we have to compute the overall timeline first
        # and proceed
        combined = sorted(zip(timestamp, username, website))
        
        timestamp, username, website = zip(*combined)

        for i in range(n):
            user = username[i]
            web = website[i]

            
            # take in this new entry
            # form a triple with all previous
            # should we use a heap or bisect insort?
            # for heap inserts are O(logn)
            # polling all cnadidates is O(nlogn)

            # for bisect insort heap inserts are O(n)
            # for bisect polling all caldidates is O(n)
            # which one is done more?
            # they both happen at the same time
            # we should go with O(n)

            # so let's go with bisect


            # test all curr_triple candidates
            # update the score if we have a successful triple
            prevs = previous[user]
            for i in range(len(prevs)):
                for j in range(i+1, len(prevs)):
                    curr_triple = (prevs[i], prevs[j], web)
            
                    scores[curr_triple].add(user)
                    if len(scores[curr_triple]) == maxscore:
                        # set to lexicographic lowest
                        maxtriple = min(maxtriple, curr_triple)
                    elif len(scores[curr_triple]) > maxscore:
                        maxtriple = curr_triple
                        maxscore = len(scores[curr_triple])
            
            # score has been updated


            # update previous
            previous[user].append(web)
        print(scores)
        return list(maxtriple)
