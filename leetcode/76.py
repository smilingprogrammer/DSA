class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        target, window = Counter(t), {}
        have, need = 0, len(target)

        ans, ansLen = [-1, -1], float('inf')
        left = 0

        for r in range(len(s)):
            curr_ch = s[r]
            window[curr_ch] = window.get(curr_ch, 0) + 1

            if curr_ch in target and window[curr_ch] == target[curr_ch]:
                have += 1

            while have == need:
                window_size = r - left + 1

                if window_size < ansLen:
                    ans = [left, r]
                    ansLen = window_size

                window[s[left]] -= 1

                if s[left] in target and window[s[left]] < target[s[left]]:
                    have -= 1

                left += 1

        l, r = ans
        return s[l:r + 1] if ansLen != float('inf') else ""