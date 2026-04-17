class Solution {
    public String mergeAlternately(String word1, String word2) {
        String out = "";
        int i = 0;
        while (i < word1.length() && i < word2.length()){
            out += word1.charAt(i);
            out += word2.charAt(i);
            i++;
        }
        out+=word1.substring(i);
        out+=word2.substring(i);
        return out;
        
    }
}