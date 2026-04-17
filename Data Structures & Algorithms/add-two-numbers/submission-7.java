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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode out = new ListNode();
        ListNode printer = new ListNode(0);
        printer.next = out;
        
        int over = 0;
        while (over>0 || ((l1 != null) || (l2 != null))){
            if (over > 0){
                out.next = new ListNode(over);
                System.out.println("next value is: " + out.next.val);
                if (((l1 == null) && (l2 == null))){
                    break;
                }
            }else{
                out.next = new ListNode(0);
            }
            
            out = out.next;
            int sum = 0;
            int val = 0;
            //check if l1 is null separately from l2 is null (one number has more decimal points)
            if (l1 == null){
                System.out.println("Only l2");
                sum+=l2.val;
                sum+=over;
                //say sum is 14
                //keep the 4, make over the 1
                val = sum % 10;
                if (sum == 10){
                    val = 0;
                }
                sum/=10;//grab second digit if any
                over = sum;
                l2 = l2.next;
            }else if (l2 == null){
                System.out.println("Only l1");
                sum+=l1.val;
                sum+=over;
                //say sum is 14
                //keep the 4, make over the 1
                val = sum % 10;//grab first digit
                if (sum == 10){
                    val = 0;
                }
                sum/=10;//grab second digit if any
                over = sum;
                l1 = l1.next;
            }else if ((l1 != null) && (l2 != null)){
                System.out.println("Finding sum of both");
                sum+= (l1.val + l2.val);
                sum+=over;
                val = sum % 10;
                if (sum == 10){
                    val = 0;
                }
                sum/=10;//grab second digit if any
                over = sum;
                l1 = l1.next;
                l2 = l2.next;
            }else{
                out.val = over;
                break;
            }
            out.val = val;
            
            System.out.println(out.val);
            System.out.println(over);
            
            
        }
        return printer.next.next;
    }
}
