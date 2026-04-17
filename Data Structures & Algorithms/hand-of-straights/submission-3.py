class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True
        # sort and then loop thru maintaining a list of begins
        list.sort(hand)

        # if we find a duplicate value, start a new draw
        # continue each draw
        # keep a list of the draws
        # if we reach a conclusion where we go thru the list, and not all draws are of the correct size, 
        # we need to return false
        # otherwise return true
        # create a tuple that represents a draw (card, size)
        
        # we need to maintain a queue of draws and peek the most recent one whenevr we want to
        # continue a draw
        queue = deque()

        print(hand)
        queue.append((hand[0], 1))
        for i in range(1, len(hand)):
            prev_draw = queue[0] if len(queue) > 0 else (-1000, 1)
            curr_card = hand[i]
            prev_card = prev_draw[0]
            print(prev_card, curr_card)
            if prev_card == curr_card:
                # start a new draw
                print("equal cards, starting new draw")
                queue.append((curr_card, 1))
            else:
                # otherwise we can either continue a draw or start a new draw
                # check if this card continues our prev_draw
                # if so, continue the draw
                # otherwise start a new draw
                if curr_card == prev_card + 1:
                    print("continuing a draw")
                    queue.popleft()
                    new_draw = (curr_card, prev_draw[1]+1)
                else:
                    print("non continuous, starting new draw")
                    new_draw = (curr_card, 1)
                
                if new_draw[1] != groupSize:
                    print("appending draw")
                    queue.append(new_draw)
        
        print(queue)
        return len(queue) == 0
