class Solution {
    public int[] getFinalState(int[] nums, int k, int multiplier) {
        PriorityQueue<int[]> minheap = new PriorityQueue<>((a, b) -> {
            int cmp = Integer.compare(a[0], b[0]);  // compare first index
            if (cmp == 0) {
                return Integer.compare(a[1], b[1]); // if equal, compare second index
            }
            return cmp;
        });
        int j = 0;
        for (int num: nums){
            minheap.offer(new int[] {num, j});
            j++;
        }
        System.out.println(minheap);
        for (int i = 0; i < k; i++){

            int[] polled = minheap.poll();
            int retrieved = polled[0];
            int index = polled[1];
            minheap.offer(new int[] {retrieved * multiplier, index});
            nums[index] = retrieved * multiplier;
            System.out.println("Replacing " + retrieved + " with " + retrieved * multiplier);
            
        }
        
        return nums;
        

    }
}