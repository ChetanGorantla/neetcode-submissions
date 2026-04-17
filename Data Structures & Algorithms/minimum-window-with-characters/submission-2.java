class Solution {
    public String minWindow(String s, String t) {
        if (t.length() > s.length()){
            return "";
        }
        if (t.length() == 1 && s.length() == 1){
            if (Objects.equals(t,s)){
                return t;
            }
        }
        int[] tarr = new int[58];
        for (Character c: t.toCharArray()){
            tarr[c-65]++;
        }
        //target array is now defined
        //minimum window for checking is the target length
        int l = 0;
        int r = t.length();
        int minlength = Integer.MAX_VALUE;
        String minstr = "";
        while ((l < r)&&((l <= s.length()-t.length()) && (r <= s.length()))){//while in bounds
            String currsub = s.substring(l, r);
            System.out.println(currsub);
            int[] currarr = new int[58];
            for (Character c: currsub.toCharArray()){
                currarr[c-65]++;
            }
            
            //System.out.println(Arrays.toString(currarr));
            //System.out.println(Arrays.toString(tarr));
            boolean eq = true;
            for (int i = 0; i < t.length(); i++){
                if (tarr[t.charAt(i)-65]>currarr[t.charAt(i)-65]){//its ok to have >= the target
                    eq = false;
                    break;
                }
            }
            if (eq){
                System.out.println("Found all characters");
                minlength = Math.min(currsub.length(), minlength);
                if (minlength == currsub.length()){
                    minstr = currsub;
                }
                //shift left to second matching
                if (l <= s.length()-t.length()){
                    System.out.println("Pushing up l");
                    if (l+1 < r){
                        for (int i = l+1; i < r; i++){
                            if (t.contains(s.charAt(i)+"")){
                                l = i;
                                break;
                            }
                    }
                    }else{
                        break;
                    }
                    
                }
                
            }else{
                
                r++;
            }

        }
        return minstr;
        
        
        
    }
}
