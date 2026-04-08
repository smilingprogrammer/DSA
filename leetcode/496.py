class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in nums1:
            found = False
            passed = False
            for j in nums2:
                if j == i:
                    passed = True
                    # break
                elif j > i and passed:
                    result.append(j)
                    found = True
                    break

            if not found:
                result.append(-1)
                    

        return result