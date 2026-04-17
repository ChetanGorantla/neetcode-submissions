class Solution {
    public String mergeAlternately(String word1, String word2) {
        String out = "";
        int pos = 0;
        int lowest = Math.min(word1.length(), word2.length());
        while (pos < lowest){
            out+=(word1.charAt(pos) + ""+ word2.charAt(pos));
            pos++;
        }
        if (word1.length() != word2.length()){
            System.out.println(pos);
            if (word1.length() == pos){
                out+=word2.substring(pos);
            }else if (word2.length()==pos){
                out+=word1.substring(pos);
            }
        
        }
        return out;
        
    }
}