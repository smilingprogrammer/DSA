from collections import Counter

class Solution:
    def findWinners(self, matches):
        losses = Counter()
        players = set()

        for w, l in matches:
            players.add(w)
            players.add(l)
            losses[l] += 1

        not_lost = [p for p in players if losses[p] == 0]
        lost_one = [p for p in players if losses[p] == 1]

        return [sorted(not_lost), sorted(lost_one)]
