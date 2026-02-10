class Solution:    
    def findUnion(self, a, b):
        # code here
        union = a + b
        union = set(union)
        return sorted(union)