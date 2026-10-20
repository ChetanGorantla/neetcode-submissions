class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # sort based on increasing enqueue time, increasing processing time, then index
        # we can't sort based on increasing enqueue time,
        # we need to populate our priority queue at each level?
        # because at each level we extend to a new time
        # so we need to accumulate all tasks that are within that time
        # so just maintain a priority queue that sorts based on (processtime, index)
        # and after each level, based on the new time, update the priority queue
        # to add whatever unexplored tasks have enqueue time <= newtime
        # maintain a pointer to wherever we are in the tasks list
        # sort tasks
        # 
        # store indices
        indices = {}
        for i in range(len(tasks)):
            indices[tuple(tasks[i])] = i
        tasks.sort()
        #print(tasks)
        ind = 0
        # find the min starting time
        currtime = sys.maxsize
        for start, delay in tasks:
            currtime = min(currtime, start)
        
        pq = []
        out = []
        available = [True]*len(tasks)
        while pq or ind < len(tasks):
            # populate the pqueue with the tasks that we can start
            while ind < len(tasks) and tasks[ind][0] <= currtime:
                heapq.heappush(pq, (tasks[ind][1], indices[tuple(tasks[ind])]))
                ind+=1
            #print(currtime, pq)
            # take a heapq task
            # if the queue is empty then that means we couldn't start any tasks. Jump to the next task.
            if not pq:
                pq.append((tasks[ind][1], indices[tuple(tasks[ind])]))
                ind+=1
                while ind < len(tasks) and tasks[ind][0] == pq[0][0]:
                    pq.append((tasks[ind][1], indices[tuple(tasks[ind])]))
                    ind+=1
            curr = heapq.heappop(pq)
            currtime += curr[0]
            out.append(curr[1])
        
        return out

