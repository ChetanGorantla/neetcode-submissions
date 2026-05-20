class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # maintain a dictionary of the indices that the tasks initially appear in
        # to match the results at the end to output properly

        # complete minheap
        # python heapq uses minheap by default


        # edge case: we have finished a previous task that went over time for multiple tasks
        # now we have the option to do multiple tasks, let's say two different tasks
        # with two different available times, but both valid for us
        # we can't judge only based on start time in that case
        # but we also can't judge first on shortest processing time because we need to act on the earliest tasks
        

        # first we want to check the tasks that are available
        # then from those, we want to check the tasks that are the shortest
        # then from those, we want to check the task that has the lowest index
        original = list.copy(tasks)
        indices = {}
        for i, task in enumerate(tasks):
            indices[(task[0], task[1])] = i

        tasks.sort()
        
        # subtract the front's value by the current time to check for validity
        # bruh do i need to make my own binary search insertion

        # don't insert based on availability - sort it and loop through the sorted times
        # and insert based on completion time in our priority queue, and then by index

        # double loop
        # iterate over the availability
        # and inside iterate while the heap exists
        time = 1
        i = 0
        n = len(tasks)
        order = []
        available = []

        while i < n or len(available) > 0:
            print(time)
            # need the idle case, where we just jump to the next task

            # only jump ahead if no available poppable
            # synonymous for time = max(time, tasks[i][0])?
            if not available and i < n and tasks[i][0] > time:
                time = tasks[i][0]
                print(f"idling to time {time}")

            
            while i < n and tasks[i][0] <= time:
                # populate the heap with available tasks
                heapq.heappush(available, (tasks[i][1], indices[tuple(tasks[i])]))
                print(f"pushing task {tasks[i]}")
                i+=1
            
            # we actually don't digest alltogether
            # we populate alltogether, but only digest one at a time to allow entry in the future

            
            popped = heapq.heappop(available)
            print(f"popping {original[popped[1]]}")
            time += popped[0]
            order.append(popped[1])
        
        return order
        

