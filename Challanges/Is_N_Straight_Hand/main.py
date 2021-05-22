"""
Alice has a hand of cards, given as an array of integers.
Now she wants to rearrange the cards into groups so that each group is size groupSize, and consists of groupSize consecutive cards.
Return true if and only if she can.
"""


from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand = sorted(hand)
        # If cant even get split up evenly
        if len(hand) % groupSize != 0: return False

        while True:
            if len(hand) < groupSize:
                if len(hand) != 0:
                    return False
                return True
            num = hand[0]
            hand.pop(0)
            for c in range(0, groupSize - 1):
                num += 1
                try:
                    hand.pop(hand.index(num))
                except:
                    return False



print(Solution.isNStraightHand(Solution, [1,2,3,6,2,3,4,7,8], 3))