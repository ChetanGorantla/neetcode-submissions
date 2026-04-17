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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        //find length
        int length = 0;
        ListNode a = head;
        while (a != null){
            a = a.next;
            length++;
        }
        if (length == 1){
            head = null;
            return head;
        }
        int index = length-n;//find index of element to remove
        //make prev.next = curr.next where curr is element at index
        int count = 0;
        //Create new listnode val 0 point to head, return listnode.next
        ListNode node = new ListNode(0);
        node.next = head;
        ListNode prev = node;
        ListNode curr = node.next;
        
        while (count < index){
            prev = curr;
            curr = curr.next;
            count++;
        }
        prev.next = curr.next;
        return node.next;
        

    }
}
