class Solution {

    public String encode(List<String> strs) {
        String completed = "";
        for (String str: strs){
            completed += str.length();
            completed += "#";
            completed+=str;
        }
        System.out.println(completed);
        return completed;
        

    }

    public List<String> decode(String str) {
        List<String> arr = new ArrayList<>();
        int l = 0;
        int r = str.length();
        while (l < r){
            int i = l;
            
            while (str.charAt(i) != '#'){
                i++;
            }
            String lengthsubstring = str.substring(l,i);
            int currlen = Integer.parseInt(lengthsubstring);
            l = i+1;//skip the pound
            arr.add(str.substring(l, l+currlen));
            l += currlen;

        }
        return arr;
    }
}
