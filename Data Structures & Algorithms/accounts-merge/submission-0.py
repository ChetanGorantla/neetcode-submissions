class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # create connection between emails, not names
        # maintain a hashmap that maps emails to names
        # build all email connections
        # go through every email and explore its full connected component
        # add it to visited so we don't re-explore it
        # for this connected component, before calling, track the name
        # within the dfs call, update a list of emails explored
        # after exiting the dfs call, sort the emails, concatenate it
        # with the name, and append it to out

        adjacency = defaultdict(list)
        mapped = {}
        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                # this will contain a cycle to itself but
                # if we append to a visited array that won't matter
                # if this email is already in adjacency, append the emails
                
                adjacency[email].extend(emails)
                mapped[email] = name
        
        # populated our adjacency and mappings
        # explore all unvisited emails
        visited = set()
        out = []
        def dfs(curr, connections):
            nonlocal visited
            if curr not in visited:
                # explore this
                visited.add(curr)
                connections.append(curr)
                # explore neighbors
                for neighbor in adjacency[curr]:
                    dfs(neighbor, connections)

        for email in adjacency:
            if email in visited:
                continue
            # this email hasn't been explored yet
            name = mapped[email]
            # explore it recursively
            connections = []
            dfs(email, connections)
            # connections is now populated
            connections.sort()
            out.append([name]+connections)

        return out

            