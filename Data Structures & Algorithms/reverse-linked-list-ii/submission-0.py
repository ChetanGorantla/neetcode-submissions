# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # not in place
        # create a new head
        curr = head

        left_head = ListNode(-501)
        result = left_head
        # answer is result.next

        #iterable = ListNode(None, head)
        i = 1
        while (i < left):
            left_head.next = ListNode(curr.val)
            left_head = left_head.next
            curr = curr.next
            i+=1
        # attach left_head.next to reversed portion

        # starting from curr, create a reversed linked list till right
        reversed_head = ListNode(curr.val, None)
        curr = curr.next
        i+=1

        while (i <= right):
            next_node = ListNode(curr.val, reversed_head)
            reversed_head = next_node
            curr = curr.next
            i+=1
        
        # retrieve the remaining
        left_head.next = reversed_head

        while (reversed_head.next):
            reversed_head = reversed_head.next
        

        reversed_head.next = curr

        return result.next







