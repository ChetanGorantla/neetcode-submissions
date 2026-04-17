class Solution {
    public List<List<String>> partition(String s) {
        ArrayList<String> path = new ArrayList<>();
        ArrayList<List<String>> out = new ArrayList<>();
        findPalindromicSubstrings(s, 0, "", path, out, 0);
        return out;
        // need to continue down a path even if it's not
        // currently a palindrome

        // if you reach the end of the string and it's not a substring then
        // exit

        // go down a path
        // choose not to add anything to the path
    }

    private void findPalindromicSubstrings(String s, int idx, String currSubstring, List<String> path, List<List<String>> out, int used){
        if (idx == s.length()){
            if (used == s.length()){
                ArrayList<String> toAdd = new ArrayList<>(path);
                out.add(toAdd);
            }
            return;
        }

        if (idx > s.length()){
            return;
        }


        // go down a path
        currSubstring = currSubstring + s.charAt(idx);
        if (isPalindromic(currSubstring)){
            path.add(currSubstring);
            findPalindromicSubstrings(s, idx+1, "", path, out, used + currSubstring.length());
            path.remove(currSubstring);
            findPalindromicSubstrings(s, idx+1, currSubstring, path, out, used);
        }else{
            // don't add to the path, since it's not palindromic
            // only one option, to continue forward
            findPalindromicSubstrings(s, idx+1, currSubstring, path, out, used);
        }
        
        
    }

    private boolean isPalindromic(String s){
        int l = 0; int r = s.length()-1;
        while (l <= r){
            if (s.charAt(l) != s.charAt(r)){
                return false;
            }
            l++;
            r--;
        }
        return true;
    }


}
