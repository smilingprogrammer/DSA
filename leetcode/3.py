class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s = list(s)
        result = []
        max_len = 0

        for char in s:
            if char in result:
                result = result[result.index(char) + 1:]

            result.append(char)
            max_len = max(max_len, len(result))

        return max_len