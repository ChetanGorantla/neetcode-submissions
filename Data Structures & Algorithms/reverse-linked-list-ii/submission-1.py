# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # this is just the same as that other problem
        # we need to locate the positions of both left and right
        # and then we need to go  until left == right
        # such that we maintain prev and curr
        # prev = None
        # curr = left
        # first_next = first.next
        # first.next = prev
        # prev = first
        # first = first_next


        # we need two jumps, one at the start and one at the end
        total_head = head

        first = head
        curr_ind = 1
        print("Finding left")
        while curr_ind < left-1:
            curr_ind+=1
            first = first.next
        # first.next points to wherever we want to bridge the jump
        print(first.val)
        # figure out the jump position
        second = head
        curr_ind = 1
        print("Finding right")
        while curr_ind < right+1:
            curr_ind+=1
            second = second.next
        print(second.val if second else "null")
        # second is right after the jump
        # at the very end of the reversal we need to set 
        # prev should be first
        print("Reversing")
        prev = second
        if left == 1:
            curr = head
        else:
            curr = first.next
        while curr != second:
            print(f"{curr.val} now points to {prev.val if prev else "null"}")
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        if left == 1:
            return prev
        else:
            print("PREV:", prev.val)
            first.next = prev
            return total_head
        # return the starting node
        # oo need to track edge case for right, it'll correctly point to None

