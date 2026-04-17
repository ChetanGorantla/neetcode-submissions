class Solution {
    public int minimumRecolors(String blocks, int k) {
        //keep track of W count and B count
        //store two variable states, exiting and entering
        //keep l and r pointer for sliding window
        int l = 0;
        int r = k-1;
        int w = 0;
        int b = 0;
        
        for (int i = l; i <= r; i++){
            if (blocks.charAt(i) == 'W'){
                w++;
            }else{
                b++;
            }
        }
        System.out.println("W: " + w + " B: " + b);
        Character exiting;
        Character entering;
        int minw = w;
        while (r < blocks.length()-1){
            
            exiting = blocks.charAt(l);
            entering = blocks.charAt(r+1);
            if (exiting == 'W'){
                w--;
            }else{
                b--;
            }
            if (entering == 'W'){
                w++;
            }else{
                b++;
            }
            l++;
            r++;
            System.out.println("W: " + w + " B: " + b);
            minw = Math.min(minw, w);
        }
        return minw;

    }
}