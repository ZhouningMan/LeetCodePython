from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        size = len(deck)

        # indices are the output order indices
        indices = deque([x for x in range(size)])
        output = [0] * size
        i = 0
        while indices:
            # get the head of the output array
            idx1 = indices.popleft()
            # reconstruct the array
            output[idx1] = deck[i]
            i += 1
            if indices:
                # poll the next and add to the tail
                indices.append(indices.popleft())
        return output

