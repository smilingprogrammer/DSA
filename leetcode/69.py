class Solution:
    def mySqrt(self, x: int) -> int:
        
        left, right = 1, x
        output = 0

        while left <= right:

            middle = (left + right) // 2

            mul_middle = middle * middle

            # print(mul_middle)

            if mul_middle == x:
                return middle
            elif mul_middle < x:
                output = middle
                left = middle + 1
            else:
                right = middle - 1
                # print(right)

        return output