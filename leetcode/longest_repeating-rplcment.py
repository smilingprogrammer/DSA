class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        c = Counter()
        left = maximum = 0

        for i, j in enumerate(s):
            c[j] += 1
            maximum = max(maximum, c[j])
            if i - left + 1 - maximum > k:
                
                c[s[left]] -= 1
                left += 1
                
        return len(s) - left