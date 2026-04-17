class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> maxheap = new PriorityQueue<>(
            (a,b) -> Integer.compare(b[0] * b[0] + b[1] * b[1], a[0] * a[0] + a[1] * a[1])
        );
        for (int i = 0; i < points.length; i++){
            int[] coords = points[i];
            maxheap.offer(coords);
            if (i >= k){
                maxheap.poll();
            }
        }
        int[][] out = new int[k][2];
        for (int i = 0; i < k; i++){
            out[i] = maxheap.poll();
        }
        return out;
        

        
    }
}
