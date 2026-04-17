class Solution {
    public long pickGifts(int[] gifts, int k) {
        int sum = 0;
        PriorityQueue<Integer> maxheap = new PriorityQueue<>(Collections.reverseOrder());

        for (int gift: gifts){
            maxheap.offer(gift);
            sum+=gift;
        }
        System.out.println(maxheap);
        for (int i = 0; i < k; i++){
            int max = maxheap.poll();
            int replace = (int) (Math.sqrt(max));
            maxheap.offer(replace);
            System.out.println("Replacing " + max + " with " + replace);
            sum-=max;
            sum+=(replace);
        }
        return sum;
    }
}