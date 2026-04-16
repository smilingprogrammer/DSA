class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        def rec(level, index, ans):
            if level == 1:
                return ans

            if index % 2 == 1:
                return rec(level - 1, (index + 1) // 2, ans)

            return rec(level - 1, index // 2, 1 - ans)

        return rec(n, k, 0)
        
        # if n == 1:
        #     return 1
        # table = "0"
        # for i in range(2, n+1):

        #     if table[-1] == "0":
        #         table += "01"

        #     else:
        #         table += "10"

        # # print(table)

        # return table[k]