# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # reorder the list so that it follows a jumping order
        # do fast and slow pointer approach
        # reverse the second half (slow to the end)
        slow = head
        fast = head
        while fast and fast.next:
            print(fast.val)
            slow = slow.next
            fast = fast.next.next
        
        # slow is currently at the midpoint
        # 1 2 3 4 null
        print(slow.val)
        curr = slow
        prev = None
        while curr:
            print(f"1 {curr.val}")
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # prev points to the second half head

        # repoint head and slow
        # 1 2 3
        # 4 5
        start = head
        while prev:
            print(f"2 {start.val} {prev.val}")
            start_nxt = start.next
            slow_nxt = prev.next
            start.next = prev
            if start_nxt != prev:
                prev.next = start_nxt
            start = start_nxt
            prev = slow_nxt
        
        # we need to check to make sure start_nxt != prev
        

        
