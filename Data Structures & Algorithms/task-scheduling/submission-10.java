class Solution {
    public int leastInterval(char[] tasks, int n) {
        
        PriorityQueue<int[]> maxheap = new PriorityQueue<>((a,b) -> Integer.compare(b[0], a[0]));
        PriorityQueue<int[]> queue = new PriorityQueue<>((a,b) -> Integer.compare(a[0], b[0]));

        int[] frequencies = new int[26];
        
        for (char task: tasks){
            frequencies[task-'A']++;
            
        }

        // our frequencies list has been implemented, add these into our maxheap, since
        // our maxheap stores priority based on the frequency of the item

        int time = 0;

        for (int i = 0; i < 26; i++){
            // frequency, character
            int[] pair = new int[] {frequencies[i], i};
            if (pair[0] > 0){
                maxheap.offer(pair);
            }
            
        }
        System.out.println("frequency maxheap:");
        for (int[] pair: maxheap){
            System.out.print(Arrays.toString(pair) + " ");
        }
        System.out.println();
        System.out.println();
        // our maxheap is initialized
        int totalfreq = tasks.length;
        while (totalfreq > 0){
            System.out.println("Time: " + time);
            System.out.println("Queue: ");
            for (int[] pair : queue){
                System.out.print(Arrays.toString(pair) + " ");
            }
            System.out.println();
            // if our maxheap is empty, we need to take from our queue
            if (maxheap.isEmpty()){
                System.out.println("frequency max heap is empty. no tasks to do. jumping forward for idles");
                // match the idle times to get to the next value since there's no other choice
                if (queue.isEmpty()){
                    System.out.println("no queue elements to poll. exiting");
                    return time;
                }
                time = queue.peek()[0];
            }else{
                // decrement the frequency of the highest frequency item, and if valid, add into
                // queue with it's cooldown
                int[] polled_pair = maxheap.poll();
                System.out.println("Doing task " + (char) (polled_pair[1] + 'A'));
                polled_pair[0]--;
                frequencies[polled_pair[1]]--;
                totalfreq--;
                if (polled_pair[0] > 0){
                    // add it back into queue with new cooldown
                    queue.add(new int[] {time + n, polled_pair[1]});
                    System.out.println("Task completed, adding cooldown to queue");
                }else{
                    System.out.println("Task exhausted");
                }
            }

            // if task at front of queue is available, pop it and reinsert into heap
            if (!queue.isEmpty()){
                System.out.println("current time: " + time + ", compared to cooldown: " + queue.peek()[0]);
                System.out.println("Polled value: " + Arrays.toString(queue.peek()));
            }
            if (!queue.isEmpty() && time >= queue.peek()[0]){
                int[] cooldown_and_char = queue.poll();
                int[] new_pair = new int[]{frequencies[cooldown_and_char[1]], cooldown_and_char[1]};
                System.out.println("Cooldown met for task " + (char) (cooldown_and_char[1] + 'A') + ", re-entering frequency heap");
                
                maxheap.add(new_pair);
            }
            time++;
            System.out.println();
        }
        return time;




    }
    
}
