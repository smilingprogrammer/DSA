class Solution:
    def validPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return s[l+1:r+1] == s[l+1:r+1][::-1] or s[l:r] == s[l:r][::-1]

            l += 1
            r -= 1

        return True


        # if s == s[::-1]:
        #     return True

        # for i in range(len(s)):
        #     c1 = s[:i] + s[i+1:]
        #     c2 = c1[::-1]
        #     if c1 == c2:
        #         return True

        # return False