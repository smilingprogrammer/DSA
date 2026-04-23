class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # [3,6,7,11]
        # 1 -> 3
        # 2 -> 4 rem 2
        # 3 -> 4 rem 5
        # 4 -> 4 rem 1
        # 5 -> 4
        # 6 -> 4
        # 7 -> 4
        def max_eat(speed):
            total = sum((size + speed - 1) // speed for size in piles)

            return total <= h

        left, right = 1, max(piles)

        first = 0

        while left <= right:
            middle = (left+right)//2
            if max_eat(middle):
                first = middle
                right = middle - 1

            else:
                left = middle + 1
            
        return first