class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        
        mapping = Counter(hand)

        numGroups = len(hand) // groupSize


        for i in range(len(hand)):
            card = hand[i]
            
            if mapping[card] == 0:
                continue

            for j in range(groupSize):
                next_card = card + j

                if mapping[next_card] == 0:
                    return False
                
                mapping[next_card] -= 1

        return True