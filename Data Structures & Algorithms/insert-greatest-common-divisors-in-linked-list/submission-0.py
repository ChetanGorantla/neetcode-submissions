# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use built in math.gcd function
        
        curr = head
        while curr.next:
            # figure out gcd
            gcd = math.gcd(curr.val, curr.next.val)
            curr.next = ListNode(gcd, curr.next)
            curr = curr.next.next
        
        return head
        

