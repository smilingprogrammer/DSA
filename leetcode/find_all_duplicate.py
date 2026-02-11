class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        seen_num = set()
        output = []

        for n in nums:
            if n in seen_num:
                output.append(n)
            else:
                seen_num.add(n)
            

        return output
