class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        minimum_appearance = len(nums)//3
        
        # return list(set([n for n in nums if nums.count(n) > minimum_appearance]))
        c = Counter(nums)

        return [k for k, v in c.items() if v > minimum_appearance]