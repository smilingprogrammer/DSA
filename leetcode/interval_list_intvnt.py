class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        i, j = 0, 0

        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]

            lo = max(a_start, b_start)
            hi = min(a_end, b_end)

            if lo <= hi:
                result.append([lo, hi])

            if a_end < b_end:
                i += 1
            else:
                j += 1

        return result
