class Solution {
    public int characterReplacement(String s, int k) {
        
        int maxlen = 0;
        if (s.length() == 1){
            return 1;
        }
        int l = 0;
        int r = 1;
        while (r < s.length()){
            int[] sub = new int[26];
            int maxchar = 0;
            int maxcount = 0;
            for (int i = l; i <= r; i++){
                sub[s.charAt(i)-'A']++;
            }
            for (int i = 0; i < 26; i++){
                maxcount = Math.max(maxcount, sub[i]);
                if (maxcount == sub[i]){
                    maxchar = i;
                }
            }
            //located max char
            if ((r-l+1)-maxcount <= k){
                maxlen = Math.max(r-l+1, maxlen);
                r++;
            }else{
                l++;
                
            }

        }
        return maxlen;
        
        
    }
}
