class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        left, right = 0, n
        first = 0

        while left <= right:
            middle = (left + right) // 2
            if middle * (middle + 1) // 2 <= n:
                first = middle
                left = middle + 1

            else:
                right = middle - 1

        return first