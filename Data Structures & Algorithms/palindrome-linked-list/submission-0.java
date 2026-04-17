/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        //find midpoint and length
        ListNode slow = head;
        ListNode fast = head;
        int size = 0;
        while (fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
            size++;
        }
        //size is now the position of slow pointer
        if (fast == null){
            size *= 2;
        }else{
            size = (size * 2) + 1;
        }

        ArrayList<Integer> first = new ArrayList<>();
        ArrayList<Integer> second = new ArrayList<>();
        System.out.println(size);
        System.out.println(Math.ceil((double) size/2));
        for (int i = 0; i < (int)Math.ceil((double)size/2); i++){
            first.add(head.val);
            second.add(slow.val);
            head = head.next;
            slow = slow.next;

        }
        System.out.println(first);
        System.out.println(second);

        for (int i = 0; i < first.size(); i++){
            if (first.get(i) != second.get(second.size()-i-1)){
                return false;
            }
        }
        return true;
    }
}