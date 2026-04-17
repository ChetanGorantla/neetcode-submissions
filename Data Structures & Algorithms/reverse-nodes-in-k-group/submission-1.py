# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # define a hashmap that points the original group heads 
        # to the inverted group heads
        # we want to loop thru all of the original group heads at k steps
        # and create new nodes that are in the reverse order

        mapping = {}

        curr = head

        starting = curr
        reverse = None
        idx = 0
        while curr:
            if (idx % k == 0 and idx > 0): 
                # store the current value of reverse in the hashmap
                mapping[reverse] = starting
                print(f"{reverse.val}: {starting.val}")
                # change the starting value
                starting = curr
                reverse = None
            
            # now that secondary is updated to the proper value,
            # we need to reverse 

            nxt = curr.next
            curr.next = reverse
            reverse = curr
            curr = nxt
            idx+=1


        reverse_last = True
        if idx % k == 0:
            reverse_last = False
            mapping[reverse] = starting

        
        # we only care about the first value because first is always
        # connected to the last
        #
        # so we just need to consider all of the 
        # actually we care about the last values and the first values
        # because we want to point the prev last value to the curr first val
        # and if the prev last value does not exist
        # we want to initialize overall to be curr first val
        overall = None
        
        prev = None
        for k in mapping:
            if prev == None:
                # initialize overlal
                overall = k
                prev = mapping[k]
            else:
                # if prev exists
                prev.next = k
                prev = mapping[k]
            # either way, it'll point to the last value
            #print(f"{str(a.val)}:{str(mapping[a].val)}")

        out = overall

        while overall.next:
            overall = overall.next
        
        # update overall
        #print(starting.val, starting.next)
        #print(reverse.val, reverse.next.val)


        straight = None
        if reverse_last:
            while reverse:
                nxt = reverse.next
                reverse.next = straight
                straight = reverse
                reverse = nxt
                
            overall.next = straight
        return out
