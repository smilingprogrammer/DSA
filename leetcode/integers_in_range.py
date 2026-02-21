class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        for num in range(left, right + 1):
            covered = False

            for num_list in ranges:

                start = num_list[0]
                end = num_list[1]
                if start <= num <= end:
                    covered = True
                    break

            if not covered:
                return False

        return True