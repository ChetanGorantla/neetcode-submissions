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
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;//left pointer
        ListNode curr = head;//right pointer
        while (curr != null){
            ListNode nxt = curr.next;//storing the next pointer location
            curr.next = prev;//point current to previous
            prev = curr;//basically prev++
            curr = nxt;//basically curr++
            
        }
        return prev;//prev is the head when curr is null
    }
}
