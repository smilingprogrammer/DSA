class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        # for i in range(len(s)-1, -1, -1):
        #     s[0] = s.append(s[i])
        #     s.pop(i)
        while l < r:
            s[l], s[r] = s[r], s[l]
            
            l += 1
            r -= 1
