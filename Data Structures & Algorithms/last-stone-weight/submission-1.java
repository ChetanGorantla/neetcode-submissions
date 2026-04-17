class Solution {
    public int lastStoneWeight(int[] stones) {
        //first try brute force
        PriorityQueue<Integer> maxheap = new PriorityQueue(Collections.reverseOrder());
        for (int stone: stones){
            maxheap.add(stone);
        }
        if (maxheap.size() < 2){
            return maxheap.poll();
        }
        int y = 0;
        while (maxheap.size()>1){
            y = maxheap.poll();
            int x = maxheap.poll();
            System.out.println(y + " " + x);
            if (y > x){
                maxheap.add(y-x);
                System.out.println("Cracked");
                
            }else{
                System.out.println("Broken");
            }
        }
        if (maxheap.isEmpty()){
            return 0;
        }else{
            return maxheap.poll();
        }
        
        
    }
}
