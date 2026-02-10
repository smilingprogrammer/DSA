class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:

        initial_start = 0

        for operand in operations:
            if operand == "++X" or operand == "X++":
                initial_start += 1

            else:
                initial_start -= 1

        return initial_start