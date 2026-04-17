class Solution {
    private HashMap<Integer, String> letters;
    public List<String> letterCombinations(String digits) {
        if (digits.equals("")){
            return new ArrayList<>();
        }
        letters = new HashMap<>();
        letters.put(2, "abc");
        letters.put(3, "def");
        letters.put(4, "ghi");
        letters.put(5, "jkl");
        letters.put(6, "mno");
        letters.put(7, "pqrs");
        letters.put(8, "tuv");
        letters.put(9, "wxyz");
        List<String> out = new ArrayList<>();
        generateCombinations(digits, 0, "", out);
        return out;
    }

    private void generateCombinations(String digits, int idx, String path, List<String> out){
        if (idx == digits.length()){
            String toAdd = path;
            out.add(toAdd);
            return;
        }
        if (idx > digits.length()){
            return;
        }

        // explore possible choices at current idx
        String choices = letters.get(Integer.parseInt(digits.charAt(idx)+""));
        for (int i = 0; i < choices.length(); i++){
            generateCombinations(digits, idx+1, path+choices.charAt(i), out);
        }
    }
}
