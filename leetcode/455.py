class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()

        p, t = 0, 0

        while p < len(s) and t < len(g):
            if s[p] >= g[t]:
                t += 1
            p += 1

        return t