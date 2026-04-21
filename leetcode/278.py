# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1

        left, right = 1, n
        while left < right:
            middle = (left + right)//2

            if isBadVersion(middle):

                print(isBadVersion(middle))
                right = middle

            else:
                left = middle + 1
        
        return left