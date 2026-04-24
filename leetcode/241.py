class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def recur(expression):

            res = []

            for i in range(0, len(expression)):
                op = expression[i]

                if op == '*' or op == '+' or op == '-':

                    a = expression[:i]
                    b = expression[i + 1 :]

                    nums1 = recur(a) 
                    nums2 = recur(b)

                    for n1 in nums1:
                        for n2 in nums2:

                            if op == '*':

                                res.append(n1 * n2)

                            elif op == '+':
                                
                                res.append(n1 + n2)

                            elif op == '-':

                                res.append(n1 - n2)

            if res == []:
                res.append(int(expression))
                
            return res



        return recur(expression)