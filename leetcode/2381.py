class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction == 1:
                diff[start] += 1
                diff[end + 1] -= 1
            else:
                diff[start] -= 1
                diff[end + 1] += 1

        result = []
        net_shift = 0

        for i, ch in enumerate(s):
            net_shift += diff[i]

            shift_amount = net_shift % 26
            new_char = chr((ord(ch) - ord('a') + shift_amount) % 26 + ord('a'))
            result.append(new_char)

        return "".join(result)