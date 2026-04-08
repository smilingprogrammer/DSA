class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        res = 0
        person = tickets[k]

        for i in range(len(tickets)):

            if i <= k:
                res += min(tickets[i], person)

            else:
                res += min(tickets[i], person - 1)

        return res