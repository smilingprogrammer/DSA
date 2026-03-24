class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")

        window = sum(1 for c in s[:k] if c in vowels)
        max_vowels = window

        for i in range(k, len(s)):
            window += (s[i] in vowels) - (s[i - k] in vowels)
            max_vowels = max(max_vowels, window)

            if max_vowels == k:
                break

        return max_vowels