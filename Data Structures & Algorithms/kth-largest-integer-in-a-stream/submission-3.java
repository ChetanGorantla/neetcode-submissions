class KthLargest {
    public PriorityQueue minheap;
    public int size;
    public KthLargest(int k, int[] nums) {
        minheap = new PriorityQueue<>();
        size = k;
        for (int i = 0; i < nums.length; i++){
            minheap.offer(nums[i]);
            if (i >= k){
                minheap.poll();
            }
            
        }
        System.out.println("Current queue: " + minheap);
        

    }
    
    public int add(int val) {
        if (minheap.size() >= size){
            System.out.println("Removing a " + minheap.peek() + " and inputting a " + val);
            minheap.offer(val);
            int removed = (int) minheap.poll();
            System.out.println(minheap);
            return (int) minheap.peek();
        }else{
            minheap.offer(val);
            return (int) minheap.peek();
        }
    }
}
