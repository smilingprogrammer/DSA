class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        if s1 == s2:
            return True
      
        multiple_swap = [i for i in range(len(s1)) if s1[i] != s2[i]]

        if len(multiple_swap) != 2:
            return False

        i, n = multiple_swap
        return s1[i] == s2[n] and s1[n] == s2[i]