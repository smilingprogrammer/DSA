class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        sort_a = sorted(a)
        sort_b = sorted(b)
        
        if sort_a == sort_b:
            return True
            
        else:
            return False
        # print(sort_a)
        # for num in a:
        #     if num in b:
                