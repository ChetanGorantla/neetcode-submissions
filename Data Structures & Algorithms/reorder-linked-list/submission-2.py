# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # we need to reverse the secon half
        # and then do two pointers to reorder

        second = head
        fast = head
        while fast and fast.next:
            second = second.next
            fast = fast.next.next
        # second now sits at the first value of the second half
        # we need to reverse from second onwards
        curr = second
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # we've rotated the second half
        # now we need to jump pointers
        first = head
        second = prev
        #print(first.val)
        #print(second.val)
        while first.next and second.next:
            nxt1 = first.next
            nxt2 = second.next
            first.next = second
            second.next = nxt1
            first = nxt1
            second = nxt2
        #return head