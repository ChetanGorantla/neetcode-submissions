class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> minheap = new PriorityQueue<>();
        for (int i = 0; i < nums.length; i++){
            int curr = nums[i];
            minheap.offer(curr);
            if (i >= k){
                minheap.poll();
            }
            System.out.println("Current queue: " + minheap);
        }
        return minheap.peek();
    }
}
