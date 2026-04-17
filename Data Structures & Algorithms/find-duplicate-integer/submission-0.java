class Solution {
    public int findDuplicate(int[] nums) {
        int slow = 0;int fast = 0;
        while (true){
            slow = nums[slow];//incr by 1 position
            fast = nums[nums[fast]]; //incr by 2 positions
            if (slow == fast){
                break; //we found the position where fast meets slow which is x distance from the start of the cycle
            }
        }
        
        int slow2 = 0; //slow2 starts from start of the linked list and is p distance from cycle start
        //we keep slow x distance from cycle start which is equal to p by Floyd's algorithm
        while (true){
            slow = nums[slow];
            slow2 = nums[slow2];
            if (slow == slow2){
                return slow; //return either slow or slow 2 as they both equal the start of the cycle
            }
        }
    }
}
