class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        output = 0
        piles.sort()

        for i in range(0, len(piles), 3):
            result = []

            result.append(piles[0])

            piles.pop(0)
            result.append(piles[-1])
            piles.pop()
            result.append(piles[-1])
            piles.pop()
            print(result)

            maximim = 0
            result.remove(max(result))

            output += max(result)
        
        return output