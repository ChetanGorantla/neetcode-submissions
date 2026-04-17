class Solution {
    public String longestCommonPrefix(String[] strs) {
        String pastprefix = "";
        String prefix = "";
        int j = 0;
        int shortestlength = Integer.MAX_VALUE;

        for (int i = 0; i < strs.length; i++){
            shortestlength = Math.min(shortestlength, strs[i].length());
        }
        while (j < shortestlength){
            j++;
            pastprefix = prefix;
            prefix = strs[0].substring(0, j);
            for (int i = 0; i < strs.length; i++){
                if (strs[i].substring(0,j).equals(prefix)){
                    continue;
                }else{
                    return pastprefix;
                }
            }
        }
        return prefix;
        
    }
}