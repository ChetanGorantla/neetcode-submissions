class Solution {
    public boolean checkInclusion(String s1, String s2) {
        
        int[] checkerlist = new int[26];
        for (int i = 0; i < s1.length(); i++){
            Character curr = s1.charAt(i);
            checkerlist[curr-97]++;
        }
        int l = 0;
        int r = l+s1.length();
        System.out.println("Is " + s1 + " in " + s2 + "?");
        while (r <= s2.length()){ //r < s2.length()
            String currstr = s2.substring(l, r);
            int[] currlist = new int[26];
            for (int i = 0; i < currstr.length(); i++){
                Character ca = currstr.charAt(i);
                currlist[ca-97]++;
            }
            int matches = 0;
            for (int i = 0; i < 26; i++){
                matches += Math.min(checkerlist[i], currlist[i]);
            }
            System.out.println("s1: " + s1 + Arrays.toString(checkerlist));
            System.out.println("s2: " + currstr + Arrays.toString(currlist));
            System.out.println("Matches: " + matches);
            
            if (matches != s1.length()){
                l += (s1.length() - matches);
                r += (s1.length() - matches);
            }else{
                return true;
            }
        }
        return false;

    }
}
