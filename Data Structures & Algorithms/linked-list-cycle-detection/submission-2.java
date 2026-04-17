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
    public boolean hasCycle(ListNode head) {
        ListNode head2 = head;
        //fast and slow (1 step vs 2 steps)
        //if the fast and slow pointer ever meets at the same node, return true
        if (head.next == null){
            return false; //if the linked list is one element long, theres no loop
        }
        while ((head != null) && (head2 != null)){ //while both pointers still exist
            head = head.next;//slow
            head2 = head2.next.next;//fast
            if (head == head2){//if slow meets fast return true
                return true;
            }
        }
        return false; //slow never met fast and they both went to the end (null)
    }
}
