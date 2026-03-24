class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for c in s1:
            count1[ord(c) - ord('a')] += 1

        matches = 0
        k = len(s1)

        for i in range(k):
            idx = ord(s2[i]) - ord('a')
            count2[idx] += 1

        for i in range(26):
            if count1[i] == count2[i]:
                matches += 1

        if matches == 26:
            return True

        for i in range(k, len(s2)):

            right = ord(s2[i]) - ord('a')
            count2[right] += 1
            if count2[right] == count1[right]:
                matches += 1
            elif count2[right] == count1[right] + 1:
                matches -= 1

            left = ord(s2[i - k]) - ord('a')
            count2[left] -= 1
            if count2[left] == count1[left]:
                matches += 1
            elif count2[left] == count1[left] - 1:
                matches -= 1

            if matches == 26:
                return True

        return False