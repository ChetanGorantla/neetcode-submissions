class Solution {

    public String encode(List<String> strs) {
        int arraylength = strs.size();

        String combined = (((String)((arraylength+""))).length()) + "";
        combined += arraylength;
        
        for (int i = 0; i < strs.size(); i++){
            String str = strs.get(i);
            String currlen = str.length()+ "";
            combined+= currlen.length();
            combined += (currlen);
            combined += str;
        }
        System.out.println(combined);
        return combined;    
        

    }

    public List<String> decode(String str) {
        int arrlenlen = Integer.parseInt(str.charAt(0)+"");
        int arraylength = Integer.parseInt(str.substring(1, 1+arrlenlen) + "");
        int currindex = 1 + arrlenlen;
        System.out.println(arrlenlen);
        System.out.println(arraylength);
        List<String> arr = new ArrayList<>();
        for (int i = 0; i < arraylength; i++){
            int sizelength = Integer.parseInt(str.charAt(currindex)+"");
            System.out.println("Sizelength " + sizelength);
            currindex++;
            int currlen = Integer.parseInt(str.substring(currindex, currindex+sizelength)+"");
            currindex+= sizelength;
            int endpt = currindex+currlen;
            arr.add(str.substring(currindex, endpt));
            System.out.println("added " + str.substring(currindex, endpt));
            currindex = endpt;
        }
        return arr;
    }
}
