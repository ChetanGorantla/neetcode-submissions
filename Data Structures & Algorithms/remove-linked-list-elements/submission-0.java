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
    public ListNode removeElements(ListNode head, int val) {
        ListNode start = new ListNode(0);
        ListNode out = start;
        start.next = head;
        while (start.next != null){
            if (start.next.val == val){
                start.next = start.next.next;
            }else{
                start = start.next;
            }
            
        }
        
        return out.next;
    }
}