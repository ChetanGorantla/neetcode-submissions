class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int num: nums){
            if (map.containsKey(num)){
                map.put(num, map.get(num)+1);
            }else{
                map.put(num, 1);
            }
        }
        int target = (int)(nums.length/2);
        for (int key: map.keySet()){
            if (map.get(key) > target){
                return key;
            }
        }
        return -1;
    }
}