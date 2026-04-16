class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # BODMAS
        all_operations= {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        stack = []

        for n in tokens:
            if n in all_operations:
                operation = all_operations[n](int(stack.pop(-2)), int(stack.pop(-1)))
              
                stack.append(int(operation))
            else:
                stack.append(int(n))

        return stack[0]